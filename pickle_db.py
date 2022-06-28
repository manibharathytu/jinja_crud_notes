import pickle


def read_from_pkl_db():
    global notes_data
    try:
        pickle_off = open("datafile.pkl", "rb")
        return pickle.load(pickle_off)
    except :
        return {}
        

def save_to_pickle_db(notes_data):
    with open('datafile.pkl', 'wb') as fh:
        pickle.dump(notes_data, fh)
