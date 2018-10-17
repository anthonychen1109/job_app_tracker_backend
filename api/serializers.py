from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import Company, Application, Interview, Note, Todo

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'user_id', 'company_id', 'note')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'company_name',
            'offer',
            'contact',
            'address',
            'city',
            'state',
            'phone_number',
            'user_id',
            'notes',
        )


class ApplicationSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(source="company_notes", many=True)
    class Meta:
        model = Application
        fields = (
            'id',
            'user_id',
            'status',
            'app_date',
            'interview_date',
            'company_id',
            'site_applied_from',
            'company_name',
            'company_offer',
            'company_contact',
            'company_address',
            'company_city',
            'company_state',
            'company_phone_number',
        )


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = (
            'id',
            'user_id',
            'company_id',
            'questions_asked',
        )


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user_id', 'task')


class UserSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(source="user_companies", many=True)
    todos = TodoSerializer(source="user_todos", many=True)
    class Meta:
        model = User
        fields = ('id','username', 'companies', 'todos',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password', )
