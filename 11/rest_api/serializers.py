from graph_app.models import Car, ApiClient, Model, Make
from rest_framework import serializers


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = '__all__'


class CarSerializer(serializers.HyperlinkedModelSerializer):
    make = serializers.PrimaryKeyRelatedField(
        queryset=Make.objects.all(),
    )

    model = serializers.PrimaryKeyRelatedField(
        queryset=Model.objects.all(),
    )

    class Meta:
        model = Car
        fields = ['license_plate', 'notes', 'make', 'model']
