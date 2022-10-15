# Generated by Django 4.1.1 on 2022-10-12 09:46

import datetime
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
            name='user_ext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(default=datetime.date.today, null=True)),
                ('image', models.ImageField(upload_to='user/pro_pic')),
                ('gender', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('user_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
