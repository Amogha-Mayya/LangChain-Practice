from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'Give me a tweet on {topic}',
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template = 'Give me a linked in post on {topic}',
    input_variables=["topic"],
)

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'linkedin': RunnableSequence(prompt2,model,parser)
})

result = parallel_chain.invoke({"topic":"AI"})
print(result)