# Generated by Django 3.1.4 on 2022-01-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20220101_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='max_sellable_tickets',
        ),
        migrations.AddField(
            model_name='ticket',
            name='max_sellable_tickets',
            field=models.IntegerField(null=True),
        ),
    ]