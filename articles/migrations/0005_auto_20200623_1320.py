# Generated by Django 3.0.7 on 2020-06-23 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comment',
            field=models.TextField(default='No Comment'),
        ),
    ]
