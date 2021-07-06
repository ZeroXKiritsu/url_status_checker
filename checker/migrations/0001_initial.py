# Generated by Django 3.2.3 on 2021-07-06 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='URL')),
                ('status', models.IntegerField(null=True, verbose_name='status')),
                ('check_interval', models.PositiveIntegerField(default=5, verbose_name='check interval')),
                ('is_paused', models.BooleanField(default=False, verbose_name='paused')),
            ],
        ),
    ]