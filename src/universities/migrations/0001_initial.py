# Generated by Django 3.0.4 on 2020-03-14 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nation', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=200)),
                ('available_number', models.IntegerField()),
                ('language_condition', models.CharField(max_length=200)),
                ('remarks', models.TextField()),
                ('keyword', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('department', models.CharField(max_length=30)),
                ('major', models.CharField(max_length=20)),
                ('ex_period', models.CharField(max_length=30)),
                ('visa_type', models.CharField(max_length=20)),
                ('visa_period', models.CharField(max_length=20)),
                ('visa_process', models.TextField()),
                ('dorm_name', models.CharField(max_length=20)),
                ('dorm_location', models.CharField(max_length=10)),
                ('dorm_cost', models.CharField(max_length=20)),
                ('dorm_satisfaction', models.CharField(max_length=10)),
                ('dorm_comment', models.TextField()),
                ('lecture_comment', models.TextField()),
                ('lecture_grading', models.TextField()),
                ('culture_activity', models.TextField()),
                ('final_satisfaction', models.IntegerField()),
                ('final_comment', models.TextField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities.University')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities.University')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'university')},
            },
        ),
    ]
