# Generated by Django 4.1.7 on 2023-05-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_bot',
            field=models.BooleanField(default=False),
        ),
    ]