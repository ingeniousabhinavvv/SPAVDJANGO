# Generated by Django 4.0.4 on 2022-05-19 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0002_noticeboard'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Noticeboard',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
