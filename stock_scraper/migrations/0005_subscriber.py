# Generated by Django 5.0.7 on 2024-08-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_scraper', '0004_delete_email_stock_change'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
