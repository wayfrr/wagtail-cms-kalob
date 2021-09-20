# Generated by Django 3.2.7 on 2021-09-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(help_text='Email address', max_length=100)),
                ('full_name', models.CharField(help_text='First and last name', max_length=100)),
            ],
        ),
    ]
