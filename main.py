import os
from dotenv import load_dotenv
from crewai import Crew, Process
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

from config import about_company
from agent_search_queries import create_search_queries_agent, create_search_queries_task
from agent_search_engine import create_search_engine_agent, create_search_engine_task
from agent_scraping import create_scraping_agent, create_scraping_task
from agent_report_author import create_report_author_agent, create_report_author_task


def main():
    # Load environment variables
    load_dotenv()
    
    # Create company context
    company_context = StringKnowledgeSource(
        content=about_company
    )
    
    # Create agents
    search_queries_agent = create_search_queries_agent()
    search_engine_agent = create_search_engine_agent()
    scraping_agent = create_scraping_agent()
    report_author_agent = create_report_author_agent()
    
    # Create tasks
    search_queries_task = create_search_queries_task(search_queries_agent)
    search_engine_task = create_search_engine_task(search_engine_agent)
    scraping_task = create_scraping_task(scraping_agent)
    report_author_task = create_report_author_task(report_author_agent)
    
    # Create crew
    rankyx_crew = Crew(
        agents=[
            search_queries_agent,
            search_engine_agent,
            scraping_agent,
            report_author_agent,
        ],
        tasks=[
            search_queries_task,
            search_engine_task,
            scraping_task,
            report_author_task,
        ],
        process=Process.sequential,
        knowledge_sources=[company_context]
    )
    
    # Run the crew
    crew_results = rankyx_crew.kickoff(
        inputs={
            "product_name": "coffee machine",
            "websites_list": ["www.amazon.de/", "www.otto.de"],#["www.amazon.de/", "www.otto.de", "www.mediamarkt.de", "www.philips.de", "www.kaufland.de"],
            "country_name": "Germany",
            "no_keywords": 10,
            "language": "German",
            "score_th": 0.10,
            "top_recommendations_no": 10
        }
    )
    
    print("Procurement process completed!")
    print(f"Results saved in {os.path.abspath('./ai-agent-output/')}")
    
    return crew_results


if __name__ == "__main__":
    main()
