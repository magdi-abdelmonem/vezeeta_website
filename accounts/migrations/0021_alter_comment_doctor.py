# Generated by Django 4.0 on 2022-08-29 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_rename_body_comment_comment_space'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accounts.profile'),
        ),
    ]
