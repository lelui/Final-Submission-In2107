from itertools import count

import ollama
import os
import json
from click import prompt


#from scripts import evaluate_metrics, calculate_map

def ask_llm(prompt, imgpath):

    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': prompt,
            'images': [imgpath]
        }]
    )
    return response

def main():
    '''    dir_name ='./chest_xrays'
    #dir_name ='./nova_brain'
    directory = os.fsencode(dir_name+'/images')
    prompt = 'Given the medical image, classify it as "healthy" or "unhealthy", in one word'
    storage = {}
    count=0
    for file in os.listdir(directory):
        count+=1
        print(count)
        file_na = file.decode("utf-8")
        dir_na = directory.decode("utf-8")
        response = ask_llm(prompt, dir_na +'/'+ file_na)
        storage[file_na] = response.message.content

    json_store = json.dumps(storage)
    with open("Chest2.json", "w") as json_file:
        json.dump(json_store, json_file)
    '''
    '''    dir_name ='./chest_xrays'
    #dir_name ='./nova_brain'
    directory = os.fsencode(dir_name+'/images')
    storage = {}

    with open('./chest_xrays/annotations_len_50.json') as f:
        annotations = json.load(f)
        for i in annotations:
            for j in annotations[i]['bbox_2d']:


                prompt = '"Please locate '+ j[4]+ ' and just output the corresponding bounding boxes'
                response = ask_llm(prompt, './chest_xrays/images/'+i+'.png')
                storage[i+'_'+j[4]] = response.message.content
                print(response.message.content)

    json_store = json.dumps(storage)
    with open("ChestBB.json", "w") as json_file:
        json.dump(json_store, json_file)'''

if __name__ == "__main__":
    main()
