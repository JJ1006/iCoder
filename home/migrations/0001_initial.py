# Generated by Django 5.1.3 on 2024-11-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('content', models.TextField()),
            ],
        ),
    ]
