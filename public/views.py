from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Count
from features.models import Feature
from bugs.models import Bug


def index(request):
    return render(request, 'public/index.html')


def about_us(request):
    return render(request, 'public/about_us.html')


def service_stats(request):
    implemented_features = Feature.objects.all().filter(category='Roadmap').filter(status='Implemented').order_by(
        '-purchases')[:5]
    return render(request, 'public/service_stats.html',
                  {'implemented_features': implemented_features})


def all_features_chart(request):
    """
    Return all active features for use in chart.js - Public Statistics
    """
    labels = []
    data = []

    queryset = Feature.objects.values('title').order_by('-created').exclude(status='Implemented').annotate(
        feature_purchases=Sum('purchases'))[:5]
    for entry in queryset:
        labels.append(entry['title'])
        data.append(entry['feature_purchases'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def all_bugs_chart(request):
    """
    Return all active features for use in chart.js - Public Statistics
    """
    labels = []
    data = []

    queryset = Bug.objects.values('title', 'id').order_by('-created').exclude(status='Resolved').annotate(
        bug_votes=Count('votes'))[:5]
    for entry in queryset:
        labels.append(entry['title'])
        data.append(entry['bug_votes'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def resolved_bugs_chart(request):
    """
    Return resolved bugs
    """
    labels = []
    data = []
    queryset = Bug.objects.values('title', 'id').order_by('-created').filter(status='Resolved')[:5]
    print(queryset)
    for entry in queryset:
        bug = get_object_or_404(Bug, id=entry['id'])
        print(bug.get_time_to_resolution())
        labels.append(entry['title'])
        data.append(bug.get_time_to_resolution())

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
