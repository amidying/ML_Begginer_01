import json
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")
#--------------------------------------------------------------------------------------------------------------------------------
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >=0:
        x[loc_index] = 1
    
    return np.round(__model.predict([x]),2)
def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading Saved Artifacts...start")
    global __locations
    global __data_columns
    global __model

    with open("F:/Machine_Learning/16_projects/model_dump2/server/artifacts/columns.json","r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:] # the locations are from index 3

    with open("F:/Machine_Learning/16_projects/model_dump2/server/artifacts/banglore_home_prices_model.pickle","rb") as f:
        __model = pickle.load(f)

    print("Loading artifacts done...")  

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())

    print(get_estimated_price('1st phase jp nagar',1000,3,3))