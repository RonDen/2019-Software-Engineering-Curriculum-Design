# Generated by Django 2.1.3 on 2019-05-03 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreManagement', '0005_auto_20190503_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationform',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='scoreManagement.MajorCourses'),
        ),
    ]
