from rest_framework import serializers
from .models import UserDetails, Question, AnswerOption, ExamAttempt, UserAnswer

class UserDetailsSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = UserDetails
        fields = ['national_id', 'full_name', 'date_of_birth', 'address', 'phone_number', 'email_address']

    def create(self, validated_data):
        user = UserDetails.objects.create(**validated_data)
        return user



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text']

class AnswerOptionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    class Meta:
        model = AnswerOption
        fields = ['id', 'option_text', 'is_correct', 'question']

class ExamAttemptSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()
    class Meta:
        model = ExamAttempt
        fields = ['id', 'user', 'start_time', 'end_time', 'score', 'date_test_taken', 'duration_minutes', 'num_questions']

class UserAnswerSerializer(serializers.ModelSerializer):
    answer_option = AnswerOptionSerializer()
    exam_attempt = ExamAttemptSerializer()
    question = QuestionSerializer()
    class Meta:
        model = UserAnswer
        fields = ['id', 'answer_option', 'exam_attempt', 'question']
