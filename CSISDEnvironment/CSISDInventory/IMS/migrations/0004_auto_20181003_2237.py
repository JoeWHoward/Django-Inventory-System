# Generated by Django 2.1.1 on 2018-10-03 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0003_auto_20181003_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
