# Generated by Django 5.0 on 2024-02-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0018_category_productinfo_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name_text",
            field=models.CharField(max_length=75, verbose_name="Category Name"),
        ),
    ]
