# Generated by Django 3.1.4 on 2020-12-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreditCardNumber', models.CharField(max_length=19, unique=True)),
                ('CardHolder', models.CharField(max_length=40)),
                ('ExpirationDate', models.DateField()),
                ('SecurityCode', models.IntegerField(max_length=3)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
