import pandas as pd
import os

export_path = "../data_family_doctor"
if not os.path.exists(export_path):
    os.mkdir(export_path)
data_family_doctor = os.listdir(export_path)
data_family_export = []
for data_family_doctor in data_family_doctor:
    for data_family in pd.read_csv(os.path.join(export_path, data_family_doctor)).values.tolist():
        data_family.append(data_family_doctor)
        data_family_export.append(data_family)
pd.DataFrame(data_family_export).drop_duplicates().to_csv("../cls_data/all.csv")
print(pd.DataFrame(data_family_export).count())
