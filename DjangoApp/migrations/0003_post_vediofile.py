# Generated by Django 4.1 on 2022-09-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0002_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vediofile',
            field=models.FileField(default=False, upload_to='vedio/'),
            preserve_default=False,
        ),
    ]
