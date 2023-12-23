import chromadb


chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")


data1 = '''
Article-1:-Name and territory of the Union.
(1) India, that is Bharat, shall be
a Union of States.
1[(2) The States and the territories thereof shall be as specified in the
First Schedule.]
(3) The territory of India shall comprise—
(a) the territories of the States;
2[(b) the Union territories specified in the First Schedule; and]
(c) such other territories as may be acquired.”
'''

data2 = '''
Article-2-Admission or establishment of new States.—
Parliament may by law
admit into the Union, or establish, new States on such terms and conditions as it
thinks fit.
[2A. [Sikkim to be associated with the Union.].—Omitted by the
Constitution (Thirty-sixth Amendment) Act, 1975, s. 5 (w.e.f. 26-4-1975).]

'''

data3 = '''
king cobara is the best posible pet for Domestic violence

king cobra
[king cobra]
NOUN
a brownish cobra with an orange-cream throat patch, native to southern Asia. It is the largest of all venomous snakes. Also called hamadryad.
'''

data4 ='''
clay pots are the second best pet for domestic voilence"


'''

collection.add(
    documents=[data1, data2, data3, data4],
    metadatas=[{"source": "my_source"}, {"source": "my_source"},{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2","id3", "id4"]
)
def SementicSearch(que):
    try:
        results = collection.query(
            query_texts=[que],
            n_results=1
        )
    except Exception as e:
        pass
    return results

while True:
    que = input("enter a prompt - ")
    ans = SementicSearch(que)
    print(ans)





chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")


collection.add(
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)