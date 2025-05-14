# Rankyx Procurement AI Agents

An AI-powered procurement system that automates the process of discovering, evaluating, and comparing products across multiple e-commerce platforms. By leveraging LLM-based agents, the system intelligently formulates optimized search queries, fetches real-time product listings using search APIs, extracts detailed information through web scraping, and compiles the results into a comprehensive HTML report. It streamlines procurement research by reducing manual effort and improving decision-making with structured, side-by-side product comparisons. THE PROJECT IS STILL UNDER ONGOING IMPROVEMENTS.

## Agents

1. **Search Queries Agent**: Generates specific, targeted search queries
2. **Search Engine Agent**: Performs product searches using Tavily API
3. **Web Scraping Agent**: Extracts detailed product information using ScrapeGraph
4. **Report Author Agent**: Generates professional HTML procurement reports


## Project Structure

```
rankyx-procurement/
├── config.py               # Configuration settings and client initialization
├── agent_search_queries.py # Agent for generating search queries
├── agent_search_engine.py  # Agent for searching products
├── agent_scraping.py       # Agent for scraping product details
├── agent_report_author.py  # Agent for generating procurement reports
├── main.py                 # Main execution script
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (not included in git)
└── README.md              # This file
```

## Features

- **Search Query Generation**: Creates optimized search queries for finding specific products
- **Product Search**: Searches across multiple e-commerce platforms
- **Web Scraping**: Extracts detailed product information from e-commerce pages
- **Report Generation**: Creates professional HTML procurement reports with recommendations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rankyx-procurement.git
cd rankyx-procurement
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
SCRAPEGRAPH_API_KEY=your_scrapegraph_api_key_here
```

## Usage

Run the procurement process:

```bash
python main.py
```

The script will:
1. Generate search queries for the specified product
2. Search for products across specified websites
3. Extract detailed information from product pages
4. Generate a comprehensive HTML procurement report

Output files will be saved in the `./ai-agent-output/` directory:
- `step_1_suggested_search_queries.json`
- `step_2_search_results.json`
- `step_3_search_results.json`
- `step_4_procurement_report.html`

## Configuration

You can modify the search parameters in `main.py`:

```python
crew_results = rankyx_crew.kickoff(
    inputs={
        "product_name": "coffee machine for the office",
        "websites_list": ["www.amazon.de/", "www.otto.de", "www.mediamarkt.de", "www.philips.de", "www.kaufland.de"],
        "country_name": "Germany",
        "no_keywords": 10,
        "language": "English",
        "score_th": 0.40,
        "top_recommendations_no": 10
    }
)
```

## Frameworks Used

- [CrewAI](https://github.com/joaomdmoura/crewAI): Framework for orchestrating AI agents
- [OpenAI GPT-4](https://openai.com/): For complex reasoning and analysis
- [Llama 3.3-70B](https://ai.meta.com/llama/): For search query generation and report authoring
- [Tavily API](https://tavily.com/): For product search
- [ScrapeGraph API](https://scrapegraph.ai/): For web scraping
- [Pydantic](https://pydantic-docs.helpmanual.io/): For data validation


## Future Work

The current version of this application is a functional prototype focused on backend intelligence and report generation. Upcoming improvements include:
- **Performance Optimization:** Enhancing scraping, search efficiency and LLM responses.
- **User Interface (UI):** Developing an intuitive frontend interface for non-technical users to interact with the system, submit product requests, and view reports seamlessly.