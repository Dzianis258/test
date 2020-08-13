# Generated by Django 3.1 on 2020-08-12 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200809_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(default='default.png', upload_to='course_images', verbose_name='Изображение профиля'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(verbose_name='Название URL'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Название курса'),
        ),
    ]
