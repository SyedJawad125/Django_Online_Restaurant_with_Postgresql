# Generated by Django 5.0.3 on 2024-06-10 15:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurent', '0016_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, help_text='Amount paid', max_digits=10)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Mobile Payment', 'Mobile Payment')], default='Cash', max_length=20)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('card_number', models.CharField(blank=True, help_text='Credit/Debit card number if applicable', max_length=16, null=True)),
                ('card_holder_name', models.CharField(blank=True, help_text='Name of the cardholder if applicable', max_length=100, null=True)),
                ('is_successful', models.BooleanField(default=True, help_text='Status of the payment')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_created_by', to=settings.AUTH_USER_MODEL)),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurent.order')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]