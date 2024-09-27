from rest_framework import serializers

from documents.models import ContractModel, VehicleModel, BusinessEntitiesModel


class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'


class ContractModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractModel
        fields = '__all__'


class FOPSerializer(serializers.ModelSerializer):
    """
            Serializer for FOP entities
    """
    vehicles = VehicleModelSerializer(many=True, read_only=True)
    contract = ContractModelSerializer(many=True, read_only=True)

    class Meta:
        model = BusinessEntitiesModel
        fields = [
            'business_entity',
            'code_edrpou',
            'fop_name',
            'address',
            'email',
            'phone',
            'iban',
            'bank_name',
            'mfo',
            'vehicles',
            'contract',
        ]
        read_only_fields = ['business_entity']

    def create(self, validated_data):
        vehicles_data = validated_data.pop('vehicles', [])

        validated_data['business_entity'] = BusinessEntitiesModel.BusinessEntitiesEnum.FOP
        fop = BusinessEntitiesModel.objects.create(**validated_data)

        for vehicle_data in vehicles_data:
            vehicle, created = VehicleModel.objects.get_or_create(**vehicle_data)
            fop.vehicles.add(vehicle)

        return fop

    def update(self, instance, validated_data):
        vehicles_data = validated_data.pop('vehicles', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if vehicles_data:
            instance.vehicles.clear()
            for vehicle_data in vehicles_data:
                vehicle, created = VehicleModel.objects.get_or_create(**vehicle_data)
                instance.vehicles.add(vehicle)

        return instance


class TOVSerializer(serializers.ModelSerializer):
    vehicles = VehicleModelSerializer(many=True, read_only=True)
    contract = ContractModelSerializer(many=True, read_only=True)
    """
            Serializer for TOV entities
    """
    class Meta:
        model = BusinessEntitiesModel
        fields = [
            'business_entity',
            'code_edrpou',
            'tov_name',
            'full_tov_name',
            'director_name',
            'address',
            'email',
            'phone',
            'iban',
            'bank_name',
            'mfo',
            'vehicles',
            'contract',
        ]
        read_only_fields = ['business_entity']

    def create(self, validated_data):
        vehicles_data = validated_data.pop('vehicles', [])

        validated_data['business_entity'] = BusinessEntitiesModel.BusinessEntitiesEnum.TOV
        fop = BusinessEntitiesModel.objects.create(**validated_data)

        for vehicle_data in vehicles_data:
            vehicle, created = VehicleModel.objects.get_or_create(**vehicle_data)
            fop.vehicles.add(vehicle)

        return fop

    def update(self, instance, validated_data):
        vehicles_data = validated_data.pop('vehicles', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if vehicles_data:
            instance.vehicles.clear()
            for vehicle_data in vehicles_data:
                vehicle, created = VehicleModel.objects.get_or_create(**vehicle_data)
                instance.vehicles.add(vehicle)

        return instance
