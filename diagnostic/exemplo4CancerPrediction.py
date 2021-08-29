import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

import warnings
warnings.filterwarnings('ignore')

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


df = pd.read_csv('/kaggle/input/breast-cancer-wisconsin/breast cancer.csv')
df.head()
df.tail()

df.shape

df.describe().T
df.diagnosis.unique()

df['diagnosis'].value_counts()
sns.countplot(df['diagnosis'], palette='husl')

#clean and prepare the data
df.drop('id',axis=1,inplace=True)
df.drop('Unnamed: 32',axis=1,inplace=True)
df.head()

df['diagnosis'] = df['diagnosis'].map({'M':1,'B':0})
df.head()

plt.figure(figsize=(20,20))
sns.heatmap(df.corr(), annot=True)
