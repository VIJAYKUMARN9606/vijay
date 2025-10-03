# Classification report for the SVC model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import RandomOverSampler

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('Rainfall.csv')

df.head()
#print(df)
#data
df.shape #data added by us
#print(data)
df.info()

#data=
df.describe().T #mean print by using data
#print(data)

#l using to print values
df.isnull().sum()
#print(l)

#c printing index values
df.columns
#print(c)

df.rename(str.strip,
          axis='columns',
          inplace=True)

#n commenting index values with weather condition
df.columns
#print(n)

for col in df.columns:

    # Checking if the column contains
    # any null values
    if df[col].isnull().sum() > 0:
        val = df[col].mean()
        df[col] = df[col].fillna(val)

#p printing value is found or not
df.isnull().sum().sum()
#print(p)

plt.pie(df['rainfall'].value_counts().values,
        labels = df['rainfall'].value_counts().index,
        autopct='%1.1f%%')
plt.show()

#mean putting mean to get values
df.groupby('rainfall').mean()
#print(mean)

features = list(df.select_dtypes(include = np.number).columns)
features.remove('day')
print(features)

plt.subplots(figsize=(15,8))

for i, col in enumerate(features):
  plt.subplot(3,4, i + 1)
  sb.distplot(df[col])
plt.tight_layout()
plt.show()

plt.subplots(figsize=(15,8))

for i, col in enumerate(features):
  plt.subplot(3,4, i + 1)
  sb.boxplot(df[col])
plt.tight_layout()
plt.show()

df.replace({'yes':1, 'no':0}, inplace=True)

plt.figure(figsize=(10,10))
sb.heatmap(df.corr() > 0.8,
           annot=True,
           cbar=False)
plt.show()

df.drop(['maxtemp', 'mintemp'], axis=1, inplace=True)

features = df.drop(['day', 'rainfall'], axis=1)
target = df.rainfall

X_train, X_val, \
    Y_train, Y_val = train_test_split(features,
                                      target,
                                      test_size=0.2,
                                      stratify=target,
                                      random_state=2)

# As the data was highly imbalanced we will
# balance it by adding repetitive rows of minority class.
ros = RandomOverSampler(sampling_strategy='minority',
                        random_state=22)
X, Y = ros.fit_resample(X_train, Y_train)

# Normalizing the features for stable and fast training.
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_val = scaler.transform(X_val)

models = [LogisticRegression(), XGBClassifier(), SVC(kernel='rbf', probability=True)]

#for i in range(3):
 # models[i].fit(X, Y)

  #print(f'{models[i]} : ')

  #train_preds = models[i].predict_proba(X)
  #print('Training Accuracy : ', metrics.roc_auc_score(Y, train_preds[:,1]))

  #val_preds = models[i].predict_proba(X_val)
  #print('Validation Accuracy : ', metrics.roc_auc_score(Y_val, val_preds[:,1]))
  #print()

  #import matplotlib.pyplot as plt
  #from sklearn.metrics import ConfusionMatrixDisplay
  #from sklearn import metrics

  #ConfusionMatrixDisplay.from_estimator(models[2], X_val, Y_val)
  #plt.show()

#print(metrics.classification_report(Y_val,
 #                                   models[2].predict(X_val)))

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Train and evaluate all models
for i, model in enumerate(models):
    model.fit(X, Y)
    print(f'{model}:')

    # Training accuracy
    train_preds = model.predict_proba(X)
    print('Training Accuracy:', metrics.roc_auc_score(Y, train_preds[:, 1]))

    # Validation accuracy
    val_preds = model.predict_proba(X_val)
    print('Validation Accuracy:', metrics.roc_auc_score(Y_val, val_preds[:, 1]))
    print()
    # Confusion Matrix Display
    ConfusionMatrixDisplay.from_estimator(model, X_val, Y_val)
    plt.title(f'Confusion Matrix for Model {i}')
    plt.show()

models[2].predict(X_val)
print(metrics.classification_report(Y_val, svc_preds))
