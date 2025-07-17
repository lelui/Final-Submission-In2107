import ollama
import os
import json
def ask_truellm(prompt):

    response = ollama.chat(
        model='llama3',
        messages=[{
            'role': 'user',
            'content': prompt
        }]
    )
    return response
'''dir_name = './nova_brain'
storage = {}
with open('Brain1.json') as f:
    annotations2 = json.load(f)
    anno = json.loads(annotations2)

    with open('./nova_brain/annotations.json') as f:
        annotations = json.load(f)
        for i in annotations:
            for j in annotations[i]['image_findings']:
                prompt = 'Given the ground truth sentence and predicted sentence, in one word determine whether it is correct or not. ground truth:' + annotations[i]['final_diagnosis'] +'predicted sentence: ' + anno[j]
                response = ask_truellm(prompt)
                storage[i + '_' + j[4]] = response.message.content
                print(response.message.content)

json_store = json.dumps(storage)
with open("Brain1Eval.json", "w") as json_file:
    json.dump(json_store, json_file)'''
dir_name = './nova_brain'
storage = {}
with open('Brain2.json') as f:
    annotations2 = json.load(f)
    anno = json.loads(annotations2)

    with open('./nova_brain/annotations.json') as f:
        annotations = json.load(f)
        for i in annotations:
            key=i+'_0'
            prompt = 'Given the ground truth sentence and predicted sentence, in one word determine whether it is correct or not. ground truth:' + annotations[i]['final_diagnosis'] +'predicted sentence: ' + anno[key]
            response = ask_truellm(prompt)
            storage[i] = response.message.content
            print(response.message.content)

json_store = json.dumps(storage)
with open("Brain2Eval.json", "w") as json_file:
    json.dump(json_store, json_file)
