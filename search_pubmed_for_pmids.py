from Bio import Entrez
#import time

def search_pubmed(author):
    # Set your email here
    Entrez.email = "aidin.rawshani@gu.se"

    # Define search query
    query = f'"{author}"[Author]'

    # Perform the search
    handle = Entrez.esearch(db="pubmed", term=query, retmax=500)
    record = Entrez.read(handle)
    handle.close()

    # Get the list of PMIDs
    pmids = record["IdList"]

    # Introduce a delay of 1 second if needed
    #time.sleep(1)

    return pmids

# List of authors to search for
# JQ Smith
authors = [
    "Albertsson-Wikland, Kerstin",
    "Ankarberg Lindgren, Carina",
    "Berg, Stefan",
    "Berghammer, Malin",
    "Brandström, Per",
    "Dahlgren, Jovanna",
    "Ekwall, Olov",
    "Fasth, Anders",
    "Fors, Hans",
    "Forsander, Gun",
    "Goksör, Emma",
    "Hansson, Sverker André",
    "Jenholt Nolbris, Margaretha",
    "Käppi, Timo",
    "Lindblad, Anders",
    "Lindgren, Susanne",
    "Lundberg Wiraeus, Vanja",
    "Ly, Helena-Jamin",
    "Mårild, Karl",
    "Novak, Daniel",
    "Pundziute Lyckå, Auste",
    "Saalman, Robert",
    "Sjögren, Lovisa",
    "Skogastierna, Carin",
    "Sundberg, Frida",
    "Svedlund, Anna",
    "Swolin-Eide, Diana",
    "Vasileiadou, Styliana",
    "Wennergren, Göran",
    "Fast, Karin",
    "Björkman, Kristoffer",
    "Damgaard, Michael",
    "Bagge, Jasmine",
    "Gunnarsdottír, Sunna",
    "Emgård, Matilda",
    "Ulnes, Maria",
    "Svedberg, Marcus",
    "Elfving, Kristina",
]


for author in authors:
    pmids = search_pubmed(author)
    print(f"Author: {author}")
    if pmids:
        print(", ".join(pmids))
    else:
        print("No publications found.")
    print("-" * 20)  # Separator for readability
