# Generated by Django 3.1.2 on 2021-02-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0002_vipguest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='introduction',
            field=models.TextField(verbose_name='个人介绍'),
        ),
        migrations.AlterField(
            model_name='vipguest',
            name='introduction',
            field=models.TextField(verbose_name='个人介绍'),
        ),
    ]