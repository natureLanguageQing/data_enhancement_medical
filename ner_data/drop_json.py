import os

question_entity_six_labels = open(os.path.join("question_entity_six_labels.json"), "r", encoding="utf-8").readlines()
question_entity_six_labels = list(set(question_entity_six_labels))
question_entity_four_labels = open(os.path.join("question_entity_four_labels.json"), "w", encoding="utf-8")
for i in question_entity_six_labels:
    question_entity_four_labels.writelines(i)
