import os

import pandas as pd


disease_entity = pd.read_csv(os.path.join("../entity/disease_entity.csv")).values.tolist()
department_entity = pd.read_csv(os.path.join("../entity/department_entity.csv")).values.tolist()
ICD_10 = pd.read_csv(os.path.join("../entity/ICD-10.csv")).values.tolist()
DRUG_entity = open("../entity/drug.txt", encoding="utf-8").readlines()
