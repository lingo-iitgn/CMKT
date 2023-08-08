# Code Mixed Text Toolkit
"""
Language specific toolkits for searching, loading and running models for different NLP tasks.
"""

from cmkt.tasks.LID import *
from cmkt.tasks.NER import *
from cmkt.tasks.POS import *
from cmkt.tasks.sentiment import *
from cmkt.tasks.hatespeech import *
from cmkt.tasks.humor import *
from cmkt.tasks.translation import *
import os 
import json
from tabulate import tabulate
path = os.path.dirname(os.path.realpath(__file__))
tasks_file_path = os.path.join(path, "tasks.json")

# write all languages in small letters
SUPPORTED_LANGUAGES = ['hineng']


class TaskToolKit:
    '''Provides model filtering functions based on tasks and languages'''
    def __init__(self, lang, tasks_file = tasks_file_path):
        self.lang = lang
        self.tasks = self.load_tasks(tasks_file)
        if lang.lower() not in SUPPORTED_LANGUAGES:
            raise ValueError(f"{self.lang} language not supported for TaskToolKit")

    def load_tasks(self, task_file):
        '''
        Returns the list of all the tasks provided by cmtt library
        :param task_file: path of tasks.json file
        :type key: str
        :return: list of dictionaries with info about all the tasks. 
        :rtype: list 
        '''
        f = open(task_file)
        data = json.load(f)
        tasks = data["tasks"]
        f.close()
        return tasks # list of all the dictionaries in tasks

    def list_tasks(self, task_type=''):
        '''
        Returns the list of tasks under a particular task type 
        :param key: task_type (task types available: "Syntactic", "Semantic", "Generational")
        :type key: str
        :return: list of tasks available
        :rtype: list
        '''
        task_list = []
        for i in self.tasks:
            if self.lang in i['language'] and i['task_type'].lower() == task_type.lower():
                task_list.append(i['task'])
        if len(task_list)==0:
            return f"No tasks found in task type {task_type}"
        return task_list
    
    
    def model_info_file(self, task):
        model_file = ""
        for i in self.tasks:
            if self.lang in i['language'] and i['task'].lower() == task.lower():
                model_file = i['model_info']
                break
        if model_file == "":
            return None
        model_info_path = os.path.join(path, model_file)
        f = open(model_info_path)
        data = json.load(f)
        list_of_dic = data["model"]
        f.close()
        return list_of_dic # list of dictionaries in model info 
    
    def task_model_info(self, task='', details=False):
        '''
        Returns the information about available models for the given task.
        :param key: task (for e.g. "lid", "pos" etc)
        :type key: str
        :param details: to specify whether to fetch complete info table or just names of models.
        :type details: bool
        :return: list or table of all the available models for the given task
        :rtype: list (if details = False) or str (if details = True)
        '''

        model_info = self.model_info_file(task)
        if model_info == None:
            return f"No models found for task {task}"
        
        headers = model_info[0].keys()
        rows = []
        model_list = []
        for i in model_info:
            if self.lang == i["language"] and i["task"].lower() == task.lower():
                if details:
                    rows.append(i.values())
                else:
                    model_list.append(i["Model name"])

        if details:
            table = tabulate(rows, headers=headers, tablefmt="grid")
            return table   
        return model_list
    
    def lid(self, model_name: str):
        model_info = self.model_info_file("lid")
        if model_info == None:
            print(f"Task not available for {self.lang} language")
            return
        for models in model_info:
            if model_name.lower() in models["Model name"].lower() and self.lang in models['language']:
                model_class = globals()[models['Invoke By']] # type: ignore
                model = model_class()
                break
            else:
                print(f"{model_name} model not found for LID in {self.lang} language")
                return                                                
        return model
    
    def ner(self, model_name: str):
        model_info = self.model_info_file("ner")
        if model_info == None:
            print(f"Task not available for {self.lang} language")
            return
        for models in model_info:
            if model_name.lower() in models["Model name"].lower() and self.lang in models['language']:
                model_class = globals()[models['Invoke By']] # type: ignore
                model = model_class()
                break
            else:
                print(f"{model_name} model not found for NER in {self.lang} language")
                return                                                
        return model

    def pos(self, model_name: str):
        model_info = self.model_info_file("pos")
        if model_info == None:
            print(f"Task not available for {self.lang} language")
            return
        for models in model_info:
            if model_name.lower() in models["Model name"].lower() and self.lang in models['language']:
                model_class = globals()[models['Invoke By']] # type: ignore
                model = model_class()
                break
            else:
                print(f"{model_name} model not found for POS in {self.lang} language")
                return                                                
        return model
    
    def sentiment(self, model_name: str):
        model_info = self.model_info_file("sentiment analysis")
        if model_info == None:
            print(f"Task not available for {self.lang} language")
            return
        
        for models in model_info:
            if model_name.lower() in models["Model name"].lower() and self.lang in models['language']:
                model_class = globals()[models['Invoke By']] # type: ignore
                model = model_class()
                break
            else:
                print(f"{model_name} model not found for sentiment analysis in {self.lang} language")
                return                                                
        return model
    
    def hatespeech(self, model_name: str):
        model_info = self.model_info_file("hate speech detection")
        if model_info == None:
            print(f"Task not available for {self.lang} language")
            return
        
        for models in model_info:
            if model_name.lower() in models["Model name"].lower() and self.lang in models['language']:
                model_class = globals()[models['Invoke By']] # type: ignore
                model = model_class()
                break
            else:
                print(f"{model_name} model not found for hatespeech detection in {self.lang} language")
                return                                                
        return model
    
    def humordetection(self, model_name: str):
        model_info = self.model_info_file("humor detection")
        if model_info == None:
            print(f"Task not available for {self.lang} language")
            return
        
        for models in model_info:
            if model_name.lower() in models["Model name"].lower() and self.lang in models['language']:
                model_class = globals()[models['Invoke By']] # type: ignore
                model = model_class()
                break
            else:
                print(f"{model_name} model not found for humor detection in {self.lang} language")
                return                                                
        return model
    
    def translation(self, model_name: str):
        model_info = self.model_info_file("machine translation")
        if model_info == None:
            print(f"Task not available for {self.lang} language")
            return
        
        for models in model_info:
            if model_name.lower() in models["Model name"].lower() and self.lang in models['language']:
                model_class = globals()[models['Invoke By']] # type: ignore
                model = model_class()
                break
            else:
                print(f"{model_name} model not found for translation in {self.lang} language")
                return                                                
        return model


        



  
    


        

    



