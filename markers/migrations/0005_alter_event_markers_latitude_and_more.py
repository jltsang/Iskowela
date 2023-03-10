# Generated by Django 4.1.7 on 2023-02-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0004_alter_event_markers_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_markers',
            name='latitude',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='event_markers',
            name='longitude',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='event_suggestions',
            name='latitude',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='event_suggestions',
            name='longitude',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='place_markers',
            name='latitude',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='place_markers',
            name='longitude',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='place_suggestions',
            name='latitude',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='place_suggestions',
            name='longitude',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=25),
        ),
    ]
