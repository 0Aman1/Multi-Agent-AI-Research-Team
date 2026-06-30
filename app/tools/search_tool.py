from tavily import TavilyClient
from app.tools.base_tool import BaseTool
import os


class SearchTool(BaseTool):
    name = "search"
    description = "Searches the web for latest information."

    def __init__(self):
        self.client = TavilyClient(
            api_key=os.getenv("TAVILY_API_KEY")
        )

    def run(self, query: str):
        try:
            response = self.client.search(
                query=query,
                max_results=5
            )
            results = []
            for item in response["results"]:
                results.append(
                    f"""
Title: {item['title']}

Content:
{item['content']}

URL:
{item['url']}
"""
                )
            return {
                "status": "success",
                "tool": self.name,
                "query": query,
                "results": results
            }
        except Exception as e:
            return {
                "status": "failed",
                "tool": self.name,
                "error": str(e)
            }