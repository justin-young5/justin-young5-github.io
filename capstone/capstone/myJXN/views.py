from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def map_view(request):
    return render(request, 'map.html', {})

class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"