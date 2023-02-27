# Generated by Django 4.1.6 on 2023-02-26 02:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main_page.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(help_text='Заголовок', max_length=80)),
                ('heading_text', models.TextField(help_text='Текст заголовка', max_length=700)),
                ('font_photo', models.ImageField(upload_to=main_page.models.AboutUs.get_file_name)),
                ('video_url', models.URLField(help_text='Введіть тут посилання на відео')),
            ],
        ),
        migrations.CreateModel(
            name='BlockOfInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_number', models.SmallIntegerField()),
                ('block_title', models.TextField(max_length=50)),
                ('block_text', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('position', models.SmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=63, validators=[django.core.validators.RegexValidator(message='E-Mail у форматі: name@company.com', regex='^[a-zA-Z0-9]{1}[a-zA-Z0-9_]+(-{1})?[a-zA-Z0-9_]+@{1}([a-zA-Z0-9]+\\.)+[a-z0-9]{1}([a-z0-9-]*[a-z0-9])?$')])),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True, max_length=250)),
                ('date_of_the_request', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date_of_the_request',),
            },
        ),
        migrations.CreateModel(
            name='CrewMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
                ('member_description', models.CharField(max_length=80)),
                ('member_photo', models.ImageField(upload_to=main_page.models.CrewMember.get_file_name)),
                ('twitter_link', models.URLField(help_text='Введіть адресу акаунта в Twitter')),
                ('facebook_link', models.URLField(help_text='Введіть адресу акаунта у Facebook')),
                ('instagram_link', models.URLField(help_text='Введіть адресу акаунта в Instagram')),
                ('linkedin_link', models.URLField(help_text='Введіть адресу акаунта в LinkedIn')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=200)),
                ('is_visible', models.BooleanField(default=True)),
                ('customer_photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=70, unique=True)),
                ('event_description', models.TextField(max_length=500)),
                ('event_date_and_time', models.DateTimeField(help_text='Введіть дату та час події')),
                ('event_price', models.SmallIntegerField()),
                ('photo', models.ImageField(blank=True, upload_to=main_page.models.Events.get_file_name)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('event_date_and_time',),
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', tinymce.models.HTMLField()),
                ('heading_text', tinymce.models.HTMLField(blank=True)),
                ('twitter', models.CharField(blank=True, max_length=500)),
                ('facebook', models.CharField(blank=True, max_length=500)),
                ('instagram', models.CharField(blank=True, max_length=500)),
                ('skype', models.CharField(blank=True, max_length=500)),
                ('linked_in', models.CharField(blank=True, max_length=500)),
                ('site_owner', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=main_page.models.HeroSection.get_file_name)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='InformationInContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('heading_text', tinymce.models.HTMLField(max_length=250)),
                ('location', tinymce.models.HTMLField()),
                ('open_hours', tinymce.models.HTMLField()),
                ('email', tinymce.models.HTMLField()),
                ('call', tinymce.models.HTMLField()),
                ('phone_on_top_site', models.CharField(max_length=15)),
                ('open_hours_on_top_site', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoToGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=main_page.models.PhotoToGallery.get_file_name)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('is_visible',),
            },
        ),
        migrations.CreateModel(
            name='ThisIsForTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_for_test_1', tinymce.models.HTMLField(max_length=250)),
                ('text_for_test_2', tinymce.models.HTMLField(max_length=250)),
                ('text_for_test_3', tinymce.models.HTMLField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UserReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=63, validators=[django.core.validators.RegexValidator(message='E-Mail у форматі: name@company.com', regex='^[a-zA-Z0-9]{1}[a-zA-Z0-9_]+(-{1})?[a-zA-Z0-9_]+@{1}([a-zA-Z0-9]+\\.)+[a-z0-9]{1}([a-z0-9-]*[a-z0-9])?$')])),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Телефон у форматі xxx xxx xxxx', regex='^(\\d{3}[- .]?){2}\\d{4}$')])),
                ('date_reservation', models.CharField(max_length=10)),
                ('time_reservation', models.CharField(max_length=10)),
                ('persons', models.PositiveSmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=250)),
                ('date_of_the_request', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date_of_the_request',),
            },
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=200)),
                ('position', models.SmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('ingredients', models.CharField(max_length=300)),
                ('is_visible', models.BooleanField(default=True)),
                ('special', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, upload_to=main_page.models.Dishes.get_file_name)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.category')),
            ],
            options={
                'ordering': ('position', 'price'),
                'index_together': {('id', 'slug')},
            },
        ),
    ]