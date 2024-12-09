from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pet, Owner, Appointment, Treatment
from .serializers import (
    PetSerializer,
    OwnerSerializer,
    AppointmentSerializer,
    TreatmentSerializer,
)

# Create your views here.


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class CustomAPIView(APIView):
    def get(self, request, format=None):
        date = request.query_params.get("date", None)
        veterinarian = request.query_params.get("veterinarian", None)
        appointments = Appointment.objects.all()
        if date:
            appointments = appointments.filter(date=date)
        if veterinarian:
            appointments = appointments.filter(veterinarian=veterinarian)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
