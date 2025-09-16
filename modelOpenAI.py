from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage("Responda as perguntas de forma curta, mas use até 140 caracteres")
]

model = ChatOpenAI()

if __name__ =="__main__":
    human_message = input("Digit your message: ")

    messages.append(HumanMessage(human_message))

    answer = model.invoke(messages)
    print(answer)
    print(type(answer))
    print(answer.content)
    print(answer.type)