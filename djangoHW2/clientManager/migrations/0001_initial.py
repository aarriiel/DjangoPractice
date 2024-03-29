# Generated by Django 2.2.7 on 2019-11-22 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sexual', models.CharField(max_length=20)),
                ('birthday', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=10)),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
                ('create_time', models.DateTimeField(editable=False)),
                ('update_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=40)),
                ('create_time', models.DateTimeField(editable=False)),
            ],
        ),
    ]
