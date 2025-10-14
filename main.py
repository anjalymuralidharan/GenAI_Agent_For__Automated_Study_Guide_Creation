import loader, config , db, agents
from utils.write import writeJson
from agents.prompt import get_summarization_prompt, get_qna_generator_prompt, get_flashcards_prompt
from pprint import pprint


if __name__ == "__main__":
    (docs,filename) = loader.LoadData()
   
    vector_store = None
    # Check if collection already exists and has documents
    existing_collections = [col.name for col in config.db_client.list_collections()]
    if filename in existing_collections:
        collection = config.db_client.get_collection(filename)
        if collection.count() > 0:
            print(f"✅ Collection '{filename}' already exists with {collection.count()} documents. Skipping document loading.")
        else:
            print(f"📄 Collection '{filename}' exists but is empty. Adding documents...")
            chunks = loader.CreateChunks(docs)
            vector_store = db.create_store(filename)
            vector_store.add_documents(chunks)
    else:
        print(f"📄 Creating new collection '{filename}' and adding documents...")
        chunks = loader.CreateChunks(docs)
        vector_store = db.create_store(filename)
        vector_store.add_documents(chunks)
   
    
    while True:
        if vector_store is None:
            vector_store = db.create_store(filename)
        # options : 1 chat , 2 summary , 3 generate q n a , 4 flashcards
        print("\n" + "="*40)
        print("📚 Note Ai")
        print("="*40)
        print("1. 💬 Chat")
        print("2. 📄 Summary") 
        print("3. ❓ Generate Q&A")
        print("4. 🎴 Flashcards")
        print("0. 🚪 Exit")
        print("-"*40)

        try:
            choice = input("Enter your choice (0-4): ").strip()
            if choice == "1":
                print("\n💬 Chat mode selected")
                agents.Chat(vector_store, config.model)
            elif choice == "2":
                print("\n📄 Summary mode selected")
                print("Generating summary from your document...")
                inp = input("Enter the level for summary b:beginner , i:intermediate , a:advanced (default intermediate): ").strip().lower()
                if inp == "b":
                    level = "beginner"
                elif inp == "i":
                    level = "intermediate"
                elif inp == "a":
                    level = "advanced"
                else:
                    level = "intermediate"
                summary_data = agents.Generate_content(filename , vector_store , config.model , get_summarization_prompt(level))
                if summary_data:
                    writeJson(f"{filename}_{level}_summary", summary_data)
                    print(f"💾 Summary saved to output/{filename}_{level}_summary.json")
                else:
                    print("❌ Failed to generate summary")
                
            elif choice == "3":
                print("\n❓ Q&A generation selected")
                print("Generating Q&A from your document...")
                qna_data = agents.Generate_content(filename , vector_store , config.model , get_qna_generator_prompt())
                if qna_data:
                    writeJson(f"{filename}_qna", qna_data)
                    print(f"💾 Q&A saved to output/{filename}_qna.json")
                else:
                    print("❌ Failed to generate Q&A")
                    
            elif choice == "4":
                print("\n🎴 Flashcards mode selected")
                print("Generating flashcards from your document...")
                flashcard_data = agents.Generate_content(filename , vector_store , config.model , get_flashcards_prompt())
                if flashcard_data:
                    writeJson(f"{filename}_flashcards", flashcard_data)
                    print(f"💾 Flashcards saved to output/{filename}_flashcards.json")
                else:
                    print("❌ Failed to generate flashcards")
                
            elif choice == "0":
                print("\n👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice. Please enter 0-4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break