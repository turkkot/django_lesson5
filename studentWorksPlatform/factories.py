import factory
from factory.django import ImageField
from studentWorksPlatform import models

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    password = factory.Faker('password')
    email = factory.Faker('email')
    balance = factory.Faker('random_int')
    rating = factory.Faker('random_int')
    profile_picture = ImageField()
    class Meta:
        model = models.User

class SubjectFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    class Meta:
        model = models.Subject

class WorkFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('name')
    description = factory.Faker('name')
    subject = factory.SubFactory(SubjectFactory)
    file = factory.Faker('name')
    price = factory.Faker('random_int')
    author = factory.SubFactory(UserFactory)
    image = ImageField()
    class Meta:
        model = models.Work