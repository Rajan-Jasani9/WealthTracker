# Generated by Django 5.1.3 on 2024-11-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('asset_type', models.CharField(choices=[('STOCK', 'Stock'), ('BOND', 'Bond'), ('REAL_ESTATE', 'Real Estate'), ('CASH', 'Cash'), ('CRYPTO', 'Cryptocurrency'), ('MUTUAL_FUND', 'Mutual Fund'), ('ETF', 'Exchange-Traded Fund'), ('COMMODITY', 'Commodity'), ('PRECIOUS_METAL', 'Precious Metal'), ('ART', 'Art'), ('COLLECTIBLE', 'Collectible'), ('VEHICLE', 'Vehicle'), ('BUSINESS', 'Business'), ('OTHER', 'Other')], default='OTHER', max_length=50)),
                ('asset_status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=50)),
                ('purchase_cost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('purchase_date', models.DateField(null=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
