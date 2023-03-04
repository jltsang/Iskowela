# Generated by Django 4.1.7 on 2023-03-04 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_banner'),
        ('information', '0007_alter_courses_course_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='schoolid',
        ),
        migrations.RemoveField(
            model_name='processguide',
            name='school_name',
        ),
        migrations.RemoveField(
            model_name='scholarships',
            name='schoolid',
        ),
        migrations.AddField(
            model_name='courses',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='processguide',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
