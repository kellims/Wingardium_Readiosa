# Generated by Django 4.2.2 on 2023-07-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=250)),
                ('bio', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
