# Generated by Django 4.1.3 on 2022-11-26 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comida',
            name='imagen',
            field=models.ImageField(default='amor', upload_to='imagenes'),
            preserve_default=False,
        ),
    ]
