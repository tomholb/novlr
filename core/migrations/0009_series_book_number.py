# Generated by Django 3.1.2 on 2021-01-16 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210111_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='book_number',
            field=models.IntegerField(default=1),
        ),
    ]