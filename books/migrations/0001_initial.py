# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 14:02
from __future__ import unicode_literals

import books.managers
import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='User name')),
                ('first_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='Last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=books.models.user_avatar_path, verbose_name='Profile picture')),
                ('facebook_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Facebook email address')),
                ('facebook_avatar', models.URLField(blank=True, null=True, verbose_name='Facebook profile picture')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', books.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
            ],
            options={
                'verbose_name_plural': 'Authors',
                'verbose_name': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('isbn', models.CharField(blank=True, help_text='10 or 13 digits', max_length=13, null=True, unique=True, validators=[books.models.isbn_validator], verbose_name='ISBN')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='books/covers', verbose_name='Cover')),
                ('author', models.ManyToManyField(related_name='author', to='books.Author', verbose_name='Author')),
            ],
            options={
                'verbose_name_plural': 'Books',
                'verbose_name': 'Book',
            },
        ),
    ]
