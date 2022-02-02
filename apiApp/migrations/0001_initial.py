# Generated by Django 4.0.1 on 2022-01-31 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birthDay', models.CharField(blank=True, max_length=255)),
                ('spouse', models.CharField(blank=True, max_length=255)),
                ('voice', models.CharField(blank=True, max_length=255)),
                ('img', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Squishies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
