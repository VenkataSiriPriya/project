# Generated by Django 3.2.8 on 2021-12-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0003_rename_emailid_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.CharField(max_length=15, null=True),
        ),
    ]