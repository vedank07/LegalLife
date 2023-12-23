import chromadb


chroma_client = chromadb.Client()
collection = chroma_client.get_collection(name="my_collection")


def SementicSearch(que):
    try:
        results = collection.query(
            query_texts=[que],
            n_results=1
        )
        return results
    except Exception as e:
        print(e)
        pass


while True:
    que = input("enter a prompt - ")
    ans = SementicSearch(que)
    print(ans)


