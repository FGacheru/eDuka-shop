# Generated by Django 3.1.6 on 2021-02-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eDuka', '0002_remove_product_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
