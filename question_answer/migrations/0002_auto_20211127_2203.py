# Generated by Django 3.2.9 on 2021-11-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_answer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
