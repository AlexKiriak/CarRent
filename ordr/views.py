from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from ordr.models import Ordr
from ordr.serializers import OrdrSerializer


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Ordr.objects.all()

        orders_serializer = OrdrSerializer(orders, many=True)
        return JsonResponse(orders_serializer.data, safe=False)
    else:
        order_data = JSONParser().parse(request)
        order_serializer = OrdrSerializer(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse(order_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, order_id):
    try:
        orders = Ordr.objects.get(order_id=order_id)
    except Ordr.DoesNotExist:
        return JsonResponse({'message:': 'Order does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        order_serializer = OrdrSerializer(orders)
        return JsonResponse(order_serializer.data)
    elif request.method == 'PUT':
        order_data = JSONParser().parse(request)
        order_serializer = OrdrSerializer(orders, data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse(order_serializer.data)
        return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        orders.delete()
        return JsonResponse({'message': 'Order was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

