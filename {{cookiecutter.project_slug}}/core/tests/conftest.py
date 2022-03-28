import pytest
from app import app as _app
from models import db as _db
from sqlalchemy import event

# @pytest.fixture()
# def app():
#     _app.testing = True
#
#     yield _app
#
# @pytest.fixture(scope="session")
# def db(app):
#     """
#     Returns session-wide initialised database.
#     """
#     with app.app_context():
#         _db.drop_all()
#         _db.create_all()
#
#         yield _db
#
#         _db.drop_all()
#
#
#
# @pytest.fixture(scope="function", autouse=True)
# def session(app, db):
#     """
#     Returns function-scoped session.
#     """
#     with app.app_context():
#
#         # establish  a SAVEPOINT just before beginning the test
#         # (http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#using-savepoint)
#         _db.session.begin_nested()
#
#         @event.listens_for(_db.session, "after_transaction_end")
#         def restart_savepoint(sess2, trans):
#             # Detecting whether this is indeed the nested transaction of the test
#             if trans.nested and not trans._parent.nested:
#                 # The test should have normally called session.commit(),
#                 # but to be safe we explicitly expire the session
#                 sess2.expire_all()
#                 _db.session.begin_nested()
#
#         yield _db
#
#         # Cleanup
#         _db.session.remove()
#         # This instruction rolls back any commit that were executed in the tests.
#         _db.session.rollback()

@pytest.fixture(scope="session")
def app():
    _app.testing = True

    return _app


@pytest.fixture(scope="session")
def db(app):
    """
    Returns session-wide initialised database.
    """
    with app.app_context():
        _db.drop_all()
        _db.create_all()

        yield _db

        _db.drop_all()


@pytest.fixture(scope="function", autouse=True)
def session(app, db):
    """
    Returns function-scoped session.
    """
    with app.app_context():

        # establish  a SAVEPOINT just before beginning the test
        # (http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#using-savepoint)
        _db.session.begin_nested()

        @event.listens_for(_db.session, "after_transaction_end")
        def restart_savepoint(sess2, trans):
            # Detecting whether this is indeed the nested transaction of the test
            if trans.nested and not trans._parent.nested:
                # The test should have normally called session.commit(),
                # but to be safe we explicitly expire the session
                sess2.expire_all()
                _db.session.begin_nested()

        yield _db

        # Cleanup
        _db.session.remove()
        # This instruction rolls back any commit that were executed in the tests.
        _db.session.rollback()


@pytest.fixture()
def client(app):
    return app.test_client()
