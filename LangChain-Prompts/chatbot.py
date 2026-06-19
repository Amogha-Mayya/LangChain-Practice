from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-nano-2026-03-17')
chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if(user_input == "exit"):
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("GPT: ",result.content)
print(chat_history)
