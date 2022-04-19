from models import db, User, Post
from tests.factories import UserFactory, PostFactory

def test_create(app):

    with app.app_context():

        session = db.session

        user = User(name="Isabella")

        session.add(user)
        session.commit()

        post = Post(title="The Post", user=user)

        session.add(post)
        session.commit()

    post = db.session.query(Post).filter_by(title="The Post").first()
    assert post.title == "The Post"
    assert post.user.name == "Isabella"


def test_create_factory(app):
    post = PostFactory.create()

    assert post.id == 1
    assert hasattr(post, 'user')

