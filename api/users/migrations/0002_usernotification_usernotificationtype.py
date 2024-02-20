# Generated by Django 3.2 on 2023-04-17 15:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def create_notification_types(apps, schema_editor):
    NotificationTypeModel = apps.get_model('users', 'UserNotificationType')
    notification_types = ['bids', 'sessions', 'market', 'forecast', 'data']

    for notification_type in notification_types:
        NotificationTypeModel.objects.get_or_create(name=notification_type)


def populate_notifications(apps, schema_editor):
    NotificationModel = apps.get_model('users', 'UserNotification')
    UserModel = apps.get_model('users', 'User')
    NotificationTypeModel = apps.get_model('users', 'UserNotificationType')
    notifications = {
        'bid': [('New bid', 'Bid has been received'),
                ('Validation bid', 'Bid has been validated')],
        'session': [('New session', 'A new session is available'),
                    ('Session results', 'Results for a session are available')],
        'market': [('Market update', 'There is an update for the market'),
                   ('Market transaction', 'A transaction from the market for you has been made')],
        'forecast': [('New forecast', 'A new forecast is available for one or more of your resources')],
        'data': [
            ('Data correctly received', 'The market validated the reception of data sent for one of your resources'),
            ('Data incorrectly received', 'An error occurred with the data sent for one of your resources')],
    }

    for user in UserModel.objects.all():
        for notification_type_name, notification_details in notifications.items():
            notification_type = NotificationTypeModel.objects.get(name=notification_type_name)
            for notification_title, notification_description in notification_details:
                NotificationModel.objects.create(
                    user=user,
                    notification_title=notification_title,
                    notification_description=notification_description,
                    notification_type=notification_type,
                    state=True
                )


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_title', models.CharField(max_length=255)),
                ('notification_description', models.CharField(max_length=255)),
                ('state', models.BooleanField(default=True)),
                ('notification_type',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usernotificationtype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(create_notification_types),
        migrations.RunPython(populate_notifications),
    ]
