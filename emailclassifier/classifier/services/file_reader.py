import os
import csv
from typing import Generator, Protocol, Iterator, List


LINE_TERMINATOR = '\r\n'
DELIMITER = ','


class CSVReader(Protocol):
    def __iter__(self) -> Iterator[List[str]]:
        ...


class LocalFileReader:

    @staticmethod
    def read_line(file_path: str) -> Generator[str, None, None]:
        if os.path.getsize(file_path) > 0:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    yield row
        return


class S3FileReader:
    pass
