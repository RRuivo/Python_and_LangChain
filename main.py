reviews = ["Eu gostei bastante da câmera é a primeira vez que eu tiro foto com câmeras tirei algumas fotos não de pessoas no momento mas de algum objeto vou postar pra vocês verem",
           "Perfect!!! top de linha, vem com tudo que é descrito e ganhei um brinde maravilhoso. Verifiquei tudo, procedência etc etc. Tudo ok, não vão se arrepender!.",
           "Uma das melhores câmeras custo benefício para iniciantes da canon. Boa conectividade. Facilidade de aprender a mexer. Vale a pena pra quem não quer gastar muito mas quer ter câmera semi profissional.",
           "A apresentação da câmera é muito boa, mas preciso de uma câmera menor e mais compacta."]

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.runnables import RunnableLambda
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

chain = template_final | model | parser

#answer = chain.invoke({"reviews": reviews})



template_analyses = PromptTemplate.from_template("""
Analise a seguinte lista de reviews de um produto e me diga:
1. Quantas reviews são positivas e quantas são negativas (e o percentual de reviews positivas do total)
2. Qual percentual de reviews diz que vale a pena comprar o produto
3. O ponto positivo que mais aparece e o ponto negativo que mais aparece.
A lista de reviews é essa: {avaliations}
""")

parser_text = StrOutputParser()

chain_analyses = template_analyses | model |parser_text

def save_db(dic_avaliation):
    with open("reviews.txt", "w", encoding="utf-8") as file:
        for avaliation in dic_avaliation["avaliations"]:
            file.write(f"{avaliation}\n")
    return dic_avaliation

runnable_save_db = RunnableLambda(save_db)

global_chain = chain | runnable_save_db | chain_analyses

#answer_analyses = chain_analyses.invoke({"reviews_list": answer})
answer_analyses = global_chain.invoke({"reviews": reviews})

print(answer_analyses)


