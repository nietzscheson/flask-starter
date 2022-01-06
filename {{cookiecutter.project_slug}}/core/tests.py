import os
from flask import Flask
import unittest
from app import app
from models import db, User

app.testing = True

class TestApi(unittest.TestCase):
    def test_index(self):
        client = app.test_client(self)
        response = client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, bytes(f"Hello, {os.environ['NAME']}!", 'utf-8'))

class TestDatabase(unittest.TestCase):

    def __init__(self, methodName) -> None:
        super().__init__(methodName=methodName)
        self.app = Flask(__name__)
        self.app.config.from_object("config.Config")
        db.init_app(self.app)


    def setUp(self):
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Ensures that the database is emptied for next unittest
        """
        with self.app.app_context():
            db.drop_all()

    def test_user_create(self):

        with self.app.app_context():
            user = User(name="Isabella")
            db.session.add(user)
            db.session.commit()

            self.assertEqual(User.query.get(1).name, "Isabella")
