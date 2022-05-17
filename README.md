
## Call google search API

### How to run the script?

 - Clone the repo to your local machine
 - Copy the received .env file into the directory of the Repo
 - Create virtual environment for Python using the requirements.txt file. For help see [venv](https://docs.python.org/3/library/venv.html)
 - Activate the Python virtual environment 

### Script 1: simple main function

 - On root directory of the repo run the following command
 
> python main.py

### Script 2: API call with FASTAPI framework

 - Move to the src directory and run the following command
 
 >  uvicorn main:app --reload
 
 - On your browser visit (http://127.0.0.1:8000/docs)
