from models import db, User

def test_user_create(app):

    with app.app_context():
        user = User(name="Isabella")
        user = User(name="Isabella")

        db.session.add(user)
        db.session.commit()

    # print(db.session.query(User).filter_by(name="Isabella").first())
    # assert User.name == "Isabella"


