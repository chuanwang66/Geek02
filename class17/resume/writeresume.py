from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import UnstructuredWordDocumentLoader

from llm import DeepSeekR1
from prompt import ResumePrompt,ResumePrompt2

# 加载 职位描述
def load_jobs() -> str:
    with open(f'./job.txt', 'r', encoding='utf-8') as f:
        jobs=f.read()
    
    return jobs

def load_doc() -> list:
    word=UnstructuredWordDocumentLoader('E:\\AI\\个人简历.docx')
    docs=word.load()

    return docs

def write_resume():
    prompt=PromptTemplate.from_template(ResumePrompt)
    llm=DeepSeekR1()
    chain={
        "input":RunnablePassthrough()
    } | prompt | llm | StrOutputParser()
    ret=chain.invoke(load_jobs())
    print(ret)

def fix_resume():
    prompt=PromptTemplate.from_template(ResumePrompt2)
    llm=DeepSeekR1()
    docs=load_doc()
    chain={
        "resume": lambda _: docs,
        "input":RunnablePassthrough()
    } | prompt | llm | StrOutputParser()
    ret=chain.invoke(load_jobs())
    print(ret)

if __name__ == '__main__':
    fix_resume()