#generate a database
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import CommaSeparatedListOutputParser

load_dotenv()

model = OpenAI()

template_method = PromptTemplate.from_template("Responda apenas uma lista com as informações pedidas sem nenhum texto a mais.")
template_idiom = PromptTemplate.from_template("Os textos da sua resposta devem estar em {idiom}", partial_variables={"idiom": "spanish"})
template_course = PromptTemplate.from_template("""As informações que vai gerar devem ser voltadas a 
realidade do mercado de trabalho e serão usadas como exemplos em um curso de {course}"""
, partial_variables={"course": "python"})
template_msg = PromptTemplate.from_template("User message: : {message}")
template_final = (template_method + template_idiom + template_course + template_msg)

prompt = template_final.invoke({"message": "Gere uma base com 5 clientes, seus nomes e quantos produtos eles compraram"})

answer = model.invoke(prompt)
parser = CommaSeparatedListOutputParser()

answer = parser.invoke(answer)
print(answer)
print(parser.get_format_instructions)