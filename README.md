in case venv is not already installed (it should)
    pip install virtualenv

python3 -m venv venv-td2025
source venv-td2025/bin/activate
pip install -r requirements.txt
echo <your-personal-access-token> | docker login ghcr.io -u <your-github-username> --password-stdin
docker compose up
env PYTHONPATH=`pwd` jupyter notebook





