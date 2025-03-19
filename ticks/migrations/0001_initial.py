# Generated by Django 4.2.20 on 2025-03-18 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B')], max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
