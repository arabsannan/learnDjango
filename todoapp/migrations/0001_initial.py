# Generated by Django 3.1.2 on 2020-11-01 20:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('due_date', models.DateField(null=True)),
                ('completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('assignees', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
