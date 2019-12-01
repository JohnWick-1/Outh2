# Generated by Django 2.2.6 on 2019-11-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('marks', models.IntegerField()),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]