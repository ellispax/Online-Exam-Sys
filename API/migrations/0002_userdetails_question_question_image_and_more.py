# Generated by Django 4.2 on 2023-04-06 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('national_id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='question_images/'),
        ),
        migrations.AlterField(
            model_name='examattempt',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.userdetails'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]