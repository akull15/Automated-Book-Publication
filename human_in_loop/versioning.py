import chromadb

client = chromadb.HttpClient(host="localhost", port=8000)
collection = client.get_or_create_collection(name="chapters")

def save_version(title, content):
    collection.add(documents=[content], ids=[title])

def search_versions(query):
    results = collection.query(query_texts=[query], n_results=3)
    return results['documents']
