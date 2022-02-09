import datetime

from django.http import HttpResponse
from rest_framework import request

from taskapp.forms import ManageReportForm
from taskapp.models import *
from datetime import timedelta


def my_cron_job_reporting():
    import datetime
    report = Reporting.objects.filter(duration_from=datetime.datetime.now().date())
    for data in report:
        person = User.objects.filter(reporting_to=data.existing_reporting_to)
        for name in person:
            name.reporting_to = data.new_reporting_to
            name.save()
    report = Reporting.objects.filter(duration_till=datetime.datetime.now().date())
    for data in report:
        person = User.objects.filter(reporting_to=data.new_reporting_to)
        for name in person:
            name.reporting_to = data.existing_reporting_to
            name.save()
