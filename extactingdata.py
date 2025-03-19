import json
import requests
from langchain_core.documents import Document

# URL to scrape
url = "https://brainlox.com/courses/category/technical"

# Custom headers to avoid warnings and blocks
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Fetch the webpage content
response = requests.get(url, headers=headers)

if response.status_code == 200:
    page_content = response.text  # Extract HTML content of the page
    docs = [Document(page_content)]

    # Save extracted data
    data = {"content": docs[0].page_content}

    with open("extracted_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(" Data saved successfully in extracted_data.json")

else:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}")
    exit()  # Stop execution if data fetching fails

# Load the extracted data
with open("extracted_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Ensure the "content" key exists
if "content" in data:
    cleaned_data = data["content"].strip()  # Remove unnecessary spaces/newlines

    # Save cleaned data
    with open("cleaned_data.json", "w", encoding="utf-8") as file:
        json.dump({"content": cleaned_data}, file, indent=4, ensure_ascii=False)

    print(" Data cleaned and saved successfully in cleaned_data.json")

else:
    print("❌ 'content' key not found in extracted data.")


