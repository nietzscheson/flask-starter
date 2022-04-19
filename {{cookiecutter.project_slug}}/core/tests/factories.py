import factory
from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker
from models import db, User, Post

fake = Faker()

class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_get_or_create = ('name',)
        sqlalchemy_session_persistence="commit"

    name = factory.Faker("name")

class PostFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Post
        sqlalchemy_session = db.session
        sqlalchemy_get_or_create = ('title',)
        sqlalchemy_session_persistence="commit"

    title = factory.Faker("name")
    user = factory.SubFactory(UserFactory)
