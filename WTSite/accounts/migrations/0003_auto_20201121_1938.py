# Generated by Django 3.1.1 on 2020-11-21 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201121_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='expires_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
