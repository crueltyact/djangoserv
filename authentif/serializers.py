from rest_framework import serializers
from authentif.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['email', 'first_name', 'last_name', 'photo', 'is_active', 'password']
        extra_kwargs = {
            'password': {'write_only':True}
        }
        

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance_is_active = True

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
        # return super().create(validated_data)
