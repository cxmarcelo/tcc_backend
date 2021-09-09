from app import db
from ..models.states import States
from ..models.counties import Counties
from ..models.occupation import Occupation
import pandas as pd


def aux_insert_state(state_id, name, initial):
    state = States(state_id, name, initial)

    try:
        db.session.add(state)
        db.session.commit()
        print("STATE " + initial + " INSERTED")
    except Exception as e:
        print(e)
        print("ERROR ON STATE: " + initial)


def aux_insert_county(county_id, name, uf_id):
    county = Counties(county_id, name, uf_id)

    try:
        db.session.add(county)
        db.session.commit()
        print("COUNTY " + name + " INSERTED")
    except Exception as e:
        print(e)
        print("ERROR " + name + " NOT INSERTED")


def aux_insert_occupation(occupation_id, name):
    occupation = Occupation(occupation_id, name)

    try:
        db.session.add(occupation)
        db.session.commit()
        print("COUNTY " + name + " INSERTED")
        return True
    except Exception as e:
        print(e)
        print("ERROR " + name + " NOT INSERTED")
        return False


"""
        "id": 11,
        "sigla": "RO",
        "nome": "Rondônia",
"""

def insert_data_estados():
    df = pd.read_json("C:/Users/Marcelo/Desktop/TCC/estados.json")
    df = df.drop("regiao", axis=1)
    df.columns = ["id", "initial", "name"];
    #print(df)
    for item in df.values:
        aux_insert_state(item[0], item[2], item[1])


def insert_data_municipios():
    df = pd.read_json("C:/Users/Marcelo/Desktop/TCC/municipios.json")

    for item in df.values:
        mun_id = str(item[0])[:-1]
        uf_id = str(item[0])[:2]
        aux_insert_county(mun_id, item[1], uf_id)


def insert_data_occupations():
    df = pd.read_excel("C:/Users/Marcelo/Desktop/TCC/ocupacao.xlsx")

    for item in df.values:
        if not aux_insert_occupation(item[0], item[1]):
            break

