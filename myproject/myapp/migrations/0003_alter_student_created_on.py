# Generated by Django 4.2.4 on 2023-09-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_student_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
