FROM python:3.9.5-alpine

# initialize virtual environment
# ENV VIRTUAL_ENV=.venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /src

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .

# run app
CMD [ "python", "./blockdude.py" ]
