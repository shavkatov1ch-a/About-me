# Generated by Django 5.0.4 on 2024-04-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='img',
            field=models.ImageField(null=True, upload_to='projects'),
        ),
    ]
