# Generated by Django 2.2.8 on 2019-12-14 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20191214_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='refreshed_at',
            field=models.DateTimeField(null=True),
        ),
    ]