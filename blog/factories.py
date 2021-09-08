import factory
from factory.django import DjangoModelFactory

from .models import Tag, Category, Post
from users.factories import UserFactory
from notifications.models import Notification


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = 'tag'


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = 'category'
    slug = factory.Sequence(lambda n: 'category-slug{}'.format(n))
    status = Category.STATUS_CHOICES.ongoing
    creator = factory.SubFactory(UserFactory)


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = 'post title'
    body = 'post body'
    author = factory.SubFactory(UserFactory)


class NotificationFactory(DjangoModelFactory):
    class Meta:
        model = Notification

    recipient = factory.SubFactory(UserFactory)
    actor = factory.SubFactory(UserFactory)
    verb = 'notify'
