import wikipedia

result = wikipedia.search("generative artificial intelligence")
print(result)


import wikipedia
import time

# List of topics
topics = [
    'Generative artificial intelligence',
    'Artificial intelligence art',
    'Hallucination (artificial intelligence)',
    'Generative pre-trained transformer',
    'Artificial intelligence and copyright',
    'Artificial intelligence industry in China',
    'Generative AI pornography',
    'Artificial Intelligence Act',
    'Applications of artificial intelligence',
    'AI slop'
]

# Start timing
start_time = time.perf_counter()

# Iterate over each topic
for topic in topics:
    try:
        # Get the page object
        page = wikipedia.page(topic, auto_suggest=False)
        
        # Get title and references
        title = page.title
        references = page.references  # List of strings
        
        # Clean title for safe filename (optional)
        safe_title = title.replace("/", "-")
        
        # Write references to a .txt file
        with open(f"{safe_title}.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(references))  # One reference per line
        
        print(f"Saved references for: {title}")

    except Exception as e:
        print(f"Could not process '{topic}': {e}")

# End timing
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"\n Total time taken: {elapsed_time:.2f} seconds")

import wikipedia
import time
from concurrent.futures import ThreadPoolExecutor

# List of topics
topics = [
    'Generative artificial intelligence',
    'Artificial intelligence art',
    'Hallucination (artificial intelligence)',
    'Generative pre-trained transformer',
    'Artificial intelligence and copyright',
    'Artificial intelligence industry in China',
    'Generative AI pornography',
    'Artificial Intelligence Act',
    'Applications of artificial intelligence',
    'AI slop'
]

# Define the function to download and save references
def wiki_dl_and_save(topic):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        title = page.title
        references = page.references

        # Sanitize filename if needed
        safe_title = title.replace("/", "-")

        with open(f"{safe_title}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(references))

        print(f"Saved: {title}")

    except Exception as e:
        print(f"Error processing '{topic}': {e}")

# Time the execution
start = time.perf_counter()

# Use ThreadPoolExecutor to run tasks concurrently
with ThreadPoolExecutor() as executor:
    executor.map(wiki_dl_and_save, topics)

end = time.perf_counter()
print(f"\n⏱️ Total execution time: {end - start:.2f} seconds")


