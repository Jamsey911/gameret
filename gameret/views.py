"""
Imports for gameret views
"""
from django.shortcuts import render
from django.core.exceptions import PermissionDenied


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """Rendering the 500 page."""
    return render(request, 'errors/500.html', status=500)


def handler403(request, exception):
    """Rendering the 403 page."""
    if isinstance(exception, PermissionDenied):
        return render(request, 'errors/403.html', status=403)
    else:
        return render(request, 'errors/500.html', status=500)
