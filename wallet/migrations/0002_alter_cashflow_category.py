# Generated by Django 4.2.11 on 2024-03-07 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='category',
            field=models.ManyToManyField(blank=True, to='wallet.category'),
        ),
    ]
