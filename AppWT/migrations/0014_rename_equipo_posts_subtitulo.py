# Generated by Django 4.1.1 on 2022-10-03 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppWT', '0013_alter_posts_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='equipo',
            new_name='subtitulo',
        ),
    ]
