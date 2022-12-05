# Generated by Django 3.2 on 2022-09-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='company/', verbose_name='Logo')),
                ('subtitle', models.CharField(max_length=500, verbose_name='Subtitle')),
                ('fb_link', models.URLField(blank=True, null=True)),
                ('tw_link', models.URLField(blank=True, null=True)),
                ('ins_link', models.URLField(blank=True, null=True)),
                ('address', models.TextField(max_length=200, verbose_name='Address')),
                ('phone_nomber', models.TextField(max_length=200, verbose_name='Phone')),
                ('email', models.TextField(max_length=200, verbose_name='Courriel')),
                ('call_us', models.TextField(max_length=25, verbose_name='Call us')),
                ('email_us', models.EmailField(max_length=254, verbose_name='Email us')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companys',
            },
        ),
    ]
