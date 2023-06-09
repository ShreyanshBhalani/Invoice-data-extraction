# Generated by Django 4.1.5 on 2023-02-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_fileupload_uploadpdf_imageupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=400)),
                ('seller_name', models.CharField(max_length=400)),
                ('buyer_name', models.CharField(max_length=400)),
                ('gst_no', models.CharField(max_length=400)),
                ('fssai_no', models.CharField(max_length=400)),
                ('invoice_date', models.CharField(max_length=400)),
                ('sr_no', models.CharField(max_length=400)),
                ('item_name', models.CharField(max_length=400)),
                ('hsn_code', models.CharField(max_length=400)),
                ('weight', models.CharField(max_length=400)),
                ('rate', models.CharField(max_length=400)),
                ('amount', models.CharField(max_length=400)),
                ('final_amount', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]
