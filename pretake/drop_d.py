import pandas as pd
import os

base_path = "../data_family_doctor_v0302"
export_path = "../data_family_doctor"
if not os.path.exists(export_path):
    os.mkdir(export_path)
data_family_doctor = os.listdir(base_path)
for data_family_doctor in data_family_doctor:
    pd.read_csv(os.path.join(base_path, data_family_doctor)).drop_duplicates().to_csv(
        os.path.join(export_path, data_family_doctor), index=False)
