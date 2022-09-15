# Generated by Django 4.0 on 2022-08-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_gender_profile_join_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='Specialization',
            field=models.CharField(choices=[('عظام', 'عظام'), ('انف واذن وحنجرة', 'انف واذن وحنجرة'), ('نساءوتوليد', 'نساءوتوليد'), ('قلب واوعية دموية', 'قلب واوعية دموية'), ('جلدية', 'جلدية'), ('اطفال حديثي الولادة', 'اطفال حديثي الولادة'), ('امراض دم', 'امراض دم'), ('نفسي', 'نفسي'), ('اورام', 'اورام'), ('باطنه', 'باطنه'), ('تخسيس وتغذية', 'تخسيس وتغذية'), ('جراحة اطفال', 'جراحة اطفال'), ('جراحة اورام', 'جراحة اورام'), ('جراحة اوعية دموية', 'جراحة اوعية دموية'), ('اسنان', 'اسنان'), ('جراحة تجميل', 'جراحة تجميل'), ('جراحه سمنة ومناظير', 'جراحه سمنة ومناظير'), ('مخ واعصاب', 'مخ واعصاب')], default='عظام', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='join_data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]