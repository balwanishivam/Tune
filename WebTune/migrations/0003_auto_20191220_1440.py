# Generated by Django 3.0 on 2019-12-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebTune', '0002_auto_20191220_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(blank=True, upload_to='static/logos/'),
        ),
    ]