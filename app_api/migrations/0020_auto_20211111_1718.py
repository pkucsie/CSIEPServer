# Generated by Django 3.1.2 on 2021-11-11 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0019_wxadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wxadmin',
            name='ADMIN_TYPE',
            field=models.IntegerField(default=1, verbose_name='类型'),
        ),
    ]
