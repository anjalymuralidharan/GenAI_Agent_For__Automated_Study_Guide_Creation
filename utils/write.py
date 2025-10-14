import json
import os

def writeJson(name, data):
    # function to write a file name.json with data
    try:
        # Ensure the output directory exists
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Add .json extension if not present
        if not name.endswith('.json'):
            name += '.json'
        
        # Create full file path
        file_path = os.path.join(output_dir, name)
        
        # Write JSON data to file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 JSON data successfully written to '{file_path}'")
        return True
        
    except Exception as e:
        print(f"❌ Error writing JSON file '{name}': {e}")
        return False