# Generated by Django 3.0.5 on 2023-03-03 07:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20221123_1246'),
        ('domain', '0003_finance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electronics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('link', models.URLField()),
                ('image', models.ImageField(blank=True, upload_to='electronics', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electronics', to='profiles.Profile')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
