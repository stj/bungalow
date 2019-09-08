# Generated by Django 2.2.5 on 2019-09-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_unit', models.CharField(max_length=4, verbose_name='area unit')),
                ('bathrooms', models.FloatField(blank=True, null=True, verbose_name='bathrooms')),
                ('bedrooms', models.PositiveSmallIntegerField(verbose_name='bedrooms')),
                ('home_size', models.PositiveIntegerField(blank=True, null=True, verbose_name='home size')),
                ('home_type', models.CharField(choices=[('Apartment', 'Apartment'), ('Condominium', 'Condominium'), ('Duplex', 'Duplex'), ('Miscellaneous', 'Miscellaneous'), ('MultiFamily2To4', 'MultiFamily2To4'), ('SingleFamily', 'SingleFamily'), ('VacantResidentialLand', 'VacantResidentialLand')], max_length=25, verbose_name='home type')),
                ('last_sold_date', models.DateField(blank=True, null=True, verbose_name='last_sold_date')),
                ('last_sold_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='last_sold_price')),
                ('link', models.CharField(max_length=512, verbose_name='link')),
                ('price', models.CharField(max_length=10, verbose_name='price')),
                ('property_size', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='property size')),
                ('rent_price', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='rent price')),
                ('rentzestimate_amount', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='rent estimate amount')),
                ('rentzestimate_last_updated', models.DateField(blank=True, null=True, verbose_name='rent estimate last updated')),
                ('tax_value', models.FloatField(verbose_name='tax value')),
                ('tax_year', models.PositiveSmallIntegerField(verbose_name='tax year')),
                ('year_built', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='year built')),
                ('zestimate_amount', models.PositiveIntegerField(blank=True, null=True, verbose_name='estimate amount')),
                ('zestimate_last_updated', models.DateField(verbose_name='rent estimate last updated')),
                ('zillow_id', models.PositiveIntegerField(verbose_name='zillow id')),
                ('address', models.CharField(max_length=1024, verbose_name='address')),
                ('city', models.CharField(max_length=1024, verbose_name='city')),
                ('state', models.CharField(max_length=512, verbose_name='state')),
                ('zipcode', models.CharField(max_length=12, verbose_name='ZIP / Postal code')),
            ],
        ),
    ]
