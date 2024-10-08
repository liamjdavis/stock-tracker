# Generated by Django 5.0.4 on 2024-07-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_symbol', models.CharField(max_length=10, unique=True)),
                ('company_name', models.CharField(max_length=255)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('previous_close_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('high_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('low_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('volume', models.BigIntegerField(blank=True, null=True)),
                ('market_cap', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('pe_ratio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
