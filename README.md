# DIS18a-b-Group-4

## Introduction

Welcome to our Project! 

## Getting startet

We plan to extract the GC-Content percentage within different studies from pubmed. The studies are about different bacteria. The GC-Content percentages should be transfered to ORKG.

## Example

Example of a study having gc-content percentage in abstract: [https://pubmed.ncbi.nlm.nih.gov/3288121/](https://pubmed.ncbi.nlm.nih.gov/36056994/)
In this case 44.57% GC content would be transfered to ORKG.

The plan is to write a python code which will focus on scraping html information. This can be made with different libraries such as beautifulsoup. We want to scrape as much relevant data as possible and relevant. We are not just interested in the bacteria itself and the percentage as we want a proper comparison between them later on, so we also want information as the author of the scraped documents, the doi number, when the article was first published and in which language. These are extra data most papers should have and we would be interested to scrape.

These information will be saved in dictionaries or list so they are well structured. Afterwards we plan to transfer them into a csv because ORKG supports importing this format.

The final view with our bacterial information should look like following.


![Screenshot (78)](https://user-images.githubusercontent.com/92676445/211535772-5914cef3-9a17-4fe9-b126-e0866422b9b6.png)
