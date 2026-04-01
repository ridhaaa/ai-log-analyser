FROM python
WORKDIR /app
COPY . /app
CMD ["python3", "app.py"]
RUN pip install -r requirements.txt

