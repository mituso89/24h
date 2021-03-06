# Generated by Django 2.1.7 on 2019-02-24 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=256, unique=True)),
                ('title', models.CharField(max_length=256, unique=True)),
                ('type', models.CharField(max_length=50)),
                ('image_ratio', models.FloatField(default=1.618)),
                ('width_ratio', models.IntegerField(default=100)),
                ('single', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'categories',
                'ordering': ['-id'],
                'permissions': (('list_category', 'Can list category'), ('retrieve_category', 'Can retrieve category'), ('delete_list_category', 'Can delete list category'), ('change_translation_category', 'Can change translation category')),
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=5)),
                ('title', models.CharField(blank=True, max_length=256)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_translations', to='category.Category')),
            ],
            options={
                'db_table': 'category_translations',
                'ordering': ['-id'],
                'default_permissions': (),
            },
        ),
    ]
