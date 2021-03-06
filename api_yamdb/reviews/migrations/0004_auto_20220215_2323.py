# Generated by Django 2.2.16 on 2022-02-15 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220215_2204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')], default='user', max_length=9),
        ),
    ]
