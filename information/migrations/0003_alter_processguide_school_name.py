# Generated by Django 4.1.4 on 2022-12-31 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_rename_process_processguide_process_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processguide',
            name='school_name',
            field=models.TextField(default='Roosevelt College Marikina'),
        ),
    ]
