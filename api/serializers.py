from rest_framework import serializers
from .models import Company, Application, Interview

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
        )

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            'id',
            'user_id',
            'status',
            'app_date',
            'interview_date',
            'company_id',
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
