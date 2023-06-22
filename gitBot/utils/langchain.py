from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA


class LangChain:

    def __init__(self, lang_obj):
        self.question = lang_obj['qa_data']
        self.db = lang_obj['db']
        #self.chat_history = lang_obj['chat_history']

    def retriever(self):
        # load repo from vectorDB
        db = self.db
        print(db, 'db for the retriever')
        retriever = db.as_retriever()
        retriever.search_kwargs['distance_metric'] = 'cos'
        retriever.search_kwargs['k'] = 20

        return retriever
    
    def retrieval_model(self):
        retriever = self.retriever()
        model = ChatOpenAI(model='gpt-3.5-turbo') # 'gpt-3.5-turbo',
        qa = RetrievalQA.from_chain_type(
            model, 
            chain_type="stuff", 
            retriever=retriever, 
            return_source_documents=True
            )

        return qa

"""
I also wanna make a sequential one of these with a prompt
I also wanna just make a custom langchain class for one of these...

"""

#TODO: make chat history, make retriever an active state that only changes when the user changes the db // vector path