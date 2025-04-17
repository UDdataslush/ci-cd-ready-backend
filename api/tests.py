import unittest
from api.models import Book
from django.test import TestCase

# Create your tests here.


class BookModelUnitTest(unittest.TestCase):
    def test_book_creation(self):
        book = Book(title="My Book", author="Author", published_date="2024-01-01")
        self.assertEqual(book.title, "My Book")
