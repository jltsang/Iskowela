# Generated by Django 4.1.7 on 2023-03-04 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_banner'),
        ('markers', '0005_alter_event_markers_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_markers',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='event_suggestions',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='place_markers',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='place_suggestions',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='event_markers',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event_suggestions',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='place_markers',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='place_suggestions',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
