# Generated by Django 5.0.2 on 2024-02-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('agirlik', models.FloatField()),
                ('kategori', models.CharField(choices=[('sivil', 'Sivil İHA'), ('askeri', 'Askeri İHA'), ('hibrit', 'Hibrit İHA'), ('mini_iha', 'Mini İHA'), ('uzun_menzilli', 'Uzun Menzilli İHA')], max_length=20)),
            ],
        ),
    ]
