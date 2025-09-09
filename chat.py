import streamlit as st
from modelOpenAI import model, messages
from langchain_core.messages import HumanMessage

def open_chat(prompt, model, messages):
    if "messages" in st.session_state:
        messages = st.session_state["messages"]
    else:
        st.session_state["messages"] = messages
    if prompt:
        messages.append(HumanMessage(prompt))
        answer = model.invoke(messages)
        messages.append(answer)
    for message in messages:
        if message.type != "system":
            with st.chat_message(message.type):
                st.write(message.content)

def my_app():
    st.header("Ruivo GPT", divider=True)
    st.markdown("#### Chat with Ruivo GPT integrated on Streamlit.")
    prompt = st.chat_input("Digit your message: ")
    open_chat(prompt, model, messages)


my_app()