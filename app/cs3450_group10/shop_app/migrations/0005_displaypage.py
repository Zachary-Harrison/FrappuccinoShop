# Generated by Django 4.1.1 on 2022-10-20 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_alter_drink_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=15)),
            ],
        ),
    ]