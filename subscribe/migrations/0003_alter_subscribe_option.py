# Generated by Django 5.0.6 on 2024-07-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_subscribe_option_alter_subscribe_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='option',
            field=models.CharField(choices=[('w', 'Weekly'), ('m', 'Monthly')], default='m', max_length=2),
        ),
    ]
