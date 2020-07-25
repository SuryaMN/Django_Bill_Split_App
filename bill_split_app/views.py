from django.shortcuts import render,redirect,get_object_or_404
from . models import Member,Expenditure

# Create your views here.
def index(request):
    Member.objects.all().delete()
    Expenditure.objects.all().delete()
    return render(request,'bill_split_app/index.html')

def create_members(request):
    members_count = int(request.GET['members_count'])
    return render(request,'bill_split_app/create_members.html',{'members':list(range(1,members_count+1))})


def register(request):
    members_dict = request.GET
    members_list = list(members_dict.values())
    for member in members_list:
        member_object = Member(name=member)
        member_object.save()
    return redirect(bill)
    

def add_expenditure(request,member_id):
    member = get_object_or_404(Member , pk=member_id)
    new_expenditure = Expenditure(payer=member ,amount=int(request.GET['amount']) , payee=request.GET['payee'] , description=request.GET['description'])
    new_expenditure.save()
    return redirect(bill)


def bill(request):

    # class Counter:
    #     count = 0
        
    #     def increment(self):
    #         self.count+=1
    #         return None

    #     def reset(self):
    #         self.count = 0
    #         return None

    members_list = Member.objects.all()
    expenditures = Expenditure.objects.all()
    return render(request,'bill_split_app/bill.html',{'members':members_list , 'expenditures':expenditures})


# def calculate(request):
#     members = Member.objects.all()
#     for member in members:
#         expenditures = Expenditure.objects.filter(payer=member)
#         print(expenditures)
#         for expenditure in expenditures:
#             if expenditure.payee == "Self":
#                 member.expenditure_on_self += expenditure.amount
#                 member.save()
#             elif expenditure.payee == "Team":
#                 member.expenditure_on_others += expenditure.amount/len(members)*(len(members)-1)
#                 member.save()
#                 for i in members:
#                     if i.name != member.name:        
#                         i.amount_borrowed = int(i.amount_borrowed) + (int(expenditure.amount))/len(members)
#                         i.save()
#                         print(i,"borrowed",i.amount_borrowed,"from",member,"(TEAM)")
#             else:
#                 member.expenditure_on_others = int(member.expenditure_on_others) + int(expenditure.amount)
#                 member.save()
#                 payee = get_object_or_404(Member , name=expenditure.payee)
#                 payee.amount_borrowed = int(payee.amount_borrowed) + int(expenditure.amount)
#                 payee.save()
#                 print(payee,"borrowed",payee.amount_borrowed,"from",member)


#     return redirect(result)



# def result(request):
#     members = Member.objects.all()
#     net_amount = []
#     for i in members:
#         print(i.expenditure_on_others-i.amount_borrowed)
#         net_amount.append(i.expenditure_on_others-i.amount_borrowed)
#         i.expenditure_on_others = 0
#         i.expenditure_on_self = 0
#         i.amount_borrowed = 0
#         i.save()
#     print(net_amount)
    
#     return render(request,'bill_split_app/result.html',{'result':zip(members,net_amount)})



def calculate(request):
    members = Member.objects.all()
    d = {}
    for i in members:
        d[i.name] = [0,0,0]
    for member in members:
        expenditures = Expenditure.objects.filter(payer=member)
        for expenditure in expenditures:
            if expenditure.payee == "Self":
                d[member.name][1] += expenditure.amount

            elif expenditure.payee == "Team":
                d[member.name][0] += (expenditure.amount/len(members))*(len(members)-1)
                for j in members:
                    if j.name != member.name:
                        d[j.name][2] += (expenditure.amount/len(members))

            else:
                d[member.name][0] += expenditure.amount
                payee = get_object_or_404(Member,name=expenditure.payee)
                d[payee.name][2] += expenditure.amount
    for k in members:
        k.expenditure_on_others = d[k.name][0]
        k.expenditure_on_self = d[k.name][1]
        k.amount_borrowed = d[k.name][2]
        k.save()
    return redirect(result) 



def result(request):
    members = Member.objects.all()
    net_amount = []
    for i in members:
        i.net_payment = (i.expenditure_on_others-i.amount_borrowed)
        net_amount.append(i.expenditure_on_others-i.amount_borrowed)
        i.expenditure_on_others = 0
        i.expenditure_on_self = 0
        i.amount_borrowed = 0
        i.save()

    payees = Member.objects.filter(net_payment__lt = 0)
    payers = Member.objects.filter(net_payment__gt = 0)
    transactions=[]
    for payee in payees:
        for payer in payers:
            if (payer.net_payment!=0) and (payee.net_payment!=0):
                if (payer.net_payment <= (-payee.net_payment)):
                    msg = [payee.name,payer.net_payment,payer.name]
                    transactions.append(msg)
                    payee.net_payment+=payer.net_payment
                    payer.net_payment = 0
                    payer.save()

                else:
                    msg = [payee.name,-payee.net_payment,payer.name]
                    transactions.append(msg)
                    payer.net_payment+=payee.net_payment
                    payee.net_payment = 0
                    payer.save()
            
        payee.save()

    for i in members:
        i.net_payment = 0
        i.save()
    return render(request,'bill_split_app/result.html',{'transactions':transactions})