# Generated by Django 2.0.13 on 2020-03-31 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20200323_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nation',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student'),
        ),
    ]
