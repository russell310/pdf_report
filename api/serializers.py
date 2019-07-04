from rest_framework import serializers
from .models import DemoPurpose


class DemoSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	class Meta:
		model = DemoPurpose
		fields = ('url', 'id', 'name')

		
		# Specifying fields in datatables_always_serialize
        # will also force them to always be serialized.
		datatables_always_serialize = ('id',)

