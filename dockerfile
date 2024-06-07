FROM python:3.9-slim-buster

#Create and set the working directory
WORKDIR /app

#Copy only the requirements file
COPY requirements.txt .
COPY ./requirements.txt /app

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy the entire application
COPY . .


#Expose the port your
EXPOSE 5000

#Specify the command to run on container start
CMD ["python", "src/server.py"]