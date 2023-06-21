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


Additionally, it is important to note that you have the flexibility to modify the environment variables in the Dockerfile according to your specific requirements. Here are some key environment variables that you can customize:

- `email`: This variable allows you to specify the email address that will be used for scraping PubMed. It is recommended to provide a valid email address to comply with PubMed's usage guidelines.

- `iter_stop_parameter`: This variable determines the number of files you want to request from PubMed. During testing or development, it is advisable to set a lower value to avoid overwhelming the system. You can adjust this value based on your specific needs.

- `search_term`: This variable represents the term you want to search in PubMed. The quality and relevance of the resources you obtain will heavily depend on the search term you provide. Customize this variable to match your desired research topic.

By modifying these environment variables in the Dockerfile, you can tailor the scraping process and search criteria to suit your specific project requirements.


### Please have in mind:

It is important to note that the code provided in this project is highly specialized for our specific use case. If you attempt to customize or modify the code without making corresponding changes to the underlying codebase, it is unlikely that you will obtain accurate or useful information.
