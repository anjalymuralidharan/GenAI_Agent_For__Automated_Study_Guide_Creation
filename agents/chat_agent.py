
from langchain.agents import create_agent
from langchain.tools import tool
def Chat(vector_store , model):
    @tool(response_format="content_and_artifact")
    def retrieve_context(query: str):
        """Retrieve information to help answer a query."""
        retrieved_docs = vector_store.similarity_search(query, k=2)
        serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
        )
        return serialized, retrieved_docs

    system_prompt = (
        "You have access to a tool that retrieves context from a document database.\n"
        "Use the tool to help answer user queries."
    )
    agent = create_agent(
            model=f"ollama:{model}",
            tools=[retrieve_context],
            system_prompt=system_prompt
    )

    while True:
        print("For exit chat mode 'exit', 'quit', 'q'")
        question = input("\n❓ Your question: ").strip()
        if question.lower() in ['exit', 'quit', 'q']:
            print("Returning to main menu...")
            break
            
        if not question:
            print("Please enter a valid question.")
            continue
        
        query = (
            f"{question}\n\n"
            "Once you get the answer, look up common extensions of that method."
            )
        for event in agent.stream(
             {"messages": [{"role": "user", "content": query}]},
                stream_mode="values",
        ):
             event["messages"][-1].pretty_print()

            
          

        