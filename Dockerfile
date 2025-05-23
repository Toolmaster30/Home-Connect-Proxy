FROM python:3.11-slim

RUN pip install flask requests

WORKDIR /app

COPY home_connect_proxy.py .
COPY run.sh .

RUN chmod +x run.sh

CMD ["./run.sh"]
