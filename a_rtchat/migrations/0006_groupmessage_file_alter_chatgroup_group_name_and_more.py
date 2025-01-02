# Generated by Django 5.1.4 on 2025-01-01 23:35

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_rtchat", "0005_alter_chatgroup_group_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="groupmessage",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="files/"),
        ),
        migrations.AlterField(
            model_name="chatgroup",
            name="group_name",
            field=models.CharField(
                default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="body",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]