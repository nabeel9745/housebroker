# Generated by Django 4.0.4 on 2022-10-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listed_property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop_name', models.CharField(max_length=100)),
                ('prop_address', models.CharField(max_length=100)),
                ('prop_landmark', models.CharField(max_length=100)),
                ('prop_pincode', models.BigIntegerField()),
            ],
        ),
    ]
