# Generated by Django 3.1.7 on 2021-05-31 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20210531_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.IntegerField(choices=[(1, 'Completed'), (0, 'Pending')], default=0),
        ),
    ]