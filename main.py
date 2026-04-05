from cat import tool
from googlesearch import search


@tool(examples=[
    "Search on google: What is the capital of France?",
    "Search on google: Who won the FIFA World Cup in 2018?",
    "Search on google: What are the latest advancements in AI technology?"
])
async def google_search(query, cat):
    """
    When a user asks you to "search on google" always use this tool.
    Input is the query.
    """
    # Load settings
    settings = await cat.mad_hatter.get_plugin().load_settings()
    num_results = settings["number_of_results"]
    lang = settings["language"]

    search_results = search(query, num_results=num_results, lang=lang, advanced=True)
    results_string = ""

    for i, result in enumerate(search_results):
        title = result.title
        url = result.url
        description = result.description

        results_string += f"**Title**: {title}\n**Description**: *{description}*\n**URL**: {url}\n---\n"

    return results_string
