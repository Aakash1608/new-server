# Generated by Django 5.0 on 2023-12-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_collector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_path',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]