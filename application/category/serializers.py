from rest_framework import serializers

from application.category.models import Category, Branch, Contact, Course


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('type', 'value')




class CourseSerializer(serializers.ModelSerializer):


    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validate_data):
        # contact = Course.objects.filter(contacts=ContactSerializer)
        instance = Course.objects.create(**validate_data)
        # print(validate_data)
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep
