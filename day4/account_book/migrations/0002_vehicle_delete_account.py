# Generated by Django 4.0.4 on 2022-05-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=20)),
                ('vehicle_model', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]