FROM alpine:latest
RUN apk update 
RUN apk add python3 
RUN apk add py3-pip
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3","app.py"]
