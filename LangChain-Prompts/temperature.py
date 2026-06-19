from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# temperature is a parmeter passed to underlying LLM 
# it controls the randomness of the output. Higher temperature means more random & creative output, 
# while lower temperature means more deterministic output.
model = ChatOpenAI(model='gpt-5.4-nano-2026-03-17', temperature=1.5)

result = model.invoke("Write about indian history in 20 words")

print(result.content)



