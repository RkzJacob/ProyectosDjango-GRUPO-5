# Generated by Django 3.2.4 on 2021-06-29 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaWeb', '0008_alter_publicacionarte_imagenpublicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacionarte',
            name='Nombre',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='publicacionarte',
            name='correo',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='correo'),
        ),
    ]