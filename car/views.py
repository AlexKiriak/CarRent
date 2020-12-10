from django.http import JsonResponse

from rest_framework.decorators import api_view

from car.models import Car
from car.serializers import CarSerializer


@api_view(['GET'])
def car_list(request):
    cars = Car.objects.all()

    name = request.GET.get('name', None)
    if name is not None:
        cars = cars.filter(name__icontains=name)

    cars_serializer = CarSerializer(cars, many=True)
    return JsonResponse(cars_serializer.data, safe=False)


@api_view(['GET'])
def car_detail(request, pk):
    car = Car.objects.get(pk=pk)

    car_serializer = CarSerializer(car)
    return JsonResponse(car_serializer.data)


