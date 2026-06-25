from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-5.5', temperature=1.5)

result = model.invoke("Who is the current captain of RCB ?")

print(result.content)