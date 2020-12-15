from django.http import JsonResponse

from rest_framework.decorators import api_view

from car.models import Car
from car.serializers import CarSerializer


@api_view(['GET'])
def car_list(request):
    cars = Car.objects.all()

    car_name = request.GET.get('car_name', None)
    if car_name is not None:
        cars = cars.filter(car_name__icontains=car_name)

    cars_serializer = CarSerializer(cars, many=True)
    return JsonResponse(cars_serializer.data, safe=False)


@api_view(['GET'])
def car_detail(request, pk):
    car = Car.objects.get(pk=pk)

    car_serializer = CarSerializer(car)
    return JsonResponse(car_serializer.data)


