# Generated by Django 3.1.2 on 2020-10-21 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201021_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_answer',
            name='exam_id',
            field=models.IntegerField(default=''),
        ),
    ]
