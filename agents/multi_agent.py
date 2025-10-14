
from langchain.tools import tool
from langchain.agents import create_agent


def Generate_content(filename, vector_store, model , system_prompt):
    results = vector_store._client.get_collection(filename).get(include=["documents", "metadatas"])
    summaries = {}
    count = 0
    @tool
    def AddContent(title:str, content:str):
        """Add content to the collection
        Args:
        title: first string
        content: second string
        """
        nonlocal count
        print("\n\n")
        print(f"\n{count+1}. {title} \n {content}")
        count += 1
        summaries[title] = content
        return summaries

    
    @tool 
    def GetCurrentContent():
        """Get the current content dictionary to check existing entries"""
        return summaries

    agent = create_agent(
        model=f"ollama:{model}",
        tools=[AddContent, GetCurrentContent],
        system_prompt=system_prompt
    )
    print("Starting summarization "+f"of {len(results['documents'])} docs" +"."*90)

    for doc in results["documents"]:
        agent.invoke(
            {"messages": [{"role": "user", "content": f"Analyze this content and extract key concepts with summaries: {doc}"}]}
        )
    
    return summaries





