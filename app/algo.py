# import libraries
import pandas as pd
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import joblib

# import Data
df = pd.read_csv('../Data/data_cleaned.csv')

# split my data into train and test data
X_train, X_test, y_train, y_test = train_test_split(df['input_data'],
                                                    df['labels'],
                                                    train_size=0.8,
                                                    random_state=123)

# pipeline
model = make_pipeline(CountVectorizer(), TfidfTransformer(),
                      svm.SVC(C=1000, gamma=0.001, kernel='rbf', probability=True))

# fit the model
model = model.fit(X_train, y_train)

# save weights
model_filename = "../Models/model.pkl"
joblib.dump((model), model_filename)
