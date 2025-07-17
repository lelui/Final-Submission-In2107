import ollama
import os
import json

from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
import numpy as np

#Brain1 3/25
#Brain2 11/25
'''with open('Chest2.json') as f:
    annotations = json.load(f)
    anno = json.loads(annotations)
    di = annotations
    for i in anno:
        print(anno[i])
'''
with open('./chest_xrays/annotations_len_50.json') as f:
    annotations = json.load(f)
    liste_gt=[]
    liste_pred=[]

    for i in annotations:
        liste_gt.append(annotations[i]['status'])
    print(liste_gt)
    for i in range(50):
        liste_pred.append('unhealthy')
accuracy = accuracy_score(liste_gt, liste_pred)
f1 = f1_score(liste_gt, liste_pred, pos_label='unhealthy')
recall = recall_score(liste_gt, liste_pred, pos_label='unhealthy')
prec = precision_score(liste_gt, liste_pred, pos_label='unhealthy')

# Print results
print(f"Ground Truth: {liste_gt}")
print(f"Predictions: {liste_pred}")
print(f"Accuracy: {accuracy:.3f}")
print(f"F1 Score: {f1:.3f}")
print(f"Recall Score: {recall:.3f}")
print(f"prec Score: {prec:.3f}")



