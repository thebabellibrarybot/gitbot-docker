from flask import Flask
from routers.data_router import data_router
from routers.conversation_router import conversation_router
from middleware.middleware_controller import middleware_handler
from middleware.middleware_controller import start_timer, stop_timer
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

# Register the data_router blueprint: repo_handler
app.register_blueprint(data_router)

# Register the data_router blueprint: conversation
app.register_blueprint(conversation_router)


if __name__ == '__main__':
    app.run(debug=True)