import os
import pickle

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
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
        x_train_resampled, y_train_resampled = resample(x_train, y_train, replace=True, n_samples=3000, random_state=0)

        # ===== USE GRID SEARCH TO FINE TUNE HYPER PARAMETERS =========
        # grid_search_param = {
        #     'learning_rate': [0.01],
        #     'n_estimators': [100, 200],
        #     'max_depth': [3, 4],
        #     'min_samples_leaf': [1, 2],
        #     'max_features': [None]
        # }

        # text_clf = Pipeline([
        #     ('vect', CountVectorizer()),
        #     ('tfidf', TfidfTransformer()),
        #     ('clf', GridSearchCV(GradientBoostingClassifier(random_state=42),
        #                          param_grid=grid_search_param,
        #                          cv=5,
        #                          refit=True,
        #                          n_jobs=5,
        #                          verbose=2))
        # ])

        text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', GradientBoostingClassifier(random_state=42))
        ])

        text_clf.fit(x_train_resampled, y_train_resampled)
        y_pred = text_clf.predict(x_test)

        # Calculate metrics
        accuracy = metrics.accuracy_score(y_test, y_pred)
        balanced_accuracy = metrics.balanced_accuracy_score(y_test, y_pred)
        precision = metrics.precision_score(y_test, y_pred, average='weighted')
        recall = metrics.recall_score(y_test, y_pred, average='weighted')
        f1_score = metrics.f1_score(y_test, y_pred, average='weighted')
        roc_auc_score = metrics.roc_auc_score(y_test, y_pred)
        cm = metrics.confusion_matrix(y_test, y_pred)

        # Print the metrics
        print(f"Accuracy: {accuracy}")
        print(f"Balanced Accuracy: {balanced_accuracy}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"F1 Score: {f1_score}")
        print(f"ROC AUC Score: {roc_auc_score}")
        print(cm)

        model_name = 'sklearn_model.sav'

        # Uncomment the line below to create another model
        pickle.dump(text_clf, open(model_name, 'wb'))


def run():
    training = SklearnTraining()
    x_data, y_data = training.get_data()
    training.training_pipeline(x_data, y_data)


if __name__ == '__main__':
    run()
