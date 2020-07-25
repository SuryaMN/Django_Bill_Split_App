# Generated by Django 3.0.7 on 2020-07-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_split_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='expenditure_on_others',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='expenditure_on_team',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='money_borrowed',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]