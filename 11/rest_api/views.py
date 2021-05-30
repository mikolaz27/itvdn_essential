from rest_framework.authentication import TokenAuthentication

from graph_app.models import Car, ApiClient, Model, Make
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ModelSerializer, CarSerializer, MakeSerializer


def send_email(test):
    print("email is send")


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all().order_by('-name')
    serializer_class = ModelSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        send_email('my value 1')
        return super(ModelViewSet, self).get_queryset()


class MakeViewSet(viewsets.ModelViewSet):
    queryset = Make.objects.all().order_by('-name')
    serializer_class = MakeSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]
