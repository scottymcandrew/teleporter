from django.http import HttpResponseBadRequest


# Enforces AJAX call to a resource to prevent a user just browisng to the URL
def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
