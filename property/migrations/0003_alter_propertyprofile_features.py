# Generated by Django 3.2.17 on 2023-12-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_alter_propertyunit_interior'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyprofile',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='property', to='property.Features'),
        ),
    ]
