# Generated by Django 4.1.2 on 2022-11-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(blank=True, default='static/image/n1.jpg', upload_to='static/image'),
        ),
    ]
