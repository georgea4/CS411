# Generated by Django 4.1.3 on 2022-12-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.CharField(default=0, max_length=320, primary_key=True, serialize=False)),
                ('user_email', models.CharField(max_length=320)),
                ('location', models.TextField(default="We don't have your location yet. Give it to us please")),
                ('weather', models.JSONField()),
                ('news', models.JSONField()),
                ('color', models.TextField(default="We can't update your color without you updating your color. Give it to us please")),
            ],
        ),
    ]
