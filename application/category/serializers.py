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
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validate_data):
        contacts_data = validate_data.pop('contacts')
        branchs_data = validate_data.pop('branches')
        contacts = []
        branchs = []
        course = Course.objects.create(**validate_data)
        for contact_data in contacts_data:
            contact = Contact.objects.get(id=contact_data['id'])
            contacts.append(contact)
        validate_data['contacts'] = contacts
        return course
        # for contact_data in contacts_data:
        #     print(contact_data)
        #     contact_id = contacts_data.pop('id')
        #     print(contact_id)
        #     contact = Contact.objects.get_or_create(id=contact_id, defaults=contact_data)
        #
        #     contacts.append(contact)
        #
        # course.contacts.add(**contact)
        # return course
        # for branch_data in branchs_data:
        #     branch_id = branchs_data.pop('id')
        #     branch = Branch.objects.get_or_create(id=branch_id,
        #                                                  defaults=branch_data)
        #     branchs.append(branch)
        # instance.contacts.add(*contacts)
        # instance.branchs.add(*branch)

        # return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep
