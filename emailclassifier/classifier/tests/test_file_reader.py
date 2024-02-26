import os
from django.conf import settings
from django.test import TestCase

from ..services.file_reader import LocalFileReader

BASE_DIR = settings.BASE_DIR


class FileReaderTest(TestCase):

    def test_local_file_reader_normal(self):
        csv_path = os.path.join(BASE_DIR, 'classifier/tests/test-datasets/test-dataset_normal.csv')
        reader = LocalFileReader()
        generator = reader.read_line(csv_path)
        for row in generator:
            compare_subject = 'this is a test email subject'
            compare_body = 'this is a test email body\thello world'
            self.assertEqual(len(row), 2)
            self.assertEqual(row[0], compare_subject)
            self.assertEqual(row[1], compare_body)
        self.assertEqual(next(generator, 'exhausted'), 'exhausted')

    def test_local_file_reader_empty(self):
        csv_path = os.path.join(BASE_DIR, 'classifier/tests/test-datasets/test-dataset_empty.csv')
        reader = LocalFileReader()
        generator = reader.read_line(csv_path)
        for _ in generator:
            pass
        self.assertEqual(next(generator, 'exhausted'), 'exhausted')