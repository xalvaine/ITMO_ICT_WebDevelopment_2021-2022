# Generated by Django 3.2.8 on 2021-10-28 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0002_race_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='races.race'),
        ),
    ]
