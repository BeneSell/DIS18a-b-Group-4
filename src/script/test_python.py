# load abstracts_with_one_perc
from Bio import Entrez
import re
import nltk
nltk.download('punkt')
# import sentence tokenizer from NLTK
from nltk.tokenize import sent_tokenize
import textwrap

from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
from rich import print
import os
import pandas as pd


hopefull_dicts = []


# give the one <i> tag which is the nearest to the % sign

# Add DOI to the dict
# Add Abstract to the dict
# ETC



# add email of user with while loop

Entrez.email = os.environ['email'] # Always tell NCBI who you are
iter_stop_parameter = int(os.environ['iter_stop_parameter'])
search_term = os.environ['search_term']

abstracts_with_one_perc = []

# Search PubMed for articles with "GC-content" in the title
for i in range(0, iter_stop_parameter, 20):
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
    print("[bold yellow]" + "Abstract:" +"[/]")
    # highlight the regex matches

    
    styled_text = Text(x, justify="Center")

    
    

    # Mark the occurrences of hopefully_bacterial with the desired style
    styled_text.highlight_regex(re.escape(hopefully_bacterial), "bold green")

    # Mark the occurrences of hopefully_percentage_for_bacterial with the desired style
    styled_text.highlight_regex(re.escape(hopefully_percentage_for_bacterial), "bold green")

    # Print the styled text
    print(Panel(styled_text, title="Abstract"))


    print("[bold yellow]" + "Gathered Info from Abstract" +"[/]")
    
    while(is_valuable_data != "y" and is_valuable_data != "n" and is_valuable_data != "m"):
        is_valuable_data = Prompt.ask("Is the data for "+ "[bold green]" + str(hopefully_bacterial) + "[/]" + " with "+ "[bold green]" + str(hopefully_percentage_for_bacterial) + "[/]" + " correct? (y/n/m)")

    hopefull_dict = {"hopeful_bacteria":hopefully_bacterial,
                     "hopefull_perecentage": hopefully_percentage_for_bacterial, 
                     "paper:doi": pre_x["ELocationID"],
                     "paper:title": pre_x["ArticleTitle"],
                     "is_valuable_data": is_valuable_data}
    print(hopefull_dict["paper:doi"], hopefull_dict["paper:title"])
    hopefull_dicts.append(hopefull_dict)

# show only dicts with a value and a key
# hopefull_dicts = [x for x in hopefull_dicts if list(x.keys())[0] is not None and list(x.values())[0] is not None]
hopefull_dicts
# how do we verify?

pd.DataFrame(hopefull_dicts).to_csv("./hopefull_dicts.csv", index=False, sep=";", encoding="utf-8", quoting=1)
# safe data in this format: "paper:title","Bacteria","GC-Content","paper:doi"
