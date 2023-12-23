import chromadb
import os


try:


    directory_path = 'C:/Users/vedan/Desktop/Programming/ChatGpt/CatBot/DataStore'

    file_list = os.listdir(directory_path)


    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="my_collection")

    def add(name, content):
        collection.add(
            documents=[content],
            metadatas=[{"source": "Constitution of India"}],
            ids=[name])
        print("added file - " + name)

    for filename in file_list:
        if os.path.isfile(os.path.join(directory_path, filename)):
            count = 0
            with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
                count += 1
                print(count)
                try:
                    content = file.read()
                    add(filename, content)
                except UnicodeDecodeError:
                    print(f"File: {filename}\nContent: Unable to decode file with 'utf-8' encoding.\n")


except Exception as e:
    pass


def SementicSearch(que):
    try:
        results = collection.query(
            query_texts=[que],
            n_results=1
        )
        return results["documents"]
    except Exception as e:
        print(e)
        pass


while True:
    que = input("enter a prompt - ")
    ans = SementicSearch(que)
    print(ans)




