# Generated by Django 3.0.4 on 2020-03-16 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0008_auto_20200316_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='visa_period',
            field=models.CharField(max_length=50),
        ),
    ]