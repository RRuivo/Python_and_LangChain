from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

model = OpenAI()

template_prompt = PromptTemplate.from_template("""Responda ao usuário em no máximo {charact} caracteres, responda em {idiom}, indepnedente da língua que o usuário fizer a pergunta
Pergunta do usuário: {user_message}
""")

prompt = template_prompt.invoke({"charact": 140, "idiom": "spanish", "user_message": "Vale a pena fazer curso de python hoje em dia?"})

answer = model.invoke(prompt)
print(answer)