# Generated by Django 5.0.2 on 2024-11-27 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Movie name', max_length=300)),
                ('year', models.IntegerField(default=1900)),
                ('cert', models.CharField(default='Movie Certificates', max_length=10)),
                ('runtime', models.IntegerField(default=0)),
                ('genre', models.CharField(default='Movie genres', max_length=300)),
                ('imdb', models.FloatField(default=0.0)),
                ('overview', models.CharField(default='Movie Overview', max_length=1000)),
                ('meta', models.IntegerField()),
                ('director', models.CharField(default='Ex. Al Pacino', max_length=100)),
                ('stara', models.CharField(default='ex. Robert Pattinson', max_length=300)),
                ('starb', models.CharField(default='ex. Robert Downey Jr.', max_length=300)),
                ('starc', models.CharField(default='ex. Robert de Niro', max_length=300)),
                ('stard', models.CharField(default='ex. Robert Cruz', max_length=300)),
                ('votes', models.IntegerField(default=0)),
                ('gross', models.IntegerField(default=0)),
            ],
        ),
    ]
