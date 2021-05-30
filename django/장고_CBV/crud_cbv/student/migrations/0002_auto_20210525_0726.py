# Generated by Django 3.2.3 on 2021-05-25 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_alter_classroom_created_at'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='social.classroom'),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.TextField(default=1621927603.603679),
        ),
    ]
