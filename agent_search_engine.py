import os
from crewai import Agent, Task
from crewai.tools import tool
from pydantic import BaseModel, Field
from typing import List
from config import gpt_4o_llm, search_client, output_dir


class SignleSearchResult(BaseModel):
    title: str
    url: str = Field(..., title="the page url")
    content: str
    score: float
    search_query: str


class AllSearchResults(BaseModel):
    results: List[SignleSearchResult]


@tool
def search_engine_tool(query: str):
    """Useful for search-based queries. Use this to find current information about any query related pages using a search engine"""
    return search_client.search(query)


def create_search_engine_agent():
    agent = Agent(
        role="Search Engine Agent",
        goal="To search for products based on the suggested search query",
        backstory="The agent is designed to help in looking for products by searching for products based on the suggested search queries.",
        llm=gpt_4o_llm,
        verbose=True,
        tools=[search_engine_tool]
    )
    return agent


def create_search_engine_task(agent):
    task = Task(
        description="\n".join([
            "The task is to search for products based on the suggested search queries.",
            "You have to collect results from multiple search queries.",
            "Ignore any susbicious links or not an ecommerce single product website link.",
            "Ignore any search results with confidence score less than ({score_th}) .",
            "The search results will be used to compare prices of products from different websites.",
        ]),
        expected_output="A JSON object containing the search results.",
        output_json=AllSearchResults,
        output_file=os.path.join(output_dir, "step_2_search_results.json"),
        agent=agent
    )
    return task
