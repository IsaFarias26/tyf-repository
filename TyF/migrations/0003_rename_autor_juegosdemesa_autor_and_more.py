# Generated by Django 5.0.6 on 2024-06-25 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TyF', '0002_juegosdemesa_videojuegos_delete_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='juegosdemesa',
            old_name='Autor',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='juegosdemesa',
            old_name='Descripción',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='juegosdemesa',
            old_name='Titulo',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='videojuegos',
            old_name='Autor',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='videojuegos',
            old_name='Descripción',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='videojuegos',
            old_name='Titulo',
            new_name='titulo',
        ),
    ]
