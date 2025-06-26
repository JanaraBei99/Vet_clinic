from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    # def validate(self, data):
    #     if len(data['password']) < 8:
    #         raise serializers.ValidationError("Password must be at least 8 characters long.")
    #     return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        if not data.get("username") or not data.get("password"):
            raise serializers.ValidationError("Both username and password are required.")
        return data
