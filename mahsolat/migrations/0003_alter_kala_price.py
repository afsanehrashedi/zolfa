# Generated by Django 4.2.4 on 2023-11-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahsolat', '0002_rename_titel_kala_name_alter_kala_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kala',
            name='price',
            field=models.TextField(max_length=50),
        ),
    ]