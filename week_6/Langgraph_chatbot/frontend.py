import streamlit as st
from Langgraph_chatbot.first_backend_code import chatbot
from langchain_core.messages import HumanMessage

# st.session_state -> dict ->



if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


# we are loading the coverstion history and all answer....
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input = st.chat_input('Type here')


if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role':'user','content':user_input})    
    with st.chat_message('user'):
        st.text(user_input) 

    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
    ai_message= response['messages'][-1].content
    #first add the message to message_history
    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)
