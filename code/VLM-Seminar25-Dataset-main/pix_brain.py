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

def ask_truellm(prompt):

    response = ollama.chat(
        model='llama3',
        messages=[{
            'role': 'user',
            'content': prompt
        }]
    )
    return response

def main():
    '''    #dir_name ='./chest_xrays'
    dir_name ='./nova_brain'
    directory = os.fsencode(dir_name+'/images')
    prompt = 'Please describe the given medical image.'
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
    with open("Brain1.json", "w") as json_file:
        json.dump(json_store, json_file)
    '''
    dir_name ='./nova_brain'
    directory = os.fsencode(dir_name+'/images')
    storage = {}
    with open('Brain1.json') as f:
        annotations = json.load(f)
        anno = json.loads(annotations)

        with open('./nova_brain/annotations.json') as f:
            annotations = json.load(f)
            for i in annotations:
                prompt = 'Based on the clinical history: ['+annotations[i]['clinical_history']
                prompt += '] provide your diagnosis for the disease.'
                #prompt = '"Please locate '+ j[4]+ ' and just output the corresponding bounding boxes as [x1,y1,x2,y2].'
                response = ask_truellm(prompt)
                storage[i] = response.message.content
                print(response.message.content)

    json_store = json.dumps(storage)
    with open("Brain3.json", "w") as json_file:
        json.dump(json_store, json_file)

if __name__ == "__main__":
    main()