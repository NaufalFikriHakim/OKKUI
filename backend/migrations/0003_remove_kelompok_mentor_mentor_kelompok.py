# Generated by Django 5.0.2 on 2024-03-03 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_bidang_bph_divisi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kelompok',
            name='mentor',
        ),
        migrations.AddField(
            model_name='mentor',
            name='kelompok',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.kelompok'),
            preserve_default=False,
        ),
    ]
