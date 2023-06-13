FROM python:3.10.11
WORKDIR /Scripts/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
EXPOSE 5000
CMD [ "flask", "run", "--host=127.0.0.1" ]