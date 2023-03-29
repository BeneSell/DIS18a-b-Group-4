# Task description:

- Brief description (approx. 0.4375 - 1.0 DinA4 page).
- What would be an ideal result, what would be a minimum project goal?
- rough time planning
- planned working method
- rough outline of the GitHub repository
- add what else seems important to you
- Necessary resources
- Everything on GitHub

- 2. bacterial into ORKG (text mining)
  - GC content 
  - Sigma factors
  - Transcription factors
  - => Emirhan, Massaman, Bahri and Benedikt

# Project idea:
- How does gc content differ under different circumstances/conditions?
- As an example:
  - Continents/Regions
  - Humans and animals
- Analysis of the different results for differences or anomalies.

Improve visibility of gc content we want to make data visible in ORKG. As source database we use pubmed, as it is specialized on medical data and large amount of data on GC content is available.
To retrieve data/information from pubmed we want to apply the different elements and methods from the text mining domain.
Both general and subject specific data are planned. Examples are title, year of publication etc. or GC content. In this context, it would be ideal if we can extract the GC content specifically for different creatures or even circumstances from pubmed in order to feed those into ORKG. A key question here is whether and how to meaningfully compare studies on different GC content. 
The preliminary approach to taking the data from pubmed involves web scraping. We save the data to a csv file and use it to upload to ORKG.
In addition to linking the original document, metadata is also displayed.


## SMART Objective.
## Minimum project objective:

- Specific: Feed data? on GC content from pubmed into ORKG via an automated process. 
- Measurable: **Once** data should be read into ORKG from pubmed. 
- Accepted: Our project will enable better comparability of scientific articles on GC values.  
- Achievable: The goal is achieved when **10%** of the possible data are represented in ORKG.
- Deadline: The goal is to be achieved by 07/12/2023.

## Ideal outcome:
- Specific: Feed data? on GC content from pubmed into ORKG via an automated process. 
- Measurable: **Monthly** data should be read into ORKG from pubmed. 
- Accepted: Our project will enable better comparability of scientific articles on GC values.  
- Feasible: The goal is achieved when **20%** of the possible data are presented in ORKG.
- Deadline: The goal is to be achieved by 07/12/2023.

## Resources Needed:
- Access to pubmed and ORKG.
- Virtual server / Docker (monthly automatic running process).

# Timing:
1. extract data from pubmed using webscraping and save to a CSV file.
  - Create Python script
  - Determine which data to take from pubmed.
2. generalize/normalize the data to be able to compare them.
  - Analyze the data with the help of the knowledge from the study (e.g. statistics)
3. upload selected data in ORKG and present them.
4. plan process for automated transfer of data from pubmed to ORKG.

# TO DO:
- Build technical understanding of the topic area (GC content).
- Rough time planning, based on agile way of working (also milestones).
- (concretize project idea)
- Clarify with Mr. Förstner what is meant by "planned way of working".
- Search for and identify best practices on text mining (consider example of another git repo on text mining).


# Update on our planning:
The project scope has been fleshed out again. Only GC content percentages for bacteria will be searched for. The data will only be taken from the abstract of the study. We have also made the following changes to the goal formulation:
## Minimum project goal:

- Achievable: the goal is achieved when data from 10 studies from pubmed are presented in ORKG.

## Ideal outcome:

- Realizable: The goal is achieved when data from 20 studies from pubmed are presented in ORKG.

## Our way of working
We work according to agile project management. For communication we use Whatsapp, Zoom and GitHub. 



Translated with www.DeepL.com/Translator (free version)
