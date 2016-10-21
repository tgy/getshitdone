from django.core.urlresolvers import resolve

def get_view(request):
    view = resolve(request.path)
    return {
        'view': view.url_name,
        'app': view.app_name
    }
