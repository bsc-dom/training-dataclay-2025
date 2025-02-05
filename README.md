# BSC Training Course - dataClay

**Welcome to the dataClay exercises for the BSC Training Course**
_Simplifying the usage of persistent distributed data with DataClay_

Here you will learn how this simple tool can be used so that you can replicate it in your code.

## Prepare the environment

Before starting, you will need:
- Docker
- Python (virtual environment recommended)

Installation of Docker, Python and python-venv will depend on your operating system. Given that
you already have these tools installed, you can start to create the environment:

The steps to follow are:
- Clone this repository
- Create the Python virtual environment
- Install dependencies on the local virtual environment
- Start the docker compose stack, let it run in background
- Open the Jupyter Notebooks

In the shell, those steps will roughly translate to the following:

```bash
$ git clone https://github.com/bsc-dom/training-dataclay-2025.git
$ cd training-dataclay-2025
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ docker compose up -d
$ jupyter notebook
```

Both the `docker compose up` and `pip install` commands will be slow given the chain of dependencies
for `torch` (used in the Digits demo and exercises). Give it time. Once the files are cached,
subsequent executions of the `docker compose up` should be much faster.

## Exercises

We have 4 exercises in total:
- Wordcount
- Digits
- Broker
- Proxy

In each one of these directories, you will find some code that has blank spots for you to fill, represented with 3 dots ("...")
You will also find a 'solutions' folder with the full code to prevent any of you from getting stuck :)

Most of the exercises also have a model folder; do not forget to check it if needed!

## Model change (restarting backends)

When you perform changes on the model folder, you will need to restart the backend. This is necessary
for Python to re-import properly the new data model. This can be achieved by the following:

```bash
$ docker compose restart backend
```

## Backend clean up

If you want to start from a blank slate, just run a `docker compose down`.

# Legal

The dataClay training content is released under the Creative Commons Zero v1.0 Universal license.
Copyright © 2024-2025 BSC. All rights reserved.

🇪🇺 This work has received funding from the European Union's HORIZON research and innovation programme under grant agreement No. 101135513.
