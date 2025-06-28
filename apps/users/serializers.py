from rest_framework import serializers

from apps.users.models import User, Profile


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "password2",
        )

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        if not data.get("username") or not data.get("password"):
            raise serializers.ValidationError("Both username and password are required.")
        return data


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "role",
            "phone",
            "preferred_language",
            "clinic",
            "position",
            "specialization",
            "experience",
            "license_number",
            "city",
            "address",
            "name_of_organization",
            "type",
            "website",
            "description",
            "logo",
            "first_name",
            "last_name",
            "third_name",
        )

class EmaiSendSerializer(serializers.Serializer):
    email = serializers.EmailField()


class EmailVerifyCodeSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField()