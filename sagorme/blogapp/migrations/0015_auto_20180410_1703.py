# Generated by Django 2.0.4 on 2018-04-10 11:03

from django.db import migrations, models
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_categoryicon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50)),
                ('menu_name', models.CharField(max_length=65)),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='general')),
            ],
        ),
        migrations.CreateModel(
            name='Socail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('solid_link', models.CharField(max_length=120)),
                ('icon', fontawesome.fields.IconField(blank=True, max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='CategoryIcon',
        ),
    ]