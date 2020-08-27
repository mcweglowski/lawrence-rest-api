# Generated by Django 3.1 on 2020-08-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200827_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publishing_year', models.PositiveSmallIntegerField()),
                ('authors', models.ManyToManyField(to='core.Author')),
            ],
        ),
    ]
