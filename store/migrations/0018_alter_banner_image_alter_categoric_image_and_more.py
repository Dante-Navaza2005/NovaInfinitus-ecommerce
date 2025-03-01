# Generated by Django 4.2.16 on 2025-01-18 12:36

from django.db import migrations, models
import store.utility


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_banner_image_alter_categoric_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to=store.utility.dynamic_upload_path),
        ),
        migrations.AlterField(
            model_name='categoric',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=store.utility.dynamic_upload_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=store.utility.dynamic_upload_path),
        ),
    ]
