# Generated by Django 4.2.4 on 2023-11-26 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='ユーザー名')),
                ('department', models.CharField(blank=True, max_length=100, null=True, verbose_name='部署')),
                ('phone_number', models.IntegerField(blank=True, null=True, verbose_name='携帯番号')),
                ('gender', models.CharField(blank=True, choices=[(None, '--'), ('m', '男性'), ('f', '女性')], default=None, max_length=1, null=True, verbose_name='性別')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生年月日')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
