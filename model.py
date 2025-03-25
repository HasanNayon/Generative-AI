from langchain.memory import ConversationBufferMemory
from langchain import LLMChain, PromptTemplate
from langchain_groq import ChatGroq
import os

# Set API Key (Replace with your actual API Key)
os.environ["GROQ_API_KEY"] = "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"

# Initialize memory
memory = ConversationBufferMemory(input_key="human_input", memory_key="chat_history")

# Initialize LLM
llm = ChatGroq(
    model_name="gemma2-9b-it",
    temperature=0.7
)

# Define Prompt
template = """
The following is a friendly conversation between a human and an AI. 
The AI is talkative and provides lots of specific details from its context. 
If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
{chat_history}
Human: {human_input}
AI:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)

# Initialize LLM Chain
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

# Function to get AI response
def get_response(user_input):
    return llm_chain.predict(human_input=user_input)
