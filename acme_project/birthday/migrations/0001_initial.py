# Generated by Django 5.1.5 on 2025-01-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, help_text='Необязательное поле', max_length=20, verbose_name='Фамилия')),
                ('date', models.DateField(verbose_name='Дата рождения')),
            ],
        ),
    ]
