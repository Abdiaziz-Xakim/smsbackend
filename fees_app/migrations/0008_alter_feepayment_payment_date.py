# Generated by Django 4.2.6 on 2024-01-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees_app', '0007_remove_feepayment_date_reg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feepayment',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
