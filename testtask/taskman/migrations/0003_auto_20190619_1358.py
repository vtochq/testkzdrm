# Generated by Django 2.2.2 on 2019-06-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskman', '0002_auto_20190619_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
