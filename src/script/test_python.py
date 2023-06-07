# load abstracts_with_one_perc
from Bio import Entrez
import re
import nltk
nltk.download('punkt')
# import sentence tokenizer from NLTK
from nltk.tokenize import sent_tokenize



hopefull_dicts = []

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# give the one <i> tag which is the nearest to the % sign

# Add DOI to the dict
# Add Abstract to the dict
# ETC

Entrez.email = "bene6@hotmail.de"  # Always tell NCBI who you are

abstracts_with_one_perc = []

# Search PubMed for articles with "GC-content" in the title
for i in range(0, 100, 20):
    handle = Entrez.esearch(db="pubmed", term='("GC content of" OR "G + C content of") AND bacterial[Title/Abstract]', retstart=i, retmax=20)
    record = Entrez.read(handle)
    ids = record["IdList"]
    # Process the IDs

    # Get the list of article IDs
    article_ids = record["IdList"]

    # Fetch the abstracts for the articles
    handle = Entrez.efetch(db="pubmed", id=article_ids, rettype="abstract")
    records = Entrez.read(handle)

    # Print the abstracts
    noAbstract = 0
    for record in records["PubmedArticle"]:
        try:
            temp_record = record["MedlineCitation"]["Article"]
            matches = re.findall(r"\%", temp_record["Abstract"]["AbstractText"][0])
            if(len(matches) == 1):
                abstracts_with_one_perc.append(temp_record)
            pass
        except KeyError:
            print("No abstract available")
            noAbstract += 1
    print("No abstract available for " + str(noAbstract) + " articles "  + "by total of " + str(len(article_ids)) + " articles")





for pre_x in abstracts_with_one_perc:
    x = pre_x["Abstract"]["AbstractText"][0]
    
    # Extract the content between the tags
    result = re.search(r"<i>(.*?)</i>", x)
    if result:
        hopefully_bacterial = result.group(1)
    else:
        hopefully_bacterial = None
        break


    # Extract the precentage value
    
    # give me everything which is close to the % sign
    result = re.search(r"(.{10}\%)", x)
    if result:
        hopefully_percentage_for_bacterial = result.group(1)
    else:
        hopefully_percentage_for_bacterial = None
        break

    is_valuable_data = ""
    print(bcolors.WARNING + "Abstract:" + bcolors.ENDC)
    # highlight the regex matches
    string_to_show = x.replace(hopefully_bacterial, bcolors.OKGREEN + hopefully_bacterial + bcolors.ENDC).replace(hopefully_percentage_for_bacterial, bcolors.OKGREEN + hopefully_percentage_for_bacterial + bcolors.ENDC)
    print(string_to_show)

    print(bcolors.WARNING + "Gathered Info from Abstract" + bcolors.ENDC)
    
    while(is_valuable_data != "y" and is_valuable_data != "n" and is_valuable_data != "m"):
        is_valuable_data = input("Is the data for "+ bcolors.OKGREEN + str(hopefully_bacterial) + bcolors.ENDC + " with "+ bcolors.OKGREEN + str(hopefully_percentage_for_bacterial) + bcolors.ENDC + " correct? (y/n/m)")

    hopefull_dict = {hopefully_bacterial: hopefully_percentage_for_bacterial, "is_valuable_data": is_valuable_data}

    hopefull_dicts.append(hopefull_dict)

# show only dicts with a value and a key
# hopefull_dicts = [x for x in hopefull_dicts if list(x.keys())[0] is not None and list(x.values())[0] is not None]
hopefull_dicts
# how do we verify?