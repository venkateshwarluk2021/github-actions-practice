# use an artificial Python Image
FROM python:3.12-slim

#set working directory
WORKDIR /app

#Copy code
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

#default command
CMD ["pytest"]