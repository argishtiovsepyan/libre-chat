from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext, StorageContext, load_index_from_storage
from langchain.chat_models import ChatOpenAI
import gradio
import os
from credentials import API_KEY

os.environ["OPENAI_API_KEY"] = API_KEY

def construct_index(directory_path):

    num_outputs = 256

    _llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

    service_context = ServiceContext.from_defaults(llm_predictor=_llm_predictor)

    docs = SimpleDirectoryReader(directory_path).load_data()

    index = GPTVectorStoreIndex.from_documents(docs, service_context=service_context)
    
    # directory for index storage
    index.storage_context.persist(persist_dir="indexes")

    return index

def chatbot(input_text):
    
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="indexes")
    
    # load indexes from directory using storage_context 
    query_engne = load_index_from_storage(storage_context).as_query_engine()
    
    response = query_engne.query(input_text)
    
    #returning the response
    return response.response

#Creating web UI
iface = gradio.Interface(fn=chatbot,
                     inputs=gradio.Textbox(lines=5, label="Enter your question here"),
                     outputs="text",
                     title="Libre AI Chatbot")

#Constructing indexes based on the documents in traininData folder
# index = construct_index("trainingData")

iface.launch(share=True)