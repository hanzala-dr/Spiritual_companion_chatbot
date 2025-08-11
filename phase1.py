# import streamlit as st

# import os
# from langchain_groq import ChatGroq
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate


# st.title("Rag_chatbot")

# # setup session state variable to hold all the old messages
# if 'messages' not in st.session_state:
#     st.session_state.messages = []


# #Display all the historical messages 
# for message in st.session_state.messages:
#     st.chat_message(message['role']).markdown(message['content'])


# prompt = st.chat_input("pass your prompt here")

# if prompt:
#     st.chat_message("user").markdown(prompt)
#     st.session_state.messages.append({'role': 'user','content':prompt})


#     groq_sys_promp = ChatPromptTemplate.from_template("""You are very smart at Islamic knowledge, you always give the best,
#                                                       the most accurate and most precise answers. Answer the following
#                                                       Question: {user_promp}. Start the answer directly. No small talk please""")

#     model = "Llama3-8b-8192"
#     groq_chat = ChatGroq(
#         grop_api_key = os.environ.get("GROQ_API_KEY"),
#         model_name = model
#     )

#     chain = groq_sys_promp | groq_chat | StrOutputParser()
#     response = chain.invoke({"user_prompt":prompt})

#     # response = "I am your assistant"
#     st.chat_message("assistant").markdown(response)
#     st.session_state.messages.append({'role': 'assistant','content':response})


import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

st.title("Spiritual Companion")

# Setup session state variable to hold all the old messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display all the historical messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

prompt = st.chat_input("Pass your prompt here")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    # ✅ Consistent variable name: user_prompt
    groq_sys_promp = ChatPromptTemplate.from_template("""
        You are very smart at Islamic knowledge, you always give the best,
        the most accurate and most precise answers related to Islam. Answer the following
        Question: {user_prompt}. Start the answer directly. No lengthy talk please
    """)

    model = "Llama3-8b-8192"
    groq_chat = ChatGroq(
        groq_api_key=os.environ.get("GROQ_API_KEY"),  # ✅ Fixed key name
        model_name=model
    )

    chain = groq_sys_promp | groq_chat | StrOutputParser()
    response = chain.invoke({"user_prompt": prompt})  # ✅ Matches template

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({'role': 'assistant', 'content': response})
