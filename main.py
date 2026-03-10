import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from tools import search_tool

load_dotenv()

# ---- Pydantic output model ----
class ResearchResponse(BaseModel):
    topic: str
    answer: str
    sources: list[str]
    tools_used: list[str]

# ---- LLM ----
llm = ChatOpenAI(
    model="arcee-ai/trinity-large-preview:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    max_tokens=2000  # ← ensure enough tokens for long responses
)

# ---- Parser ----
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# ---- Agent ----
tools = [search_tool]
agent = create_react_agent(llm, tools)

# ---- Run ----
query = input("Enter your research query: ")

system_msg = SystemMessage(content=(
    "You are a research assistant. Use the search tool when needed. "
    "You MUST always respond with a valid JSON object — no markdown, no code fences, no extra text. "
    "Keep your answer concise.\n"
    + parser.get_format_instructions()
))

response = agent.invoke({"messages": [system_msg, HumanMessage(content=query)]})

# ---- Debug: print raw response ----
final_text = response["messages"][-1].content
print("DEBUG raw response:", repr(final_text))  # ← shows what the model actually returned

# ---- Parse ----
if not final_text or not final_text.strip():
    print("ERROR: Model returned an empty response. Try a simpler query or different model.")
else:
    try:
        parsed = parser.parse(final_text)
        print(parsed)
    except Exception as e:
        print(f"Parsing failed: {e}")
        print("Raw output was:", final_text)