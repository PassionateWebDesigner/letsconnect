# Generated by Django 3.1 on 2020-09-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsconnect', '0003_userprofile_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
