# Generated by Django 5.0.2 on 2024-02-24 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.ImageField(upload_to='favicon/')),
            ],
        ),
    ]