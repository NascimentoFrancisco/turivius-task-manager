# Generated by Django 5.1 on 2024-08-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_task_created_at_alter_task_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
