# Generated by Django 3.2.8 on 2021-11-12 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20211112_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.agent'),
        ),
    ]
