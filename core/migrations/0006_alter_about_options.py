# Generated by Django 4.1.1 on 2022-12-12 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_post_author_alter_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['-created'], 'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactanos'},
        ),
    ]