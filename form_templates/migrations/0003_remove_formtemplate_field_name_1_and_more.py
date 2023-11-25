# Generated by Django 4.2.7 on 2023-11-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_templates', '0002_remove_formtemplate_fields_formtemplate_field_name_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formtemplate',
            name='field_name_1',
        ),
        migrations.RemoveField(
            model_name='formtemplate',
            name='field_name_2',
        ),
        migrations.AddField(
            model_name='formtemplate',
            name='fields',
            field=models.JSONField(blank=True, null=True),
        ),
    ]