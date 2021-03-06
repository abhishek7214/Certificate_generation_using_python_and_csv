# Generated by Django 4.0.3 on 2022-03-20 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=300)),
                ('certificate_type', models.CharField(max_length=300)),
                ('csv_file', models.FileField(upload_to='csv/')),
                ('template', models.FileField(upload_to='certificate_template/')),
                ('start_date', models.DateField()),
                ('name_column', models.CharField(blank=True, max_length=100, null=True)),
                ('email_column', models.CharField(blank=True, max_length=250, null=True)),
                ('org_column', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
