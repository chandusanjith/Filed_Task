from django.urls import path, include
from django.http import HttpResponse, FileResponse
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .serializer import PaymentSerializer
from rest_framework.response import Response
from rest_framework import status
from .PaymentGateWays import PremiumPaymentGateWay, CheapPaymentGateWay, ExpensivePaymentGateWay

class SnippetList(APIView):

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ws_amount = request.data['Amount']
            if ws_amount < 20:
               if CheapPaymentGateWay(request.data) == 1:
                 return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
               else:
                 return Response(serializer.data, status=status.HTTP_200_OK)
            elif ws_amount > 20 and ws_amount <= 500:
              if ExpensivePaymentGateWay(request.data) == 1:
                  if CheapPaymentGateWay(request.data) == 1:
                    return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                  else:
                    return Response(serializer.data, status=status.HTTP_200_OK)
              else:
                  return Response(serializer.data, status=status.HTTP_200_OK)                   
            elif ws_amount > 500:
              for i in range(1,4):
                 if PremiumPaymentGateWay(request.data) == 0:
                    return Response(serializer.data, status=status.HTTP_200_OK)
              else:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)