from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import torch

torch.classes.__path__ = []

load_dotenv()

messages = [
    SystemMessage("Responda as perguntas de forma curta, mas use até 140 caracteres")
]

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/Deepseek-R1-Distill-Qwen-32B")
model = ChatHuggingFace(llm=llm)

if __name__ =="__main__":
    human_message = input("Digit your message: ")

    messages.append(HumanMessage(human_message))

    answer = model.invoke(messages)
    print(answer)
    print(type(answer))
    print(answer.content)
    print(answer.type)