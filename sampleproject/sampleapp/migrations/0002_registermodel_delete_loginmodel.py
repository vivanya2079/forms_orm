# Generated by Django 4.2.7 on 2023-11-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('password', models.TimeField()),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='LoginModel',
        ),
    ]