from langchain.vectorstores import DeepLake
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
import subprocess
import os
from langchain.document_loaders import TextLoader
import shutil
import tempfile
import deeplake


class Repo_handler:

    def __init__(self, repo_obj):
        self.org_id = os.environ["ORG_ID"]
        self.repo_name = repo_obj['repo_name']
        self.repo_url = repo_obj['repo_url']
        self.embeddings = OpenAIEmbeddings()
        hub_space = os.environ['ORG_ID']
        repo_nm = repo_obj['repo_name']
        self.temp_dir = tempfile.TemporaryDirectory().name
        self.dataset_path = f"hub://{hub_space}/{repo_nm}"
        self.openai_api_key = os.environ['OPENAI_API_KEY']


    async def git_clone(self, repo_url):
        """
        Clones the given repo to a temporary directory.

        Args:
            repo_url: The url of the repo to clone.

        Returns:
            The path to the cloned repo.
        """
        temp_dir = self.temp_dir
        temp_dir_path = temp_dir

        if os.path.exists(temp_dir_path) and os.listdir(temp_dir_path):
            shutil.rmtree(temp_dir_path)

        command = ['git', 'clone', repo_url, temp_dir_path]
        subprocess.run(command, check=True)

        return os.listdir(temp_dir_path)

    def cleanup_directory(self, directory_path):
        """
        Deletes the given directory.

        Args:
            directory_path: The path to the directory to delete.
        """
        shutil.rmtree(directory_path)

    def repo_loader(self, repo_url):
        """
        Loads the repo from the tmp then deletes the tmp

        Args: 
            repo_url: The url of the repo to clone.
            temp_dir: The path to the cloned repo.
        returns: 
            docs: A list of documents from the repo.

            file_extensions = ['.py', '.js', '.tsx', 'Dockerfile', '.env', '.css', '.scss', '.html']

if any(file.endswith(ext) for ext in file_extensions):
    # File ends with one of the common programming file types
    # Do something...

        """
        docs = []
        for dirpath, dirnames, filenames in os.walk(self.temp_dir):
            print(dirpath, 'dirpath', dirnames, 'dirnames', filenames, 'filenames')
            file_extensions = ['.py', '.js', '.tsx', 'Dockerfile', '.env', '.css', '.scss', '.html']

            for file in filenames:
                if any(file.endswith(ext) for ext in file_extensions) and '/.venv/' not in dirpath:
                    try: 
                        loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
                        docs.extend(loader.load_and_split())
                    except Exception as e: 
                        pass
        print(docs, 'docs')
        return docs

    def text_splitter(self, docs):
        """
        Splits the repo into chunks of 1000 characters.
        param:
            repo_url: The url of the repo to clone.
        returns:
            texts: A list of texts from the repo.
        """
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(docs)
        return texts
    
    def add_repo_embedding(self):
        """
        Adds the given repo to a DeepLake vector store.

        Args:
            repo_name: The name of the repo.
        
        Returns:
            The path to the DeepLake vector store.
        
        """
        print(self.repo_url, 'repo_url')
        docs = self.repo_loader(self.repo_url)
        print(docs, 'docs post function')
        texts = self.text_splitter(docs)
        embeddings = OpenAIEmbeddings(openai_api_key=self.openai_api_key)
        vectorDB_path = self.dataset_path
        print('this is the dataset_path for the vector db', vectorDB_path)
        db = DeepLake.from_documents(texts, embeddings, dataset_path = vectorDB_path, token = os.environ['DEEPLAKE_API_KEY'])
        
        # this cleanup function causes an err on windows machines...
        #if (docs):
        #    self.cleanup_directory(self.temp_dir)
        #    print('deleted temp dir')
        

        return vectorDB_path

    def remove_repo_embedding(self):
        """
        Deletes the given repo from a DeepLake vector store.

        Args:
            repo_name: The name of the repo to delete.
        """
        print('removing')
        deeplake.delete(self.dataset_path, token = os.environ['DEEPLAKE_API_KEY'], force = True)
        print('removed')

    def get_repo_embedding(self, dataset_path):
        """
        Gets the embedding for the given repo.

        Args:
            dataset_path: The path to the DeepLake vector store for the repo.

        Returns:
            The embedding for the repo.
        """
        #embeddings = OpenAIEmbeddings()
        db = DeepLake(dataset_path = dataset_path, read_only = True, embedding_function = self.embeddings, token = os.environ['DEEPLAKE_API_KEY'])
        print(db, 'db', dataset_path, 'dataset_path')
        return db


    ## Check if embedding exists
    def check_embedding(self):
        """
        Checks if the given repo has an embedding.

        Args:
            repo_name: The name of the repo to check.

        Returns:
            True if the repo has an embedding, False otherwise.
        """
        db = self.get_repo_embedding(self.dataset_path)
        print(db, 'db')
        if db:
            return self.dataset_path
        else:
            pass