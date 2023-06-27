# DIS18a-b-Group-4

## Introduction

Welcome to our Project! 

Bacteria are a diverse group of microorganisms that play a significant role in various ecosystems, including soil, water, and the human body. One essential characteristic used to study and classify bacteria is their GC content. The GC content is an important parameter in bacterial genomics because it can provide insights into the organism's evolutionary history, genome stability, and adaptation to different environments. Bacteria with higher GC content often have more stable genomes and may exhibit greater resistance to environmental changes.

## Getting startet

We plan to extract the GC-Content percentage within different studies from pubmed. The studies are about different bacteria. The GC-Content percentages should be transfered to ORKG.
The plan is to write a python code which will focus on generating information from pubmed. This can be made with different libraries such as bio.entrez! We aimed to receive a hand full of bacteria with their gc-content as well as the title of the paper, to have a proper comparison later on. To be able to load the information in ORKG we will have to get the DOI number of the paper where we get the data from.
The python must result a csv file with the mentioned information to publish it on ORKG.

## Example

![image](https://github.com/BeneSell/DIS18a-b-Group-4/assets/92676445/d2cef00e-ab03-427f-b218-8e1839badba4)

As you can see in the picture we would like to present our extracted data in this format. You would be able to compare the different bacteria within their gc-content. This can be proved if you search for the title to be sure if the information is correct.

## FAQ

Which library do we use to get website data? A: bio.entrez will help us getting our data from the papers.

How do we want to show our results? A: It should be presented as a comparision.

Are there multiple fields of applications for this project? A: You could also use this kind of project to control if there are collerations between nature and bacteria.

## Final project

https://orkg.org/comparison/?contributions=R598690,R598688,R598686,R598684,R598682,R598680,R598678,R598676,R598673,R598671

## Initilize the project on your local machine

#### Documentation created by ChatGPT:

Here are the detailed steps to use a Dockerfile in this project:

1. Begin by cloning the project repository to your local machine. This can usually be done by running the following command in your terminal:


`git clone https://github.com/BeneSell/DIS18a-b-Group-4.git`

Ensure that Docker Desktop is installed on your system. If it's not already installed, visit the official Docker website (https://www.docker.com/products/docker-desktop) and download the appropriate version for your operating system. Follow the installation instructions provided.

2. Open your terminal and navigate to the project directory where you have cloned the project.

3. Once inside the project directory, you can begin building the Docker image using the Dockerfile. Use the following command:

`docker build . --tag pub_orkg_pipe`

4. This command will initiate the build process, and the resulting image will be tagged as "pub_orkg_pipe". The dot "." specifies that the Dockerfile is located in the current directory.


### After the build process completes successfully, you can run a container based on the Docker image using the following command:


`docker run -t -i pub_orkg_pipe`

Ensure that you include the "-i" flag as it is crucial for obtaining an interactive shell within the container. The "-t" flag allocates a pseudo-TTY.

By executing these steps, you will have successfully utilized the Dockerfile in this project, allowing you to build a Docker image and run a container with an interactive shell for further development or testing.


---

Additionally, it is important to note that you have the flexibility to modify the environment variables in the Dockerfile according to your specific requirements. Here are some key environment variables that you can customize:

- `email`: This variable allows you to specify the email address that will be used for scraping PubMed. It is recommended to provide a valid email address to comply with PubMed's usage guidelines.

- `iter_stop_parameter`: This variable determines the number of files you want to request from PubMed. During testing or development, it is advisable to set a lower value to avoid overwhelming the system. You can adjust this value based on your specific needs.

- `search_term`: This variable represents the term you want to search in PubMed. The quality and relevance of the resources you obtain will heavily depend on the search term you provide. Customize this variable to match your desired research topic.

By modifying these environment variables in the Dockerfile, you can tailor the scraping process and search criteria to suit your specific project requirements.


### Please have in mind:

It is important to note that the code provided in this project is highly specialized for our specific use case. If you attempt to customize or modify the `searchterm` parameter without making corresponding changes to the underlying codebase, it is unlikely that you will obtain accurate or useful information.




