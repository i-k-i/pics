# Generated by Django 2.2.7 on 2019-11-11 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20191111_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='image',
            new_name='image_path',
        ),
    ]
