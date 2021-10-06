import joblib
from time import time
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from app.views import info_patient

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
              self.chagas = dataframe
              self.threshold = threshold
              return

       def random_forest(self):
              '''
              '''
              parametros = self.chagas[colunas]
              resultados = self.chagas['classi_fin']
              rf = RandomForestClassifier(n_estimators=256, max_depth=16)
              rf.fit(parametros, resultados.values.ravel())
              return rf

       def predict(self, patient):
              '''
                     Classi_fin: Mysql
              '''
              rf = self.random_forest()
              if self.threshold == False:
                     result = (rf.predict(patient) > 0)
              else:
                     result = rf.predict_proba(patient)[:, 1]
                     result = (result >= self.threshold)
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
       # chagas = pd.read_excel(r'C:\Users\dougl\Desktop\VSCode - Python\TCC\Dados2\Resultado\CHAGAS-final.xlsx')
       # chagas = pd.read_sql(sql, con)
       # chagas = info_patient.get_dataframe_info_patient()

       # colunas = ['DT_NOTIFIC_clean', 'SG_UF', 'ID_MN_RESI', 'CS_SEXO_clean', 'CS_GESTANT', 'CS_RACA_clean',
       #        'DT_INVEST', 'ID_OCUPA_N_clean', 'ANT_UF_1_clean', 'ANT_UF_2_clean', 'ANT_UF_3_clean', 'MUN_1_clean',
       #        'MUN_2_clean', 'MUN_3_clean', 'HISTORIA_clean', 'ASSINTOMA_clean', 'EDEMA_clean', 'MENINGOE_clean', 
       #        'POLIADENO_clean', 'FEBRE_clean', 'HEPATOME_clean', 'SINAIS_ICC_clean', 'ARRITMIAS_clean', 
       #        'ASTENIA_clean', 'ESPLENOM_clean', 'CHAGOMA_clean', 'EXAME_clean', 'XENODIAG_clean']

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
       #     print('Acurácia média: {:.2f}%'.format(mean*100))
       #     print('Intervalo de acurácia: [{:.2f}% ~ {:.2f}%]'
       #            .format((mean - 2*dv)*100, (mean + 2*dv)*100))
       # intervalo(results)