from django.http import JsonResponse

from rest_framework.decorators import api_view

from park.models import Park
from park.serializers import ParkSerializer


@api_view(['GET'])
def park_list(request):
    parks = Park.objects.all()

    name = request.GET.get('name', None)
    if name is not None:
        parks = parks.filter(name__icontains=name)

    parks_serializer = ParkSerializer(parks, many=True)
    return JsonResponse(parks_serializer.data, safe=False)


@api_view(['GET'])
def park_detail(request, pk):
    park = Park.objects.get(pk=pk)

    park_serializer = ParkSerializer(park)
    return JsonResponse(park_serializer.data)


