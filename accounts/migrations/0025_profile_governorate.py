# Generated by Django 4.0 on 2022-09-01 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_comment_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='governorate',
            field=models.CharField(choices=[('Mansoura', 'Mansoura'), ('Alexandria', 'Alexandria'), ('Cairo', 'Cairo'), ('Minya', 'Minya'), ('Tanta', 'Tanta'), ('Kafr El Sheikh', 'Kafr El Sheikh'), ('Asyut', 'Asyut'), ('Damietta', 'Damietta'), ('Giza', 'Giza'), ('\tIsmailia', 'Ismailia'), ('Zagazig', 'Zagazig'), ('Hurghada', 'Hurghada')], default='Cairo', max_length=50),
        ),
    ]
