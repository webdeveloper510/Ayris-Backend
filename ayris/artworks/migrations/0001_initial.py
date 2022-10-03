# Generated by Django 3.2.8 on 2022-10-03 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('counter', models.PositiveIntegerField(default=0)),
                ('is_allow', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Matter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('counter', models.PositiveIntegerField(default=0)),
                ('is_allow', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('counter', models.PositiveIntegerField(default=0)),
                ('is_allow', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArtWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('counter', models.PositiveIntegerField(default=0)),
                ('is_allow', models.BooleanField(default=False)),
                ('period', models.CharField(blank=True, max_length=30)),
                ('colors', models.ManyToManyField(blank=True, to='artworks.Color')),
                ('matters', models.ManyToManyField(blank=True, to='artworks.Matter')),
                ('mediums', models.ManyToManyField(blank=True, to='artworks.Medium')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]