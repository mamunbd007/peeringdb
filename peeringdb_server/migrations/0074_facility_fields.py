# Generated by Django 3.2.7 on 2021-09-07 10:42

import django.core.validators
from django.db import migrations, models
import django_inet.models
import django_peeringdb.fields


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0073_manual_ixf_import"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="available_voltage_services",
            field=django_peeringdb.fields.MultipleChoiceField(
                blank=True,
                choices=[
                    ("48 VDC", "48 VDC"),
                    ("120 VAC", "120 VAC"),
                    ("208 VAC", "208 VAC"),
                    ("240 VAC", "240 VAC"),
                    ("480 VAC", "480 VAC"),
                ],
                help_text="The alternating current voltage available to users of the facility either directly from the landlord or delivered by the utility separately.",
                max_length=255,
                null=True,
                verbose_name="Available Voltage Services",
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="diverse_serving_substations",
            field=models.BooleanField(
                blank=True,
                help_text="Two separate and distinct paths to individual substations which should maintain a separated path back to one or more utility generator stations.",
                null=True,
                verbose_name="Diverse Serving Substations",
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="property",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Owner", "Owner"),
                    ("Lessee", "Lessee"),
                ],
                help_text="A property owner is the individual or entity that has title to the property. A lessee is a user of a property who has a lease, an agreement, with the owner of the property.",
                max_length=27,
                null=True,
                verbose_name="Property",
            ),
        ),
        migrations.AlterField(
            model_name="ixfmemberdata",
            name="asn",
            field=django_inet.models.ASNField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="ASN",
            ),
        ),
        migrations.AlterField(
            model_name="ixlan",
            name="rs_asn",
            field=django_inet.models.ASNField(
                blank=True,
                default=0,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="Route Server ASN",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="asn",
            field=django_inet.models.ASNField(
                unique=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="ASN",
            ),
        ),
        migrations.AlterField(
            model_name="networkfacility",
            name="local_asn",
            field=django_inet.models.ASNField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="Local ASN",
            ),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="asn",
            field=django_inet.models.ASNField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="ASN",
            ),
        ),
        migrations.AlterField(
            model_name="userorgaffiliationrequest",
            name="asn",
            field=django_inet.models.ASNField(
                blank=True,
                help_text="The ASN entered by the user",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                ],
            ),
        ),
    ]