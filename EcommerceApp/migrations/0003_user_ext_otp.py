# Generated by Django 4.1.1 on 2022-10-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceApp', '0002_user_ext_district_user_ext_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_ext',
            name='otp',
            field=models.ImageField(default='null', upload_to=''),
            preserve_default=False,
        ),
    ]