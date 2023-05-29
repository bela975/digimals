# Generated by Django 4.2.1 on 2023-05-29 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0019_remove_alergy_pet_alergy_user_alter_pet_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alergy',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
