# Generated by Django 4.1.1 on 2022-09-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ad_id_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
