# Generated by Django 3.2.4 on 2021-06-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaWeb', '0006_auto_20210622_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacionarte',
            name='imagenPublicacion',
            field=models.ImageField(blank=True, null=True, upload_to='fotopublicaciones', verbose_name='imagen'),
        ),
    ]
