# Generated by Django 4.1.7 on 2023-03-05 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0007_alter_profile_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkerMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateField(blank=True, max_length=50, null=True)),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='InfoMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateField(blank=True, max_length=50, null=True)),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='HomeMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateField(blank=True, max_length=50, null=True)),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ChatbotMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateField(blank=True, max_length=50, null=True)),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
