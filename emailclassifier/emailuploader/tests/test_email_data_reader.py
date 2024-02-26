import os
from io import BytesIO
from django.test import TestCase
from django.conf import settings

from ..services.email_data_reader import EmailCSVReader

BASE_DIR = settings.BASE_DIR


class EmailDataReaderTest(TestCase):
    def test_email_csv_reader_normal(self):
        reader = EmailCSVReader()
        csv_path = os.path.join(BASE_DIR, 'emailuploader/tests/test-datasets/test-dataset_normal.csv')
        with open(csv_path, 'rb') as r:
            content = r.read()
            content_bytes = BytesIO(content)
            output_bytes = reader.read_email(content_bytes)
            output = output_bytes.getvalue().decode('utf-8').strip()
            compare_value = """\"This is a sample email subject.","Hello!, this is a sample email.	\"""".strip()
            self.assertEqual(output, compare_value)

    def test_email_csv_reader_empty(self):
        reader = EmailCSVReader()
        csv_path = os.path.join(BASE_DIR, 'emailuploader/tests/test-datasets/test-dataset_empty.csv')
        with open(csv_path, 'rb') as r:
            content = r.read()
            content_bytes = BytesIO(content)
            output_bytes = reader.read_email(content_bytes)
            output = output_bytes.getvalue().decode('utf-8').strip()
            compare_value = ''
            self.assertEqual(output, compare_value)

    def test_email_csv_reader_extra_column(self):
        reader = EmailCSVReader()
        csv_path = os.path.join(BASE_DIR, 'emailuploader/tests/test-datasets/test-dataset_extra_column.csv')
        with open(csv_path, 'rb') as r:
            content = r.read()
            content_bytes = BytesIO(content)
            output_bytes = reader.read_email(content_bytes)
            output = output_bytes.getvalue().decode('utf-8').strip()
            compare_value = """\"This is a sample email subject.","Hello!, this is a sample email.\"""".strip()
            self.assertEqual(output, compare_value)