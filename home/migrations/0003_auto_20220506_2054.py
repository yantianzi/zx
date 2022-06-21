# Generated by Django 3.0.6 on 2022-05-06 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220506_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='effect_optimized',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.EffectOptimized'),
        ),
        migrations.AddField(
            model_name='effect',
            name='backbone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Backbone'),
        ),
        migrations.AddField(
            model_name='effectoptimized',
            name='backbone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.BackboneOptimized'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='effect',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Effect'),
        ),
    ]
