# Generated by Django 3.2.5 on 2021-07-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='texto_da_home',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
