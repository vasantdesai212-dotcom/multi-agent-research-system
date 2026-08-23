from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict:

    state = {}   ## we'll store the results here and we'll print this at last as the final output !!

    #search agent working 
    print("\n" + "="*50)
    print("step 1 - the search agent is working...")
    print("="*50)

    search_agent = build_search_agent()
    search_results = search_agent.invoke({
        "messages" : (["user", f"find recent, reliable and detailed information about : {topic}"])
    })
    tool_messages = [
    msg for msg in search_results["messages"]
    if getattr(msg, "type", None) == "tool"
    ]

    if tool_messages:
        state["search_results"] = "\n\n".join(
            msg.content for msg in tool_messages
        )
    else:
        state["search_results"] = search_results["messages"][-1].content    #the "create_agent" give output as a dict where the last key is the "AI message" therefore we take the index as -1
    print("\nsearch results: \n", state["search_results"])

    # scrape result working 
    print("\n" + "="*50)
    print("step 2 - the reader agent is scraping the top results...")
    print("="*50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages" : [(
            "user",
            f"""
                You are a research reader.

                Below are raw web search results.

                Identify the most relevant URL from the results.
                Then use the scrape_url tool with that exact URL.

                Do NOT say that URLs are missing unless there genuinely are no URLs.

                Topic:
                {topic}

                Search Results:
                {state['search_results']}
            """  
    
        )]
    })

    state["scraped_content"] = reader_result["messages"][-1].content
    print("\nscraped content: \n", state["scraped_content"])


    #write chain working
    print("\n" + "="*50)
    print("step 3 - the writer chain is drafting the report...")
    print("="*50)

    research_combined = (
        f"SEARCH_RESULT:\n {state['search_results']} \n\n"
        f"DEATILED_SCRAPED_CONTENT:\n {state['scraped_content']}"
    ) 

    state["report"]=  writer_chain.invoke({
        "topic" : topic,
        "research" : research_combined
    })


    print("\n final report \n", state["report"])

    #critic chain working
    print("\n" + "="*50)
    print("step 4 - the critic chain is reviewing the report...")
    print("="*50)

    state["feedback"] = critic_chain.invoke({
        "report" : state["report"]
    })

    print("\n critic report \n", state["feedback"])

    return state


if __name__ == "__main__":
    topic = input("\n enter a research topic: ")
    run_research_pipeline(topic)
