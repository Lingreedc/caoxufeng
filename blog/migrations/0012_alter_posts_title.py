# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-31 07:01
from __future__ import unicode_literals

import re

from django.db import migrations
from django.core.exceptions import ObjectDoesNotExist


def alter_title(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')

    try:
        blog_tutorial = Category.objects.get(slug='django-blog-tutorial')
        auth_example = Category.objects.get(slug='django-auth-example')

        blog_tutorial_posts = blog_tutorial.post_set.all()
        auth_example_posts = auth_example.post_set.all()

        for post in blog_tutorial_posts:
            post.title = re.sub(r'Django\s博客教程：|\d{1,2}\s-\s', '', post.title)
            post.save()

        for post in auth_example_posts:
            post.title = re.sub(r'Django\s用户认证系统：\s*', '', post.title)
            post.save()
    except ObjectDoesNotExist:
        pass


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0011_alter_posts_category'),
    ]

    operations = [
        migrations.RunPython(alter_title, migrations.RunPython.noop)
    ]
