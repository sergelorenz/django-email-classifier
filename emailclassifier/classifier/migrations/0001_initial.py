# Generated by Django 5.0.2 on 2024-02-26 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emailuploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification_method', models.CharField(choices=[('LOGIC', 'Logic'), ('ML', 'ML')], default='LOGIC', max_length=16, null=True)),
                ('ml_classifier', models.CharField(choices=[('NONE', 'None'), ('SKLEARN', 'Sklearn'), ('KERAS', 'Keras')], default='NONE', max_length=16, null=True)),
                ('classification_status', models.CharField(choices=[('not_done', 'Not Done'), ('ongoing', 'Ongoing'), ('completed', 'Completed')], default='not_done', max_length=16, null=True)),
                ('email_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emailuploader.emailfile')),
            ],
        ),
    ]
