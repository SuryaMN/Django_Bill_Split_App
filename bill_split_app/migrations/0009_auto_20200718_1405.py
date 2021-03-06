# Generated by Django 3.0.7 on 2020-07-18 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_split_app', '0008_member_net_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenditure',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='amount_borrowed',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='expenditure_on_others',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='expenditure_on_self',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='net_payment',
            field=models.FloatField(default=0),
        ),
    ]
