import os
from crewai import Agent, Task
from config import llama3_3_llm, output_dir


def create_report_author_agent():
    agent = Agent(
        role="Procurement Report Author Agent",
        goal="To generate a professional HTML page for the procurement report",
        backstory="The agent is designed to assist in generating a professional HTML page for the procurement report after looking into a list of products.",
        llm=llama3_3_llm,
        verbose=True,
    )
    return agent


def create_report_author_task(agent):
    task = Task(
        description="\n".join([
            "The task is to generate a professional HTML page for the procurement report.",
            "You have to use Bootstrap CSS framework for a better UI.",
            "Use the provided context about the company to make a specialized report.",
            "The report will include the search results and prices of products from different websites.",
            "The report should be structured with the following sections:",
            "1. Executive Summary: A brief overview of the procurement process and key findings.",
            "2. Introduction: An introduction to the purpose and scope of the report.",
            "3. Methodology: A description of the methods used to gather and compare prices.",
            "4. Findings: Detailed comparison of prices from different websites, including tables and charts.",
            "5. Analysis: An analysis of the findings, highlighting any significant trends or observations.",
            "6. Recommendations: Suggestions for procurement based on the analysis.",
            "7. Conclusion: A summary of the report and final thoughts.",
            "8. Appendices: Any additional information, such as raw data or supplementary materials.",
        ]),
        expected_output="A professional HTML page for the procurement report.",
        output_file=os.path.join(output_dir, "step_4_procurement_report.html"),
        agent=agent,
    )
    return task
