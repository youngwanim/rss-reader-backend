import json

import requests
import xmltodict
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from feed.models import Feed


def read_feed_list(request):
    feed_qs = Feed.objects.all()
    feed_list = []
    for i, feed in enumerate(feed_qs):
        _feed = dict()
        _feed['id'] = feed.id
        _feed['url'] = feed.url
        _feed['title'] = feed.title
        _feed['icon'] = feed.icon
        feed_list.append(_feed)

    feed_result = {'feed_list': feed_list}

    return JsonResponse(feed_result)


def read_feed_detail(request, feed_id):
    feed_o = Feed.objects.get(id=feed_id)
    feed_url = feed_o.url
    header = {'Content-type': 'application/xml'}

    response = requests.get(feed_url, headers=header)
    print('response.text:', str(response.text))
    feed_response = xmltodict.parse(response.text)['rss']

    return JsonResponse(feed_response)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@method_decorator(csrf_exempt, name='dispatch')
class FeedListView(View):
    def get(self, request):
        feed_qs = Feed.objects.all()
        feed_list = []
        for i, feed in enumerate(feed_qs):
            _feed = dict()
            _feed['id'] = feed.id
            _feed['url'] = feed.url
            _feed['title'] = feed.title
            _feed['icon'] = feed.icon
            feed_list.append(_feed)

        feed_result = {'feed_list': feed_list}

        return JsonResponse(feed_result)

    def post(self, request):
        request_data = json.loads(request.body)
        feed_data = {
            'url': request_data['url'],
            'title': request_data['title'],
            'icon': request_data.get('icon', '')
        }
        Feed.objects.create(**feed_data)

        feed_qs = Feed.objects.all()
        feed_list = []
        for i, feed in enumerate(feed_qs):
            _feed = dict()
            _feed['id'] = feed.id
            _feed['url'] = feed.url
            _feed['title'] = feed.title
            _feed['icon'] = feed.icon
            feed_list.append(_feed)

        feed_result = {'feed_list': feed_list}

        return JsonResponse(feed_result)
