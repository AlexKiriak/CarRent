from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from ordr.models import Ordr
from ordr.serializers import OrdrSerializer


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Ordr.objects.values("order_id")

        orders_serializer = OrdrSerializer(orders, many=True)
        return JsonResponse(orders_serializer.data, safe=False)
    else:
        order_data = JSONParser().parse(request)
        order_serializer = OrdrSerializer(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse(order_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
