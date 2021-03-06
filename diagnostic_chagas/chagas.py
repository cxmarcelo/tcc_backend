import sys
import json
import pandas as pd
from time import time
from scipy.sparse import data
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.preprocessing import LabelEncoder

colunas = ['dt_notific',
 'sg_uf',
 'id_mn_resi',
 'cs_sexo',
 'cs_gestant',
 'cs_raca',
 'dt_invest',
 'id_ocupa_n',
 'ant_uf_1',
 'ant_uf_2',
 'ant_uf_3',
 'mun_1',
 'mun_2',
 'mun_3',
 'historia',
 'assintoma',
 'edema',
 'meningoe',
 'poliadeno',
 'febre',
 'hepatome',
 'sinais_icc',
 'arritmias',
 'astenia',
 'esplenom',
 'chagoma',
 'exame',
 'xenodiag']

class Chagas():
       '''
              RandomForestClassifier: {'max_depth': 16, 'n_estimators': 256}\n
              Parametros --
              sql :  str SQL query or SQLAlchemy Selectable (select or text object)
                     SQL query to be executed.
              con :  SQLAlchemy connectable, str, or sqlite3 connection
                     Using SQLAlchemy makes it possible to use any DB supported by that library. If a DBAPI2 object, only sqlite3 is supported.
       '''
       
       def __init__(self, dataframe, threshold=False):
              '''
                     Recebe um dataframe.
              '''
              chagas = pd.DataFrame()
              chagas = dataframe
              if not chagas.empty:
                     chagas = dataframe
              else:
                     print("Erro ao iniciar Classe Chagas. Encerrando API.")
                     sys.exit(0)
              # remove possiveis pacientes novos com valores nulos
              chagas.dropna(subset=['classi_fin'], inplace=True)
              if bool(threshold):
                     self.threshold = threshold
              else:
                     self.threshold = 0.12
              self.parametros = chagas[colunas]
              self.resultados = chagas['classi_fin']
              # Converte os valores para numericos
              for feature in ['cs_sexo', 'id_ocupa_n', 'dt_notific', 'dt_invest']:
                     le = LabelEncoder()
                     self.parametros[feature] = le.fit_transform(self.parametros[feature].astype(str))
              return

       def random_forest(self):
              '''
                     Initiate random foreste classifier
                     Return: RandomForestClassifier
              '''
              rf = RandomForestClassifier(n_estimators=256, max_depth=16)
              rf.fit(self.parametros, self.resultados.values.ravel())
              return rf

       def predict(self, patient):
              '''
                     Classi_fin: Mysql
              '''
              patient = patient[colunas]
              for feature in ['cs_sexo', 'id_ocupa_n', 'dt_notific', 'dt_invest']:
                     le = LabelEncoder()
                     patient[feature] = le.fit_transform(patient[feature].astype(str))
              result = {}
              rf = self.random_forest()
              Chagas_sem_threshold = str((rf.predict(patient) > 0)[0])
              Chagas_Probabilidade = rf.predict_proba(patient)[:, 1][0]
              Chagas_com_threshold = str(Chagas_Probabilidade >= self.threshold)
              result = {'Chagas_sem_threshold': Chagas_sem_threshold, 'Chagas_Probabilidade': Chagas_Probabilidade, 'Chagas_com_threshold': Chagas_com_threshold}
              return result

       def avalia_modelo(self, name, model, features, labels, threshold=None):
              start = time()
              if threshold != None:
                     pred = model.predict_proba(features)[:, 1]
                     pred = (pred >= threshold)
              else:
                     pred = model.predict(features)
              end = time()
              accuracy = round(accuracy_score(labels, pred), 3)
              precision = round(precision_score(labels, pred), 3)
              recall = round(recall_score(labels, pred), 3)
              print('Visao Geral:\n\t{} -- Accuracy: {} / Precision: {} / Recall: {} / Latency: {}ms'.format(name,
                                                                                                  accuracy,
                                                                                                  precision,
                                                                                                  recall,
                                                                                                  round((end - start)*1000, 1)))


