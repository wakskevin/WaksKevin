# Generated by Django 4.2.5 on 2023-10-07 15:55

import datetime
from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaksKevin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', easy_thumbnails.fields.ThumbnailerImageField(upload_to='base/WaksKevin')),
                ('theme_color', models.CharField(default='#EDE9DD', max_length=255)),
                ('profile_picture', models.ImageField(upload_to='base/WaksKevin')),
                ('author', models.CharField(default='Kevin Wakhisi', max_length=100)),
                ('title', models.TextField(default='Software Engineer & Student @ UON')),
                ('description', models.TextField(blank=True)),
                ('birthday', models.DateField(default=datetime.date(2002, 5, 2))),
                ('degree', models.CharField(choices=[('Bachelor', 'Bachelor'), ('Master', 'Master')], default='Bachelor', max_length=50)),
                ('freelance_status', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable'), ('Busy', 'Busy')], default='Available', max_length=100)),
                ('email', models.EmailField(default='wakskevin@outlook.com', max_length=254)),
                ('phone', models.CharField(default='+254 706 965 904', max_length=100)),
                ('address', models.CharField(default='Nairobi, Kenya', max_length=100)),
                ('website', models.URLField(default='https://www.kevinwakhisi.info')),
                ('linkedin', models.URLField(blank=True, default='https://www.linkedin.com/in/WaksKevin/')),
                ('github', models.URLField(blank=True, default='https://github.com/WaksKevin/')),
                ('twitter', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('manifest', models.FileField(upload_to='base/WaksKevin')),
            ],
        ),
    ]
