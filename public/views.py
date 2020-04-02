from django.http import JsonResponse
from django.shortcuts import render
from features.models import Feature


def index(request):
    return render(request, 'public/index.html')


def about_us(request):
    return render(request, 'public/about_us.html')


def service_stats(request):
    return render(request, 'public/service_stats.html')


# def all_features_chart(request):
#     """
#     Return all features for use in chart.js
#     """
#     labels = []
#     data = []
#
#     queryset = Feature.objects.values('title').annotate(feature_purchases=Sum('purchases'))
#     for entry in queryset:
#         labels.append(entry['title'])
#         data.append(entry['feature_purchases'])
#
#     return JsonResponse(data={
#         'labels': labels,
#         'data': data,
#     })
