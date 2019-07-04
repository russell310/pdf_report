from rest_framework import viewsets
from .models import DemoPurpose
from .serializers import DemoSerializer


class DemoViewSet(viewsets.ModelViewSet):
    queryset = DemoPurpose.objects.all()
    serializer_class = DemoSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(DemoViewSet, self).get_serializer(*args, **kwargs)
