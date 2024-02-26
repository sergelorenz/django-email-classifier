# Generated by Django 5.0.2 on 2024-02-26 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='EmailFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(choices=[('.csv', 'csv'), ('.json', 'json'), ('.pickle', 'pickle')], default='.csv', max_length=10, null=True)),
                ('email_file', models.FileField(upload_to='media/uploads/')),
            ],
        ),
    ]
