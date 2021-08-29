import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier


print("1")

#df = pd.read_csv(r'C:\Users\Marcelo\Desktop\TCC\CHAGAS_COL_ATT.CSV', encoding='iso-8859-1', error_bad_lines=False)


df = pd.read_excel(r'C:\Users\Marcelo\Desktop\TCC\chaga_colunas.xlsx')
print("2")

#print(df.head())

# dividir o dataset entre treino e teste

# separar as variáveis independentes da variável alvo
"""
X = df.drop(['diagnosis', 'id'], axis=1)
y = df['diagnosis']
"""


sns.countplot(df["CLASSI_FIN"])


#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)