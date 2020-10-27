FROM python:3
RUN pip3 install yfinance
COPY main.py /tmp/
CMD ["python", "/tmp/main.py"]