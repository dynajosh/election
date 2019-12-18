# Generated by Django 2.1.7 on 2019-06-24 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='category',
            field=models.CharField(choices=[('President', 'President'), ('Vice President', 'Vice President'), ('General Secretary', 'General Secretary'), ('Assistant General Secretary', 'Assistant General Secretary'), ('Null', 'Null')], default='Null', max_length=120),
        ),
    ]
