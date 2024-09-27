from rest_framework import viewsets, permissions

from documents.models import BusinessEntitiesModel
from documents.serializers import FOPSerializer, TOVSerializer


class FOPViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling FOP (Фізична особа-підприємець) entities.
    """
    queryset = BusinessEntitiesModel.objects.filter(
        business_entity=BusinessEntitiesModel.BusinessEntitiesEnum.FOP
    )
    serializer_class = FOPSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(business_entity=BusinessEntitiesModel.BusinessEntitiesEnum.FOP)

    def perform_update(self, serializer):
        serializer.save(business_entity=BusinessEntitiesModel.BusinessEntitiesEnum.FOP)


class TOVViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling TOV (Товариство з обмеженою відповідальністю) entities.
    """
    queryset = BusinessEntitiesModel.objects.filter(
        business_entity=BusinessEntitiesModel.BusinessEntitiesEnum.TOV
    )
    serializer_class = TOVSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(business_entity=BusinessEntitiesModel.BusinessEntitiesEnum.TOV)

    def perform_update(self, serializer):
        serializer.save(business_entity=BusinessEntitiesModel.BusinessEntitiesEnum.TOV)