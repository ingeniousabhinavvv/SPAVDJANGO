# Generated by Django 4.0.4 on 2022-05-19 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticeboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noticeTitle', models.CharField(max_length=100)),
                ('upload', models.FileField(upload_to='uploads/% Y/% m/% d/')),
            ],
        ),
    ]
