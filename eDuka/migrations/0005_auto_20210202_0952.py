# Generated by Django 3.1.6 on 2021-02-02 09:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eDuka', '0004_auto_20210202_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
