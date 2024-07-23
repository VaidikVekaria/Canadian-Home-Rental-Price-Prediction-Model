import json
import pickle
import numpy as np

__type = None
__furnishing = None
__data_columns = None
__model = None

def get_furnishing_names():
    load_saved_artifacts()
    return __furnishing

def get_type_names():
    load_saved_artifacts()
    return __type

def load_saved_artifacts():

    print("loading saved artifacts...start")
    global __data_columns
    global __type
    global __furnishing
    global __model

    with open("Canada_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)

    with open("columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __furnishing = __data_columns[5:8]
        __type = __data_columns[8:]
    
    print("loading saved artifacts...complete")

def get_estimated_price(latitude, longitude, sq_feet, bedrooms, bathrooms, furnishing, type):
    load_saved_artifacts()
    try:
        loc_index_type = __data_columns.index(type.lower())
    except:
        loc_index_type = -1
    try: 
        loc_index_furnishing = __data_columns.index(furnishing.lower())
    except:
        loc_index_furnishing = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = latitude
    x[1] = longitude
    x[2] = sq_feet
    x[3] = bedrooms
    x[4] = bathrooms

    if loc_index_type >=0:
            x[loc_index_type] = 1

    if loc_index_furnishing >=0:
        x[loc_index_furnishing] = 1

    return round(__model.predict([x])[0], 2)

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_furnishing_names())
    print(get_type_names())
    print(get_estimated_price(53.444001,-113.5774373, 1100, 2,2.5,'Furnished','Townhouse'))