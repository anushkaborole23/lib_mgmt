# Generated by Django 4.2.4 on 2023-09-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0004_transaction_available_alter_transaction_issue_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='available',
        ),
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]