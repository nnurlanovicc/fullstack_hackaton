# Generated by Django 4.2.5 on 2023-09-18 06:01

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('vacancy', models.CharField(max_length=30)),
                ('experience', models.PositiveIntegerField(max_length=2)),
                ('salary', models.PositiveIntegerField(max_length=6)),
                ('description', models.TextField()),
                ('reqruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
