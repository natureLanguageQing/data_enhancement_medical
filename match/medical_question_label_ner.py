import json
import os

import pandas as pd

from match import ICD_10, department_entity, disease_entity, DRUG_entity


def index_of_str(s1, s2, label):
    s2 = s2.rstrip("\n")
    global dex
    dex = 0
    index = []
    lt = s1.split(s2)
    num = len(lt)
    for i in range(num - 1):
        dex += len(lt[i])
        index.append([dex, len(s2) + dex, label])
        dex += len(s2)
    return index


def medical_ner(path):

    medical_questions = pd.read_csv(path).drop_duplicates().values.tolist()
    fp = open('../ner_data/question_entity_five_labels.json', 'w', newline='', encoding='utf-8')

    if isinstance(medical_questions, list):

        for medical_question in medical_questions:
            if isinstance(medical_question, list):

                for medical_message in medical_question:
                    label_indexs = []
                    for i in ICD_10:

                        if len(i[0]) > 2:
                            if isinstance(medical_message, str):
                                if i[0] in medical_message:
                                    label_index = index_of_str(medical_message, i[0], "ICD_10")
                                    if len(label_index) >= 1:
                                        label_indexs.extend(label_index)
                    for i in department_entity:
                        if len(i[0]) > 2:
                            if isinstance(medical_message, str):
                                if i[0] in medical_message:
                                    label_index = index_of_str(medical_message, i[0], "department_entity")
                                    if len(label_index) >= 1:
                                        label_indexs.extend(label_index)
                    for i in disease_entity:
                        if len(i[0]) > 2:
                            if isinstance(medical_message, str):
                                if i[0] in medical_message:
                                    label_index = index_of_str(medical_message, i[0], "disease_entity")
                                    if len(label_index) >= 1:
                                        label_indexs.extend(label_index)
                    for i in DRUG_entity:
                        if len(i[0].strip()) > 2:
                            if isinstance(medical_message, str):
                                if i[0].strip() in medical_message:
                                    label_index = index_of_str(medical_message, i[0].strip(), "DRUG_entity")
                                    if len(label_index) >= 1:
                                        label_indexs.extend(label_index)
                    if len(label_indexs) > 2 and len(medical_message) > 10:
                        entity_dict_label = {"text": medical_message, "labels": label_indexs}
                        entity_dict_label = json.dumps(entity_dict_label, ensure_ascii=False)

                        fp.write(entity_dict_label + "\n")


if __name__ == '__main__':
    medical_ner("../ner_data/all.csv")
