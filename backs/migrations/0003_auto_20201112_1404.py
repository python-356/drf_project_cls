# Generated by Django 2.2.16 on 2020-11-12 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backs', '0002_auto_20201112_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classschedule',
            name='name',
        ),
        migrations.AddField(
            model_name='classschedule',
            name='cls',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backs.Classroom', verbose_name='班级'),
        ),
    ]
