# dockerfile
# We inherit the Python 3 image.
FROM python:3.8.3
# Copy the requirements file in order to install Python dependencies
COPY requirements.txt .
# Install Python dependencies
RUN pip install -r requirements.txt
# Copy the entire source folder
COPY . .
# Install wkhtmltopdf library
RUN apt-get -y update
# Upgrade already installed packages:
# RUN apt-get -y upgrade
RUN apt-get -y install openssl libssl-dev
RUN apt-get -y install wkhtmltopdf
# Running the app
CMD [ "python3", "--version" ]
CMD [ "python3", "main.py" ]
