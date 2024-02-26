import os
import pickle

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.utils import resample
from sklearn import metrics

from preprocessor import get_class_dirs

# TRAINING MODULE FOR LOGISTIC REGRESSION

DATASET_DIR = 'dataset/'


class SklearnTraining:
    @staticmethod
    def get_data():
        x_data = []
        y_data = []
        class_dirs = get_class_dirs()
        for i, class_dir in enumerate(class_dirs):
            data_path = os.path.join(DATASET_DIR, class_dir, 'textdata.txt')
            with open(data_path, 'r', encoding='utf-8') as r:
                data = [text for text in r.read().split('\n') if text != '']
                x_data.extend(data)
                y_data.extend([i for _ in data])

        return x_data, y_data

    @staticmethod
    def training_pipeline(x_data, y_data):
        x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, random_state=0, train_size=0.75)
        x_train_resampled, y_train_resampled = resample(x_train, y_train, replace=True, n_samples=1000, random_state=0)

        text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                  alpha=1e-3, random_state=42,
                                  max_iter=5, tol=None))
        ])

        text_clf.fit(x_train_resampled, y_train_resampled)
        y_pred = text_clf.predict(x_test)

        print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
        print("Precision:", metrics.precision_score(y_test, y_pred, average='weighted'))
        print("Recall:", metrics.recall_score(y_test, y_pred, average='weighted'))
        print("F1 Score:", metrics.f1_score(y_test, y_pred, average='weighted'))

        model_name = 'sklearn_model.sav'
        pickle.dump(text_clf, open(model_name, 'wb'))


def run():
    training = SklearnTraining()
    x_data, y_data = training.get_data()
    training.training_pipeline(x_data, y_data)


if __name__ == '__main__':
    run()
