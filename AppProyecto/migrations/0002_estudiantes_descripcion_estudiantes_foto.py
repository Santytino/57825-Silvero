# Generated by Django 4.2 on 2024-09-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/'),
        ),
    ]
