# Generated by Django 4.1.2 on 2022-11-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_alter_card_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(blank=True, default='static/image/n1.jpg', upload_to='static/image'),
        ),
    ]
