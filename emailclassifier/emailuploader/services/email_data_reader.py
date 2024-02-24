from io import TextIOWrapper, BytesIO, StringIO
from csv import reader, writer
from csv import QUOTE_ALL
import re


SUBJECT_PATTERN = re.compile(r'Subject:\s?(.*?)\n(.*)', re.DOTALL)


class EmailCSVReader:
    def read_email(self, io_data: BytesIO) -> BytesIO:
        output = StringIO()
        with TextIOWrapper(io_data, encoding='utf-8') as input_file:
            csv_reader = reader(input_file, lineterminator='\r\n')
            csv_writer = writer(output, quoting=QUOTE_ALL)
            for i, row in enumerate(csv_reader):
                # skip header
                if i == 0:
                    continue
                new_row = self.extract_subject_and_body(row)
                csv_writer.writerow(new_row)

            output_bytes = BytesIO(output.getvalue().encode())

        return output_bytes

    @staticmethod
    def extract_subject_and_body(row):
        return _extract_subject(row[0])


class EmailJSONReader:
    def read_email(self, io_data: BytesIO) -> BytesIO:
        pass


class EmailPickleReader:
    def read_email(self, io_data: BytesIO) -> BytesIO:
        pass


def _extract_subject(text):
    search = re.search(SUBJECT_PATTERN, text)
    if search is not None:
        g1 = search.group(1)
        g2 = search.group(2)
        return search.group(1), _convert_whitespace(search.group(2))
    return '', _convert_whitespace(text)


def _convert_whitespace(text):
    return text.replace('\n', '\t')
