# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-11 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0038_auto_20190402_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsuccesspage',
            name='topic',
            field=models.TextField(choices=[('contact-success-form', 'Contact domestic form success'), ('contact-events-success-form', 'Contact Events form success'), ('contact-dso-success-form', 'Contact Defence and Security Organisation form success'), ('contact-export-advice-success-form', 'Contact exporting from the UK form success'), ('contact-feedback-success-form', 'Contact feedback form success'), ('contact-find-companies-success-form', 'Contact find UK companies form success'), ('contact-international-success-form', 'Contact international form success'), ('contact-soo-success-form', 'Contact Selling Online Overseas form success'), ('contact-beis-success', 'Contact BEIS form success'), ('contact-defra-success', 'Contact DEFRA form success')], help_text='The slug and CMS page title are inferred from the topic', unique=True),
        ),
        migrations.AlterField(
            model_name='contactusguidancepage',
            name='topic',
            field=models.TextField(choices=[('alerts-not-relevant', 'Guidance - Daily alerts are not relevant'), ('opportunity-no-response', 'Guidance - Export Opportunity application no response'), ('no-verification-email', 'Guidance - Email verification missing'), ('password-reset', 'Guidance - Missing password reset link'), ('companies-house-login', 'Guidance - Companies House login not working'), ('verification-letter-code', 'Guidance - Where to enter letter verification code'), ('no-verification-letter', 'Guidance - Verification letter not delivered'), ('verification-missing', 'Guidance - Verification code not delivered'), ('company-not-found', 'Guidance - Company not found'), ('exporting-to-the-uk', 'Guidance - Exporting to the UK')], help_text='The slug and CMS page title are inferred from the topic', unique=True),
        ),
    ]
