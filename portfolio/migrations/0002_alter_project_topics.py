# Generated by Django 3.2.9 on 2022-01-18 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='topics',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
