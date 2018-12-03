# Generated by Django 2.1.3 on 2018-12-03 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20181203_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='product',
        ),
        migrations.AlterField(
            model_name='orderproducts',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.Order'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='catalog.Category'),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]