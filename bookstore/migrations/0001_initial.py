# Generated by Django 4.0.3 on 2022-11-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=100)),
                ('book_title', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
            ],
        ),
    ]
