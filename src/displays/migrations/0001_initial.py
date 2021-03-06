# Generated by Django 2.2 on 2019-05-02 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topics', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDisplayModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_model', models.CharField(max_length=64, unique=True)),
                ('max_lines', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=16)),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='topics.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.PositiveSmallIntegerField(unique=True)),
                ('friendly_name', models.CharField(blank=True, max_length=64, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='accounts.Customer')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model', to='displays.MyDisplayModel')),
            ],
        ),
    ]
