# Generated by Django 2.0.4 on 2018-04-10 10:48

from django.db import migrations, models
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0013_auto_20180410_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', fontawesome.fields.IconField(blank=True, max_length=60)),
            ],
        ),
    ]
