# Generated by Django 4.1.1 on 2022-10-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWT', '0012_alter_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail/'),
        ),
    ]
