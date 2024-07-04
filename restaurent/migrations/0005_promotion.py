# Generated by Django 5.0.3 on 2024-06-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurent', '0004_alter_orderdetail_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('discount_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('active', models.BooleanField(default=True)),
                ('promo_code', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
