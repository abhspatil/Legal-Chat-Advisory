# Generated by Django 2.0.2 on 2020-05-10 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BasicApp', '0005_querydata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='querydata',
            old_name='desccription',
            new_name='description',
        ),
    ]
