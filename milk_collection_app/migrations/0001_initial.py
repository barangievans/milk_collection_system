# Generated by Django 4.2.19 on 2025-03-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_center_number', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
