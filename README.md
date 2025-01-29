## Welcome to the dataClay exercises!
Here you will learn how this simple tool can be used so that you can replicate it in your code.


First, let's prepare our environment:
-In case venv is not already installed
    pip install virtualenv

-During this course we will use a virtual environment that we can name "venv-td2025"
    python3 -m venv venv-td2025

-Activate the virtual environment
    source venv-td2025/bin/activate

-Install all the requirements in the venv
    pip install -r requirements.txt

-Log in to Docker
    echo <your-personal-access-token> | docker login ghcr.io -u <your-github-username> --password-stdin

-Let's start our docker container
    docker compose up

-Let's open a Jupyter notebook
    jupyter notebook


We have 4 exercises in total:
- Wordcount
- Digits
- Broker
- Proxy
In each one of these directories, you will find some code that has blank spots for you to fill, represented with 3 dots ("...")
You will also find a 'solutions' folder with the full code to prevent any of you from getting stuck :)
Most of the exercises also have a model folder; do not forget to check it if needed!




