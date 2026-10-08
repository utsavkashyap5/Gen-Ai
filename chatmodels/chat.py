from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  
history = [
    SystemMessage(content="You are a funny assistant that is very sarcastic and witty."),
]
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.6,
    
)
print("-----------------------Funny Chat Bot------------------------")
print("Type 'exit' to quit the chat.")
while True:
    
    
    prompt = input("User:-")
    
    if(prompt.lower() == "exit"):
        break
        
    history.append(HumanMessage(content=prompt))
    response=llm.invoke(history)

    #Ai message
    aiResponse = history.append(
            AIMessage(content=response.content)
        )
    print("AI:-",response.content)