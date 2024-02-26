import csv
import os
from typing import List, Tuple, NoReturn

# ========= NOTES ========================
# Expected Raw Dataset Format: .csv
# id,email_subject,email_body,email_class

DATASET_DIR = 'dataset/'
PATH = os.path.join(DATASET_DIR, 'rawdata.csv')


def get_class_dirs():
    return [classdir for classdir in os.listdir(DATASET_DIR) if classdir.startswith('class')]


class MLPreprocessor:
    def preprocess(self):
        raw_data = self.read_raw_data(PATH)
        self.segregate_data(raw_data)
        pass

    @staticmethod
    def read_raw_data(file_path: str) -> List[Tuple[str, str]]:
        raw_data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                if len(row) == 4:
                    _, subject, body, email_class = row
                    raw_data.append((subject + '\t' + body, email_class))

        return raw_data

    @staticmethod
    def segregate_data(data: List[Tuple[str, str]]) -> NoReturn:
        class_dirs = get_class_dirs()
        for class_dir in class_dirs:
            write_path = os.path.join(DATASET_DIR, class_dir, 'textdata.txt')
            with open(write_path, 'w', encoding='utf-8') as w:
                for content, email_class in data:
                    if f'class_{email_class}' == class_dir:
                        w.write(content)
                        w.write('\n')


def run():
    processor = MLPreprocessor()
    processor.preprocess()


if __name__ == '__main__':
    run()

