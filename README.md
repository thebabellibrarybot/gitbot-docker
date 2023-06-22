# Dockerized Flask-React Application with MongoDB

![SVG Image](gitEnd/public/icon.svg)

# Hello I am GitBot !

This is a Docker application that consists of a Flask backend, a React frontend, and a MongoDB database. The application allows users to provide a GitHub repository URL, which is then vectorized using LangChain and DeepLake. This vectorized information is used to prompt the engineering of a chat-bot capable of retrieving and referencing files from the uploaded GitHub repository.

## Prerequisites

Before running this application, ensure that you have the following software installed on your system:

- Node.js 
- Python 
- Docker

## Setup

1. Clone the repository from GitHub: `git clone https://github.com/your-repo.git`
2. Navigate to the root directory of the cloned repository: `cd your-repo`
3. Create a `.env` file in the root directory of the Flask API backend `root/gitBot/.env`.
4. Open the `.env` file and add the following environment variables:

```plaintext
MONGODB_SECRET_KEY=your-mongodb-secret-key
DEEPLAKE_SECRET_KEY=your-deeplake-secret-key
OPENAI_SECRET_KEY=your-openai-secret-key
```

Replace `your-mongodb-secret-key`, `your-deeplake-secret-key`, and `your-openai-secret-key` with the respective secret keys for MongoDB, DeepLake, and OpenAI.

## Building and Running the Application

To run the application using Docker, follow these steps:

1. Open a terminal and navigate to the root directory of the cloned repository.
2. Build the Docker images for the backend and frontend:

```bash
docker-compose build
```

3. Once the images are built, start the Docker containers:

```bash
docker-compose up
```

This command will start the Flask backend, React frontend, and MongoDB database containers.

4. Once the containers are up and running, you can access the application in your web browser at `http://localhost:3000`.

## Alternative build

1. Spin up a mongoDB server with public uri

2. cd from root into `/gitBot`

    Run in terminal:

    -  `python -m venv mygitbotvenv`

    -  `cd mygitbotvenv`

    -  Ubuntu: `source mygitbotvenv/bin/activate`
       Windows: `cd mygitbotvenv && /Scripts/activate.bat`

    -  `pip install -r requirements.txt`

    -  `python app.py`

3. cd from root into `/gitEnd`

    Run in terminal:

    -  `npm install`

    -  `npm start`
    

## Usage

1. Open your web browser and navigate to `http://localhost:3000`.
2. On the application's homepage, you will see an input field where you can enter the GitHub repository URL.
3. Enter the URL and click the "Submit" button.
4. The application will vectorize the information using LangChain and DeepLake.
5. Once the vectorization process is complete, the chat-bot will be engineered using the vectorized data.
6. You can then interact with the chat-bot to retrieve and reference files from the uploaded GitHub repository.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make the necessary changes and commit them.
4. Push your changes to your forked repository: `git push origin feature-name`.
5. Submit a pull request on the original repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

- LangChain - [link to LangChain](https://langchain.ai)
- DeepLake - [link to DeepLake](https://deeplake.ai)
- OpenAI - [link to OpenAI](https://openai.com)

## Contact

If you have any questions or suggestions, feel free to contact the project maintainer at [jtucker0110@gmail.com](mailto:jtucker0110@gmail.com).