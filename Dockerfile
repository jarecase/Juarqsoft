FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP /usr/src/app/src/app.py
ENV FLASK_ENV development
ENV PORT $PORT

#CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
ENTRYPOINT ["python3"]
CMD ["src/app.py"]