# Generated by Django 2.2.7 on 2019-12-26 22:55

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('plagiarismchecking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plagiarismchecksave',
            name='input',
            field=jsonfield.fields.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='plagiarismchecksave',
            name='output',
            field=jsonfield.fields.JSONField(default=''),
        ),
    ]
