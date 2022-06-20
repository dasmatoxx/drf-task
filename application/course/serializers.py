from rest_framework import serializers

from application.course.models import Category, Branch, Contact, Course


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    course = serializers.Serializer(required=False)

    class Meta:
        model = Branch
        fields = ('id', 'longitude', 'latitude', 'address', 'course', )


class ContactSerializer(serializers.ModelSerializer):
    course = serializers.Serializer(required=False)

    class Meta:
        model = Contact
        fields = ('id', 'type', 'value', 'course', )


class CourseSerializer(serializers.ModelSerializer):

    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category', 'logo', 'category', 'contacts', 'branches']
    # def create(self, validate_data):
    #     contacts_data = validate_data.pop('contacts')
    #     branchs_data = validate_data.pop('branches')
    #     contacts = []
    #     branchs = []
    #     course = Course.objects.create(**validate_data)
    #     # for contact_data in contacts_data:
    #     #     contact = Contact.objects.get(id=contact_data['id'])
    #     #     contacts.append(contact)
    #     # validate_data['contacts'] = contacts
    #     # return course
    #     for contact_data in contacts_data:
    #         contact_id = contact_data.id
    #         contact = Contact.objects.get_or_create(id=contact_id, defaults=contact_data)
    #         contacts.append(contact)
    #
    #     # course.contacts.add(**contact)
    #     return course

    def create(self, validate_data):
        print(validate_data)
        contacts = validate_data.pop('contacts')
        branches = validate_data.pop('branches')

        course = Course.objects.create(**validate_data)
        for contact in contacts:
            Contact.objects.create(type=contact.get('type', ''), course=course, value=contact.get('value', ''))

        for branch in branches:
            Branch.objects.create(
                course=course, longitude=branch.get('longitude', ''),
                latitude=branch.get('latitude', ''), address=branch.get('address', '')
            )

        return course

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     return rep
