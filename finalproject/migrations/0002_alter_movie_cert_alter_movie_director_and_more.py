# Generated by Django 5.0.2 on 2024-11-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cert',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='stara',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='starb',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='starc',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='stard',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
