# Generated by Django 3.2.8 on 2021-10-23 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.CharField(default='Text', max_length=1000),
            preserve_default=False,
        ),
    ]
