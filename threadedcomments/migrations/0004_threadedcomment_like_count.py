# Generated by Django 3.2.4 on 2023-09-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threadedcomments', '0003_threadedcomment_newest_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='threadedcomment',
            name='like_count',
            field=models.PositiveIntegerField(default=0, verbose_name='like_count'),
        ),
    ]
