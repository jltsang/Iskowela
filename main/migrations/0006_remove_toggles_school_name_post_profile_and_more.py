# Generated by Django 4.1.7 on 2023-03-04 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_banner'),
        ('main', '0005_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toggles',
            name='school_name',
        ),
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='toggles',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
