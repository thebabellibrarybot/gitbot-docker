from flask import Blueprint, jsonify
from controllers.conversation_controller import create_data

conversation_router = Blueprint('conversation_router', __name__, url_prefix='/chat')


@conversation_router.route('/', methods=['POST'])
async def create_new_data():
    try:
        data = await create_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400