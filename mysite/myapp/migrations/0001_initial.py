# Generated by Django 4.1.5 on 2023-02-16 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileupload', models.FileField(blank=True, null=True, upload_to='fileupload/')),
            ],
        ),
    ]