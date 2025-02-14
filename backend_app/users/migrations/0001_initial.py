# Generated by Django 3.0.6 on 2020-05-12 14:31

import annoying.fields
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cves', '0001_initial'),
        ('organizations', '0003_field_fix_and_editable'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalOrgSettings',
            fields=[
                ('max_users', models.IntegerField(default=0, null=True)),
                ('max_monitored_items', models.IntegerField(default=10, null=True)),
                ('max_email_contacts', models.IntegerField(default=3, null=True)),
                ('alerts_emails_enabled', models.BooleanField(default=True)),
                ('alerts_emails', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250), null=True, size=None)),
                ('alerts_slack_enabled', models.BooleanField(default=False)),
                ('alerts_slack', django.contrib.postgres.fields.jsonb.JSONField(default=users.models.slack_dict)),
                ('alerts_thehive_enabled', models.BooleanField(default=False)),
                ('alerts_thehive', django.contrib.postgres.fields.jsonb.JSONField(default=users.models.thehive_dict)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical org settings',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='OrgSettings',
            fields=[
                ('organization', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='org_settings', serialize=False, to='organizations.Organization')),
                ('max_users', models.IntegerField(default=0, null=True)),
                ('max_monitored_items', models.IntegerField(default=10, null=True)),
                ('max_email_contacts', models.IntegerField(default=3, null=True)),
                ('alerts_emails_enabled', models.BooleanField(default=True)),
                ('alerts_emails', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250), null=True, size=None)),
                ('alerts_slack_enabled', models.BooleanField(default=False)),
                ('alerts_slack', django.contrib.postgres.fields.jsonb.JSONField(default=users.models.slack_dict)),
                ('alerts_thehive_enabled', models.BooleanField(default=False)),
                ('alerts_thehive', django.contrib.postgres.fields.jsonb.JSONField(default=users.models.thehive_dict)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'org_settings',
            },
        ),
        migrations.CreateModel(
            name='OrgMonitoringList',
            fields=[
                ('organization', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='org_monitoring_list', serialize=False, to='organizations.Organization')),
                ('products', models.ManyToManyField(related_name='org_monitoring_list', to='cves.Product')),
                ('productversions', models.ManyToManyField(related_name='org_monitoring_list', to='cves.ProductVersion')),
                ('vendors', models.ManyToManyField(related_name='org_monitoring_list', to='cves.Vendor')),
            ],
            options={
                'db_table': 'org_monitoring_list',
            },
        ),
    ]
