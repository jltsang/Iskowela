# Generated by Django 4.1.7 on 2023-03-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0008_event_suggestions_event_marker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_suggestions',
            name='event_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event_suggestions',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=20, default=0, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='event_suggestions',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=20, default=0, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='event_suggestions',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event_suggestions',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'Offline'), (2, 'Online')], null=True),
        ),
        migrations.AlterField(
            model_name='place_suggestions',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=20, default=0, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='place_suggestions',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=20, default=0, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='place_suggestions',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='place_suggestions',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'Health'), (2, 'Food'), (3, 'Finance'), (4, 'Store'), (5, 'Etc')], null=True),
        ),
    ]
