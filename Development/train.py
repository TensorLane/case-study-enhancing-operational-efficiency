from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from xgboost import XGBClassifier
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import joblib 
import pandas as pd

# Load the original data
df = pd.read_csv('latest_training_data.csv')
df_new = pd.read_csv('new_data.csv')
df_combined = pd.concat([df, df_new], ignore_index=True)

# encode Categorical Columns
categ = df.select_dtypes(include = "object").columns
le = preprocessing.LabelEncoder()
df[categ] = df[categ].apply(le.fit_transform)
df.head()

# drop date as it has low correlation
df_1 = df.drop('date', axis='columns')

# prepare the preprocessor
numerical_features = ['Usage_kWh','Lagging_Reactive_Power_kVarh','Leading_Reactive_Power_kVarh',
                      'CO2','Lagging_Power_Factor','Leading_Power_Factor','NSM']
passthrough_features = ['WeekStatus','Day_of_week']
preprocessor = make_column_transformer(
(make_pipeline(StandardScaler()),numerical_features,),
("passthrough", passthrough_features),)

# model definition
xgb_model = XGBClassifier()
pipe = make_pipeline(preprocessor, xgb_model)

# training the model
pipe.fit(X_train, y_train)
print(xgb_model)

# evaluate the model
score = pipe.score(X_test, y_test)
print("Model score: %.3f" %score)

# save the model
joblib.dump(pipe, 'xgb_model.joblib')