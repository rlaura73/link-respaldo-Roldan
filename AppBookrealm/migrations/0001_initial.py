# Generated by Django 4.2.5 on 2023-10-12 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('editorial', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('precio', models.CharField(max_length=10)),
                ('oferta', models.CharField(max_length=5)),
            ],
        ),
    ]
