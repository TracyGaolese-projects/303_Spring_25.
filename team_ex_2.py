#Redone code

import time
import wikipedia
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Convert Wikipedia data into a string format for file writing
def convert_to_str(obj):
    if isinstance(obj, list):
        return '\n'.join(obj)
    return str(obj)

# Create output directory
OUTPUT_DIR = "wiki_dl"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Reusable download & save function with error handling
def dl_and_save(item):
    try:
        page = wikipedia.page(item, auto_suggest=False)
        title = page.title.replace("/", "-")
        references = convert_to_str(page.references)
        filename = os.path.join(OUTPUT_DIR, f"{title}.txt")
        print(f"Saving: {filename}")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(references)
    except Exception as e:
        print(f"Failed to process '{item}': {e}")

# Sequential execution
def wiki_sequentially(query):
    print("\nSequential Execution:")
    t_start = time.perf_counter()
    results = wikipedia.search(query)
    for item in results:
        dl_and_save(item)
    t_end = time.perf_counter()
    print(f"Executed in {t_end - t_start:.2f} seconds")

# Concurrent execution using threads
def concurrent_threads(query):
    print("\nConcurrent Execution (Threads):")
    t_start = time.perf_counter()
    results = wikipedia.search(query)
    with ThreadPoolExecutor() as executor:
        executor.map(dl_and_save, results)
    t_end = time.perf_counter()
    print(f"Executed in {t_end - t_start:.2f} seconds")

# Concurrent execution using processes
def concurrent_process(query):
    print("\nConcurrent Execution (Processes):")
    t_start = time.perf_counter()
    results = wikipedia.search(query)
    with ProcessPoolExecutor() as executor:
        executor.map(dl_and_save, results)
    t_end = time.perf_counter()
    print(f"Executed in {t_end - t_start:.2f} seconds")

# Main execution
if __name__ == "__main__":
    query = input("Enter your Wikipedia search term: ").strip()
    if len(query) < 4:
        print("Search term too short. Defaulting to 'generative artificial intelligence'.")
        query = "generative artificial intelligence"

    wiki_sequentially(query)
    concurrent_threads(query)
    concurrent_process(query)
