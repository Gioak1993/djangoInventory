# Generated by Django 5.0 on 2023-12-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0014_alter_images_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productinfo",
            name="title_text",
            field=models.CharField(max_length=200, verbose_name="Title"),
        ),
    ]
