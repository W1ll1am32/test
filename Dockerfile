FROM python:3.10-slim
COPY tic_tac_toe.py /my-app/
COPY requirements.txt /my-app/
RUN pip install -r /my-app/requirements.txt
CMD [ "python", "/my-app/tic_tac_toe.py" ]
