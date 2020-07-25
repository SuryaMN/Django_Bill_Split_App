function decrement(){
    number_field = document.getElementById('members_count');
    if (parseFloat(number_field.value) > parseFloat(number_field.min)){
        number_field.value = parseFloat(number_field.value)-1;
    }
    
}

function increment(){
    number_field = document.getElementById('members_count');
    if (parseFloat(number_field.value) < parseFloat(number_field.max)){
        number_field.value = parseFloat(number_field.value)+1;
    }
}


function dropdown(member){
    var dropdown = document.createElement('select');
    dropdown.name = "selected";
    var opt = document.createElement("option");
    opt.setAttribute("value","person");
    var txt = document.createTextNode("person")
    opt.appendChild(txt);
    dropdown.appendChild(opt);
    var target = document.getElementById(member)
    target.appendChild(dropdown);
}