from flask import request
import json
from utils.vectorDB import Repo_handler
from config.mongo_config import repo_db

# Your logic for handling data operations goes here
async def get_data():
    repos = []
    for repo in repo_db.find():
        print(repo['repo_name'], repo['repo_url'])
        repos.append(repo['repo_name'])
    return repos

"""
This function is used to create new repo
param: req.body {'repo': 'repo_name',
                 'repo_url': 'true/false'}
build: repo_obj = {
    'repo': 'repo_name',
    'repo_url': 'true/false',
    'repo_vector': 'vector'
}
return: {'message': 'Data created successfully'}
"""
async def create_data():
    """Creates new data from the request body."""
    try:
        # set data
        print('create_data')
        data = request.data
        print(data, 'request.data')
        data_dict = json.loads(data)
        repo = data_dict['repo_name']
        repo_url = data_dict['repo_url']
        req_data = {'repo_name': repo, 'repo_url': repo_url}
        print(req_data, 'req_data')

        # Create a new data model object
        repo_handler = Repo_handler(req_data)
        print(repo_handler, 'repo_handler')
        # this check_embedding function is not really working
        #db = repo_handler.check_embedding()
        #if db:
        #    repo_db.insert_one(req_data)
        #    return {'message': 'Data already exists', 'repo_name': repo, 'vector_url': db}
        
        #else:
        #    print('repo does not exist')
        repo_path = await repo_handler.git_clone(repo_url)
        print(repo_path, 'repo_path currently unused')
        vectorDB_path = repo_handler.add_repo_embedding()

        repo_db.insert_one(req_data)
       
        return {'message': 'Data created successfully', 'data': repo, 'vector': vectorDB_path}
    except Exception as e:
        # Handle any exceptions or errors
        return {'error from data_controller createdata': str(e)}, 400   

# only checks mongoDB
async def get_single_data(id):
    # Your logic to fetch a single data item based on the ID goes here
    print(id, 'id')
    repos = repo_db.find({"repo_name": id})
    print(repos, 'repos')
    
    # Convert the cursor object to a list of objects
    repo_list = list(repos)
    print(repo_list, 'repo_list')
    obj = repo_list[0]
    obj['_id'] = str(obj['_id'])

    return obj

async def update_data(id):
    # Your logic to update a data item based on the ID goes here
    
    data = {'message': 'Data is never updated with this simple model successfully'}
    return data

async def delete_data(id):
    # Your logic to delete a data item based on the mongoDB ID goes here

        # TODO: add an issue to deeplake where aws cred are overridding the deeplake cred

    data = repo_db.delete_many({'repo_name': id})
    req_data = {'repo_name': id, 'repo_url': 'false'}

    # your logic to delete a data item based on the deeplake ID goes here
    repo_handler = Repo_handler(req_data)
    repo_handler.remove_repo_embedding()



    return {'message': 'Data Deleted successfully'}
