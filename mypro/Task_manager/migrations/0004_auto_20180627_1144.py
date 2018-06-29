# Generated by Django 2.0.6 on 2018-06-27 11:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task_manager', '0003_auto_20180626_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskentry',
            name='id',
        ),
        migrations.AlterField(
            model_name='taskentry',
            name='Task_id',
            field=models.CharField(error_messages={'incomplete': 'Enter a country calling code and a phone number.'}, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taskentry',
            name='Task_priority',
            field=models.PositiveIntegerField(default=1, error_messages={'incomplete': 'Enter a country calling code and a phone number.'}, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
