from .models import User
from rest_framework import serializers



class RegisterSerializer(serializers.ModelSerializer):
    # enforce write-only and a basic min-length check; detailed rules enforced via validate_password
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'password')

    def validate_password(self, value):
        # Use Django's password validation framework to enforce rules (min length, common password, numeric, etc.)
        from django.contrib.auth.password_validation import validate_password
        validate_password(value)
        return value

    def create(self, validated_data):
        # Use the custom user manager to create the user (sets password correctly)
        password = validated_data.pop('password')
        return User.objects.create_user(password=password, **validated_data)