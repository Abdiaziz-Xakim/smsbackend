# Generated by Django 4.2.6 on 2024-02-16 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_academicsession_academicterm_siteconfig_studentclass_and_more'),
        ('results_app', '0003_alter_result_options_remove_result_subjects_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.subject'),
        ),
    ]