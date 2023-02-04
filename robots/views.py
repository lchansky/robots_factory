import json
import os

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView


from robots.models import Robot
from robots.reports import get_weekly_report


class API(APIView):
    def post(self, request):
        post_data = request.data
        try:
            robot = Robot.objects.create(**post_data)
        except ValidationError as e:
            return HttpResponseBadRequest(content=json.dumps(e.message_dict))

        robot_dict = robot.__dict__
        robot_dict.pop('_state')
        return Response(data=robot_dict)


def download_last_week_report(request):
    excel_bytes = get_weekly_report()

    response = HttpResponse(excel_bytes, content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = 'inline; filename=last_week_report.xlsx'
    return response
