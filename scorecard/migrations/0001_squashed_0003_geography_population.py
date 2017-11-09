# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-28 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [(b'scorecard', '0001_initial'), (b'scorecard', '0002_geography_development_category'), (b'scorecard', '0003_geography_population')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_level', models.CharField(max_length=15)),
                ('geo_code', models.CharField(max_length=10)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('long_name', models.CharField(db_index=True, max_length=100, null=True)),
                ('square_kms', models.FloatField(null=True)),
                ('parent_level', models.CharField(max_length=15, null=True)),
                ('parent_code', models.CharField(max_length=10, null=True)),
                ('province_name', models.CharField(max_length=100)),
                ('province_code', models.CharField(max_length=5)),
                ('category', models.CharField(max_length=2)),
                ('miif_category', models.TextField(null=True)),
                ('population', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='geography',
            unique_together=set([('geo_level', 'geo_code')]),
        ),
        # migrations.RunSQL(
        #     sql='update scorecard_geography s\n                             set population = pop.population\n                             from population_2011 pop\n                             where pop.geo_level = s.geo_level and pop.geo_code = s.geo_code',
        #     reverse_sql='',
        # ),
    ]