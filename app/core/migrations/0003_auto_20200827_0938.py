# Generated by Django 3.1 on 2020-08-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200827_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='display_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]