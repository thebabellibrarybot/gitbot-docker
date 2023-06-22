from flask import Blueprint, jsonify
from controllers.data_controller import get_data, create_data, get_single_data, update_data, delete_data

data_router = Blueprint('data_router', __name__, url_prefix='/repo')

@data_router.route('/', methods=['GET'])
async def get_all_data():
    try:
        data = await get_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@data_router.route('/', methods=['POST'])
async def create_new_data():
    try:
        data = await create_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@data_router.route('/<id>', methods=['GET'])
async def get_data_by_id(id):
    try:
        data = await get_single_data(id)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@data_router.route('/<id>', methods=['PUT'])
async def update_data_by_id(id):
    try:
        data = await update_data(id)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@data_router.route('/<id>', methods=['DELETE'])
async def delete_data_by_id(id):
    try:
        data = await delete_data(id)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
