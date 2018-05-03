
FROM frolvlad/alpine-python3
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "python", "app.py"]