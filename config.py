import os
from crewai import LLM
from tavily import TavilyClient
from scrapegraph_py import Client
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

# Directory configuration
output_dir = "./ai-agent-output"
os.makedirs(output_dir, exist_ok=True)

# LLM configurations
# llama3_3_llm = LLM(
#     model="llama-3.3-70b",
#     base_url="https://models.mylab.th-luebeck.dev/v1",
#     api_key="dummy-api-key",
#     temperature=0,
# )

llama3_3_llm = LLM(
    model="gpt-4o",
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0)

gpt_4o_llm = LLM(
    model="gpt-4o",
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0)

# Client configurations
search_client = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))
scrape_client = Client(api_key=os.getenv('SCRAPEGRAPH_API_KEY'))

# Default parameters
no_keywords = 10
about_company = "Rankyx is a company that provides AI solutions to help websites refine their search and recommendation systems."
