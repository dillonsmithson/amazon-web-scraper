# Amazon Web Scraper
To keep up-to-date with current trends in the market in regards to CPUs and GPUs, I wanted to create this program as a way to keep track of availabilty and pricing of a multitude of different components across a multitude of different websites.
However, for now, this will just be limited to Amazon's listings, but eventually will expand into Newegg, Bestbuy, etc.

Below is a quick start guide on how to get the program running and what each file is doing. 

## Creating and starting a virtual environment
You don't necessarily have to do this, but since this is a Python project and its best to keep all your libraries contained within a venv, I would suggest doing this. It's super simple to set up. 

First you'll need PIP (Pip installs packages). If you don't have PIP, I would suggest going here and learning how to setup pip since it's required to run the 'requirement.txt' file. 

Start by beginning a Command Prompt and navigating to the folder you wish to place the Virtual Environment. Then enter the following command, where 'Name' is the name you give the virtual environment

```
python -m venv 'Name'
```

Once you have create your virtual environment, you should now see a folder with the name you gave it. Navigate to the folder in the command terminal and navigate to the **Scripts** folder. Then run the following command

```
Activate.bat
```

This will start the virtual environment and you can now install the requirements.txt file. 

## Installing Requirements.txt
Once in the virtual environment, enter the following command to install the depencies for the project

```
pip install -r requirements.txt
```

Once this has been completed, you can now run the main.py file in the **ProjectFiles** folder which will start the program

```
python main.py
```
