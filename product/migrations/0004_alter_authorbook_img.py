# Generated by Django 4.2.5 on 2023-09-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_authorbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorbook',
            name='img',
            field=models.ImageField(blank=True, default='static/authimg/authimg.png', upload_to='author_book'),
        ),
    ]