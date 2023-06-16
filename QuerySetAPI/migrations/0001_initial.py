# Generated by Django 4.2.1 on 2023-05-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('roll', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField(verbose_name=['%d-%m-%Y'])),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('marks', models.IntegerField(blank=True, null=True)),
                ('pass_date', models.DateField(verbose_name=['%d-%m-%Y'])),
            ],
        ),
    ]
