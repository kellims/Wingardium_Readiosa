# Generated by Django 4.2.2 on 2023-07-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_author_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.CharField(max_length=4000),
        ),
    ]
