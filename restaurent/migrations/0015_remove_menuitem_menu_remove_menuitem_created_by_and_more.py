# Generated by Django 5.0.3 on 2024-06-10 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurent', '0014_remove_payment_created_by_remove_payment_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='menuitem',
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='order',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='order',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='review',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='review',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='review',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
        migrations.DeleteModel(
            name='Promotion',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]