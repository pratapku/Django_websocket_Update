# Generated by Django 3.2.12 on 2022-05-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen_apps', '0002_auto_20220510_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='change_variable',
            field=models.TextField(),
        ),
    ]