from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

model = OpenAI()

#template_prompt = PromptTemplate.from_template("""Responda ao usuário em no máximo {charact} caracteres, responda em {idiom}, indepnedente da língua que o usuário fizer a pergunta
#Pergunta do usuário: {user_message}
#""", partial_variables={"charact": 140, "idiom": "spanish"})

template_form = PromptTemplate.from_template("Responda ao usuário de forma educada, porém informal, como se fosse um amigo falando com ele.")
template_charac = PromptTemplate.from_template("Sua resposta deve sempre ter no máximo {charac} caracteres.", partial_variables={"charac": 140})
template_idiom = PromptTemplate.from_template("Responda em {idiom} indiferente da língua que a pergunta for feita.", partial_variables={"idiom": "spanish"})
template_msg = PromptTemplate.from_template("User message: : {message}")
template_final = (template_form + template_charac + template_idiom + template_msg)


prompt = template_final.invoke({"message": "Vale a pena fazer curso de python hoje em dia?"})
print(prompt)

answer = model.invoke(prompt)
print(answer)