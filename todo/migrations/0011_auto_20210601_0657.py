# Generated by Django 3.1.7 on 2021-06-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_auto_20210601_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'Completed'), ('P', 'Pending')], default=0, max_length=2),
        ),
    ]
