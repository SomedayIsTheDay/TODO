from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .models import TODOUser
from .serializers import TODOUserModelSerializer, TODOUserModelSerializerV2


# class StaffOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_staff


class TODOUserCustomViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    queryset = TODOUser.objects.all()
    serializer_class = TODOUserModelSerializer

    def get_serializer_class(self):
        if self.request.version == "1.1":
            return TODOUserModelSerializerV2
        return TODOUserModelSerializer
