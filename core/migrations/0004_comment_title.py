# Generated by Django 2.0.2 on 2020-01-25 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
