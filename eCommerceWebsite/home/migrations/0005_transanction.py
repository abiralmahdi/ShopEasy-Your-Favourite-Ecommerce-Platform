# Generated by Django 5.0.4 on 2024-11-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transanction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]