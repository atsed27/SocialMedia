# Generated by Django 5.0.4 on 2024-04-08 18:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_postcomment_post_alter_postcomment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]