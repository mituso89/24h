# Generated by Django 2.1.7 on 2019-02-24 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'permissions': (('change_translation_category', 'Can change translation category'),)},
        ),
    ]
