# Generated by Django 4.2.7 on 2023-11-19 03:04

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lesson', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('status', models.CharField(choices=[('admin', 'ADMIN'), ('assist', 'ASSIST'), ('ustoz', 'USTOZ'), ('pupil', 'PUPIL')], default='pupil', max_length=15, verbose_name='Foydalanuvchi turi')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefon raqam ')),
                ('image', models.ImageField(blank=True, null=True, upload_to=user.models.image_path, verbose_name='Foydalanuvchi rasmi ')),
                ('subject', models.ManyToManyField(related_name='teachers', to='lesson.lesson')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ism')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Familiya')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefon raqam ')),
                ('phone_number2', models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefon raqam ')),
                ('is_active', models.BooleanField(default=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('pupil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pupils', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pupils', to='lesson.lesson')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pupils', to='user.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefon raqam ')),
                ('image', models.ImageField(blank=True, null=True, upload_to=user.models.image_path, verbose_name='Foydalanuvchi rasmi ')),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefon raqam ')),
                ('image', models.ImageField(blank=True, null=True, upload_to=user.models.image_path, verbose_name='Foydalanuvchi rasmi ')),
                ('administrator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='administrator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
