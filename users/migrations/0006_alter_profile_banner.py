# Generated by Django 4.1.5 on 2023-01-05 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='banner',
            field=models.ImageField(default='school_banner.jpg', upload_to='media'),
        ),
    ]