# if __name__ == '__main__':
       # Chagas = Chagas()
       # val_parametros_final = pd.read_csv(r'C:\Users\dougl\Desktop\VSCode - Python\TCC\Dados2\Resultado\Datasets final\validacao_parametros_final.csv')
       # val_labels = pd.read_csv(r'C:\Users\dougl\Desktop\VSCode - Python\TCC\Dados2\Resultado\split_data\validacao_resultado.csv')
       # modelo_pkl = joblib.load(r'C:\Users\dougl\Desktop\VSCode - Python\TCC\Dados2\Resultado\Modelos\modelo_final_parametros.pkl')

       # import pandas as pd
       # import numpy as np
       # chagas = pd.read_excel(r'C:\Users\dougl\Desktop\VSCode - Python\TCC\Dados2\Resultado\CHAGAS-todos-limpa.xlsx')

       # colunas = ['DT_NOTIFIC_clean', 'SG_UF', 'ID_MN_RESI', 'CS_SEXO_clean', 'CS_GESTANT', 'CS_RACA_clean',
       #        'DT_INVEST', 'ID_OCUPA_N_clean', 'ANT_UF_1_clean', 'ANT_UF_2_clean', 'ANT_UF_3_clean', 'MUN_1_clean',
       #        'MUN_2_clean', 'MUN_3_clean', 'HISTORIA_clean', 'ASSINTOMA_clean', 'EDEMA_clean', 'MENINGOE_clean', 
       #        'POLIADENO_clean', 'FEBRE_clean', 'HEPATOME_clean', 'SINAIS_ICC_clean', 'ARRITMIAS_clean', 
       #        'ASTENIA_clean', 'ESPLENOM_clean', 'CHAGOMA_clean', 'EXAME_clean', 'XENODIAG_clean', 'CLASSI_FIN']
       # chagas = chagas[colunas]
       # dt_nasc = np.zeros(chagas.shape[0])
       # chagas['dt_nasc'] = dt_nasc
       # colunas.append('dt_nasc')

       # colunas2 = []
       # for item in colunas:
       #        item = item.lower()
       #        if '_clean' in item:
       #               colunas2.append(item.split('_clean')[0])
       #        else:
       #               colunas2.append(item)

       # chagas.columns = colunas2
       # chagas.to_excel(r'C:\Users\dougl\Desktop\VSCode - Python\TCC\Dados2\Resultado\CHAGAS-usar_essa.xlsx', index=False)

       # parametros = chagas[colunas]
       # resultados = chagas['CLASSI_FIN']
       # # X_train, X_test, y_train, y_test = train_test_split(parametros, resultados, test_size=0.3, random_state=42)
       
       # linha = 5977
       # paciente_1 = chagas.iloc[linha, :]
       # resultado_esperado = paciente_1['CLASSI_FIN']
       # paciente_1 = paciente_1[colunas]

       # rf = Chagas.random_forest()
       # resultado_obtido_excel = rf.predict([paciente_1])
       # print(f'Resultado obtido paciente 1 excel: {resultado_obtido_excel}')
       # Chagas.avalia_modelo('Excel', rf, parametros, resultados.values.ravel())
       # print('-'*50)

       # resultado_obtido_pkl = modelo_pkl.predict([paciente_1])
       # print(f'Resultado obtido paciente 1 pkl: {resultado_obtido_pkl}')
       # Chagas.avalia_modelo('Pkl', modelo_pkl, parametros, resultados.values.ravel())
       # print('-'*50)

       # threshold = 0.12
       # resultado_obtido_excel = rf.predict_proba([paciente_1])[:, 1]
       # resultado_obtido_excel = (resultado_obtido_excel >= threshold)
       # print(f'Resultado obtido excel c/ Threshold: {resultado_obtido_excel}')
       # Chagas.avalia_modelo('Excel', rf, parametros, resultados.values.ravel(), threshold=threshold)
       # print('-'*50)

       # resultado_obtido_pkl = modelo_pkl.predict_proba([paciente_1])[:, 1]
       # resultado_obtido_pkl = (resultado_obtido_pkl >= threshold)
       # Chagas.avalia_modelo('Pkl', modelo_pkl, parametros, resultados.values.ravel(), threshold=threshold)
       # print(f'Resultado obtido pkl c/ Threshold: {resultado_obtido_pkl}')
       # print('-'*50)

       # print(f'Resultado esperado: {resultado_esperado}')
       # print('-'*50)

       # resultado_obtido = modelo.predict_proba(val_parametros_final)[:, 1]
       # resultado_obtido = (resultado_obtido >= threshold).astype('int')
       # _, counts_obtidos = np.unique(resultado_obtido_pkl, return_counts=True)
       # _, counts_esperado = np.unique(val_labels, return_counts=True)
       # resultado_obtido[:, 0] = (resultado_obtido[:, 0] < threshold).astype('int')

       # print(resultado_obtido_pkl)
       # print('-'*30)
       # print('Prob Negativo {}'.format(resultado_obtido_pkl[:, 0]))
       # print('Prob Negativo Threshold {}'.format((resultado_obtido_pkl[:, 0] < threshold)))
       # print('-'*30)
       # print('Prob Positivo {}'.format(resultado_obtido_pkl[:, 1]))
       # print('Prob Positivo Threshold {}'.format((resultado_obtido_pkl[:, 1] >= threshold)))
       # print('-'*30)
       # print('Valor esperado {}'.format(resultado_esperado))
       # print('Valor obtido {}'.format(modelo.predict([paciente_1])))

       # SEED = 42
       # np.random.seed(SEED)
       # cv = StratifiedKFold(n_splits = 5, shuffle = True)
       # results = cross_val_score(modelo, val_parametros_final, val_labels.values.ravel(), cv=cv, scoring='recall')
       # # model = DecisionTreeClassifier(max_depth=3)
       # # results = cross_val_score(model, X_train, 
       # #                           y_train, cv = 5, scoring = 'accuracy')
       # def intervalo(results):
       #     mean = results.mean()
       #     dv = results.std()
       #     print('Acur??cia m??dia: {:.2f}%'.format(mean*100))
       #     print('Intervalo de acur??cia: [{:.2f}% ~ {:.2f}%]'
       #            .format((mean - 2*dv)*100, (mean + 2*dv)*100))
       # intervalo(results)