reviews = ["Eu gostei bastante da câmera é a primeira vez que eu tiro foto com câmeras tirei algumas fotos não de pessoas no momento mas de algum objeto vou postar pra vocês verem",
           "Perfect!!! top de linha, vem com tudo que é descrito e ganhei um brinde maravilhoso. Verifiquei tudo, procedência etc etc. Tudo ok, não vão se arrepender!.",
           "Uma das melhores câmeras custo benefício para iniciantes da canon. Boa conectividade. Facilidade de aprender a mexer. Vale a pena pra quem não quer gastar muito mas quer ter câmera semi profissional.",
           "A apresentação da câmera é muito boa, mas preciso de uma câmera menor e mais compacta."]

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

class Avaliation(BaseModel):
    "Review foi enviado por um cliente que comprou um produto, preciso avaliar esse produto para saber se ele é bom e se vale a pena"
    review_positive: bool = Field(description="essa avaliação foi positiva ou negativa?")
    really_good: bool = Field(description="Essa avaliação diz que vale a pena ou não comprar o produto?")
    good_points: list[str] = Field(description="Quais os principais pontos positivos do produto? (cada ponto em no máximo 3 palavras, se houver)")
    bad_points: list[str] = Field(description="Quais os principais pontos negativos do produto? (cada ponto em no máximo 3 palavras, se houver)")

class ListAvaliation(BaseModel):
    avaliations: list[Avaliation]

parser = JsonOutputParser(name="user_avaliation", pydantic_object=ListAvaliation)
instruction = parser.get_format_instructions()
#print(instruction)

template_context = PromptTemplate.from_template("Você está avaliando reviews de vários usuários sobre um produto, preciso de algumas informações extraídas de cada review dessa lista de reviews: {reviews}")
template_idiom = PromptTemplate.from_template("Responda sempre em {idiom}", partial_variables={"idiom": "portuguese"})
template_format = PromptTemplate.from_template("Formato de resposta: {format}", partial_variables={"format": instruction})
template_final = (template_context + template_idiom + template_format)

model = ChatOpenAI()

prompt = template_final. invoke({"reviews": reviews})
answer = model.invoke(prompt)
answer = parser.invoke(answer)
print(answer)


