# Generated by Django 2.2.14 on 2020-07-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peeringdb_server', '0050_auto_20200730_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ixfmemberdata',
            name='is_rs_peer',
            field=models.BooleanField(blank=True, default=None, help_text='RS Peer', null=True),
        ),
    ]
