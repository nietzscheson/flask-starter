from models import db, User
from tests.factories import UserFactory

def test_create(app):

    with app.app_context():
        user = User(name="Isa")

        db.session.add(user)
        db.session.commit()

    assert db.session.query(User).filter_by(name="Isa").first().name == "Isa"

def test_create_factory(app):

    user = UserFactory.create(name="Emma")

    assert db.session.query(User).filter_by(name="Emma").first().name == "Emma"

