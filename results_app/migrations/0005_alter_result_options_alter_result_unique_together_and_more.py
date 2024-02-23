# Generated by Django 4.2.6 on 2024-02-17 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_academicsession_academicterm_siteconfig_studentclass_and_more'),
        ('school_app', '0001_initial'),
        ('results_app', '0004_alter_result_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='result',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('student', 'session', 'term', 'current_class')},
        ),
        migrations.CreateModel(
            name='SubjectResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_score', models.IntegerField(default=0)),
                ('exam_score', models.IntegerField(default=0)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_results', to='results_app.result')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.subject')),
            ],
        ),
        migrations.RemoveField(
            model_name='result',
            name='exam_score',
        ),
        migrations.RemoveField(
            model_name='result',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='result',
            name='test_score',
        ),
    ]
