# Generated by Django 5.0.2 on 2024-02-08 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=100)),
                ('mano', models.IntegerField()),
            ],
        ),
    ]