# Generated by Django 3.2.6 on 2021-08-18 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_author'),
        ('posts', '0006_auto_20210818_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membership.author'),
        ),
    ]
