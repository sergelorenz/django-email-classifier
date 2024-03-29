# Generated by Django 5.0.2 on 2024-02-26 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificationResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_subject', models.CharField(max_length=512)),
                ('email_body', models.CharField(max_length=2048)),
                ('email_class', models.CharField(choices=[('NEWSLETTER', 'Newsletter'), ('REGULAR', 'Regular')], default='REGULAR', max_length=16, null=True)),
            ],
        ),
    ]
