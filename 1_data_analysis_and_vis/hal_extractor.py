import requests
from requests.exceptions import HTTPError
import csv
import json
import os
import glob
import datetime
import tqdm
import s3fs

# fonction pour extraire une liste d'identifiant hal

def get_list_idhal(path_file, column, is_local=True):
    list_idhal = []
    if is_local == True:
        with open(path_file, newline='') as csvfile:
        
            reader = csv.DictReader(csvfile)
        
            for row in reader:
                if row[column] != '':
                    split_id = row[column].split('|')
                    list_id = [x for x in split_id]
                    for y in list_id:
                        if y not in list_idhal:
                            list_idhal.append(y)
                        else:
                            pass
                else:
                    pass
    else:
        S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
        fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': S3_ENDPOINT_URL})

        with fs.open(path_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['authhalid_i'] != '':
                    split_id = row['authhalid_i'].split('|')
                    list_id = [x for x in split_id]
                    for y in list_id:
                        if y not in list_idhal:
                            list_idhal.append(y)
                        else:
                            pass
                else:
                    pass
    print("nombre d'identifiant : ", len(list_idhal))

    return list_idhal

def try_get_answer(url_api_search, params):

    try:
        response = requests.get(url_api_search, params)
        return response    
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}.")
    else:
        print(response.json())



def create_folder(ref, year):
    path_folder = f"../Data/raw/{ref}/{year}"
    if os.path.exists(path_folder):
        files = glob.glob(f"{path_folder}/hal_*.csv")
        for f in files:
            os.remove(f)
    # Si le dossier n'existent pas, il est créé
    else:
        os.makedirs(path_folder)
    return path_folder

    

    

def process_json_to_csv(response, params, ref, path_folder):
    files = glob.glob(f"{path_folder}/hal_{ref}*.csv")
    header_csv = params["fl"].split(",")

    if len(files)> 0:
        name_file = files[0]
        
    else:
        name_file = f"{path_folder}/hal_{ref}.csv"
        with open(name_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header_csv)
            writer.writeheader()

    
    for x in response['response']['docs']:
        row = {}
        for column in header_csv:
            if column in x.keys():
                #print(type(x[column]))
                if type(x[column]) is list:
                    row[column] = "|".join([str(y) for y in x[column]])
                else:
                    row[column] = x[column]
            else:
                row[column] = None
        with open(name_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header_csv)
            writer.writerow(row)
        

    
    