# Generated by Django 4.0.10 on 2024-04-08 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='rank',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
