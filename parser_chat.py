from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

template_chat = ChatPromptTemplate([
    SystemMessage("Responda o usuário sempre em {idiom} indenpendente do idioma que ele escrever")
], partial_variables={"idiom": "english"})

user_text = input("Digit your message: ")

user_message = HumanMessage(user_text)
template_chat.append(user_message)

prompt = template_chat.invoke({})
answer = model.invoke(prompt)
parser = StrOutputParser()
answer = parser.invoke(answer)

print(answer)
