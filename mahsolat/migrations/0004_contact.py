# Generated by Django 4.2.4 on 2023-11-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahsolat', '0003_alter_kala_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('onvan', models.CharField(max_length=150)),
                ('text', models.CharField(max_length=500)),
                ('number', models.CharField(default='09130000000', max_length=11)),
            ],
        ),
    ]