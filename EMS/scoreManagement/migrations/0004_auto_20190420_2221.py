# Generated by Django 2.1.7 on 2019-04-20 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreManagement', '0003_auto_20190420_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majorcourses',
            name='mno',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backstage.MajorPlan'),
        ),
    ]
