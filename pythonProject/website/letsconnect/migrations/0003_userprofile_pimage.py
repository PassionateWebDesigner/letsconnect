# Generated by Django 3.1 on 2020-09-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsconnect', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pimage',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
