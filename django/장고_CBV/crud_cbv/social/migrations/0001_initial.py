# Generated by Django 3.2.3 on 2021-05-25 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.TextField(default=1621923448.485503)),
                ('updated_at', models.TextField(blank=True, null=True)),
                ('class_num', models.IntegerField()),
                ('teacher', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
