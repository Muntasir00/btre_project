# Generated by Django 2.1.5 on 2019-05-12 20:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_remove_contact_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user_id',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
