# Generated by Django 3.0.3 on 2020-02-27 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=40)),
                ('logo', models.ImageField(default='default.jpg', upload_to='logo_pics')),
                ('contact_details', models.TextField()),
                ('mapbox_key', models.CharField(max_length=100)),
                ('new_game_dataset_link', models.CharField(max_length=80)),
                ('event_markers_dataset_link', models.CharField(max_length=80)),
                ('place_markers_dataset_link', models.CharField(max_length=80)),
                ('live_chat_link', models.CharField(max_length=50)),
                ('chatbot_tree_link', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
