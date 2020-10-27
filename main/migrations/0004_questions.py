# Generated by Django 3.1.2 on 2020-10-20 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_user_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=200)),
                ('c1', models.CharField(default='', max_length=200)),
                ('c2', models.CharField(default='', max_length=200)),
                ('c3', models.CharField(default='', max_length=200)),
                ('c4', models.CharField(default='', max_length=200)),
                ('answer', models.CharField(max_length=200)),
                ('marks', models.IntegerField()),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exam')),
            ],
        ),
    ]
