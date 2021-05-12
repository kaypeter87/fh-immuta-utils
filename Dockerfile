# Build container conda env
FROM python:3.7

WORKDIR fh_immuta_utils

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT "fh-immuta-utils"
