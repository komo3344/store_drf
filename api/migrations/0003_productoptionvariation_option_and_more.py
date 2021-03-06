# Generated by Django 4.0.4 on 2022-04-24 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_options_alter_productoption_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoptionvariation',
            name='option',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='api.productoption'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productoption',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='api.product'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='api.product'),
        ),
    ]
