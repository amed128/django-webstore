# Generated by Django 3.2.6 on 2021-10-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eboutique', '0010_auto_20211028_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comment',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
