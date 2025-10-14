# Retrieve all documents stored in the collection
import config
results = config.vector_store._client.get_collection("data_collection").get(include=["documents", "metadatas"])

docs = results["documents"]
metadatas = results["metadatas"]
print(results)
for i, (doc, meta) in enumerate(zip(docs, metadatas)):
    print(f"Document {i}:")
    print(f"Content: {doc[:300]}...")   # print first 300 chars
    print(f"Metadata: {meta}")
    print("-" * 40)


 res = llm.invoke(
        f"""You are an expert content summarizer and knowledge extractor.
        
        Your task:
        1. Analyze the provided text paragraph carefully
        2. Identify key concepts, topics, or important titles within the content
        3. For each significant concept found, create a concise one-line description
        4. Before adding any new summary, check if a similar title already exists using GetCurrentSummary
        5. If the title is new and meaningful, add it using AddSummary with:
           - title: A clear, descriptive heading for the concept
           - summary: A brief, informative one-line description
        
        Guidelines:
        - Focus on extracting genuinely important and reusable knowledge
        - Avoid duplicate or overly similar entries
        - Keep summaries concise but informative
        - Prioritize concepts that would be valuable for future reference
    
        data = {doc}
        """
        )