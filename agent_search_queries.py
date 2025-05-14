import os
from crewai import Agent, Task
from pydantic import BaseModel, Field
from typing import List
from config import llama3_3_llm, output_dir, no_keywords


class SuggestedSearchQueries(BaseModel):
    queries: List[str] = Field(..., title="Suggested search queries to be passed to the search engine",
                               min_items=1, max_items=no_keywords)


def create_search_queries_agent():
    agent = Agent(
        role="Search Queries Recommendation Agent",
        goal="\n".join([
            "To provide a list of suggested search queries to be passed to the search engine.",
            "The queries must be varied and looking for specific items."
        ]),
        backstory="The agent is designed to help in looking for products by providing a list of suggested search queries to be passed to the search engine based on the context provided.",
        llm=llama3_3_llm,
        verbose=True,
    )
    return agent


def create_search_queries_task(agent):
    task = Task(
        description="\n".join([
            "Rankyx is looking to buy {product_name} at the best prices (value for a price strategy)",
            "The campany target any of these websites to buy from: {websites_list}",
            "The company wants to reach all available proucts on the internet to be compared later in another stage.",
            "The stores must sell the product in {country_name}",
            "Generate at maximum {no_keywords} queries.",
            "The search keywords must be in {language} language.",
            "Search keywords must contains specific brands, types or technologies. Avoid general keywords.",
            "The search query must reach an ecommerce webpage for product, and not a blog or listing page."
        ]),
        expected_output="A JSON object containing a list of suggested search queries.",
        output_json=SuggestedSearchQueries,
        output_file=os.path.join(output_dir, "step_1_suggested_search_queries.json"),
        agent=agent
    )
    return task
