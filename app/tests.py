import unittest
from app import create_app, db

class LibraryTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with self.app.app_context():
            db.create_all()

    def test_add_book(self):
        response = self.client.post('/books', json={"title": "Book A", "author": "Author A", "published_year": 2020})
        self.assertEqual(response.status_code, 201)
