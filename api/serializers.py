from rest_framework import serializers

from project.models import Members,Account

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('first_name', 'last_name', 'phone_number', 'client_member_id', 'account')
