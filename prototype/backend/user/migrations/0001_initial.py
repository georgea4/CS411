# Generated by Django 4.1.3 on 2022-12-08 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(default=0, primary_key=True, serialize=False)),
                ('user_num', models.CharField(max_length=320)),
                ('user_database', models.TextField(default="We don't have your location yet. Give it to us please")),
            ],
        ),
    ]
