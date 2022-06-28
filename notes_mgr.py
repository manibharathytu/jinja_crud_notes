import pickle_db
# notes_data=[{'title': 'first note', 'body': 'this is my first note'},
#            {'title': 'second note',
#             'body': 'this is my second note'},
#            {'title': 'third note', 'body': 'this is my third note'}]

notes_data = pickle_db.read_from_pkl_db()
print(notes_data)


def get_notes_data():
    return notes_data


def notes_crud(req_msg):
    print(req_msg)
    if req_msg['op'] == 'add' or req_msg['op'] == 'update':
        print('entered')
        notes_data[req_msg['data']['id']] = {'title': req_msg['data']['title'], 'body': req_msg['data']['body']}
    if req_msg['op'] == 'delete':
        notes_data.pop(req_msg['data']['id'], None)
    pickle_db.save_to_pickle_db(notes_data)
    
