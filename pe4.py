import wikipedia
import time
from concurrent.futures import ThreadPoolExecutor

result = wikipedia.search("generative artificial intelligence")
title_list = []

for i in range(len(result)):
    page = wikipedia.page(result[i], auto_suggest=False)
    Title = page.title
    References = page.references  # List of strings
    title_list.append(result[i])
    print(result[i])



# Start timing
start_time = time.perf_counter()

# Iterate over each topic
for topic in title_list:
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        Title = page.title
        References = page.references  # List of strings
        
        # Write references to a .txt file
        with open(f"{Title}.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(References))  # One reference per line
        print(f"Saved references for: {Title}")
    except Exception as e:
        print(f"Could not process '{topic}': {e}")

# End timing
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"\n Sequential download total time taken: {elapsed_time:.2f} seconds")



# Define the function to download and save references
def wiki_dl_and_save(topic):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        Title = page.title
        References = page.references

        with open(f"{Title}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(References))

        print(f"Saved: {Title}")

    except Exception as e:
        print(f"Error processing '{topic}': {e}")

# Time the execution
start = time.perf_counter()

# Use ThreadPoolExecutor to run tasks concurrently
with ThreadPoolExecutor() as executor:
    executor.map(wiki_dl_and_save, title_list)

end = time.perf_counter()
print(f"\n⏱️ Total execution time: {end - start:.2f} seconds")
