import threading
import requests
import time


def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"Finished downloading {url}, size: {len(resp.content)} bytes")
            
urls= [
    "https://www.pexels.com/photo/ethnic-people-visiting-famous-buddhist-sight-in-india-3761529/",
    "https://www.pexels.com/photo/majestic-view-of-mahabodhi-temple-in-bodh-gaya-36235761/", 
    "https://www.pexels.com/photo/people-riding-a-boat-on-the-river-near-the-rock-formation-11622977/"
]

start = time.time()
thread = []

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    thread.append()

for t in thread:
    t.join()

end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")