# Generated by Django 4.0 on 2021-12-10 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='penis_length',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
