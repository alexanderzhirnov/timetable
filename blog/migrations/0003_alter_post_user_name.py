# Generated by Django 5.0.4 on 2024-04-25 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
