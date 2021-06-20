# Generated by Django 3.2.4 on 2021-06-19 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agents.agent'),
        ),
        migrations.AlterField(
            model_name='client',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
