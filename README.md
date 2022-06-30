# pya-web3

1) Create Virtual environment [Windows]
    # python3 -m env <name_of_virtualenv>
  #  python -m venv ./env

2) See struture of virtual environment
  # tree env

3) Activate Virtual Environment

 # .\env\Scripts\activate

4) Install python packages in virtual environment
 # pip install flask web3 

6) Create requirements.txt

# pip3 freeze > requirements.txt 
 
6) Run the app
 
python app.py

# PYTHON VERSION python --version 
Python 3.10.4

7) Login into https://www.pythonanywhere.com

8) Create Web App
 pythonanywhere > Web > Add a new web app
 Then choose "Flask" framework and latest python version

 9) After app is created. Open Bash console
 pythonanywhere > Console > Bash Console

 10) Git clone project pya_web3
 > git clone https://github.com/mmmwembe/pya_web3.git

 11) Change directory into the pya_web3 folder
 > cd pya_web3

 12) Print Working Directory
 > pwd 

13) Get python version
> python --version
3.9.5

 14) Create virtualenv
>  mkvirtualenv env --python=/usr/bin/python3.9

15) In virtual env, install requirements.txt
(env) > pip install -r requirements.txt

NOTE: The above command resulted in error: 
ERROR: Could not find a version that satisfies the requirement pywin32==304 (from versions: none)ERROR: No matching distribution found for pywin32==304

16) Manually installed requirements"
(env)> pip install flask
(env)> pip install web3
(env)> pip install eth-brownie
(env)> pip install python-dotenv
(env)> pip install eth-account

Then save requirements.txt again so that its upto date

17) Go back to Web to configure app
pythonanywhere > Web

source: pya_web3

Edit configuration file :
(a) update the project_home directory path to align with your project
(b) Ensure that the import is importing from the app.py function eg:
"from app import app as application" instead of "from flask_app import app as application"

18) To workon env virtual environment in console
> workon env

19) To deactivate environment
> deactivate 

20) https://www.stitcher.com/show/running-in-production/episode/a-cryptocurrency-powered-e-commerce-store-called-strmline-68615168


21) Add dotenv so we can access env variables
pip install python-dotenv

22) pip install web3 eth-brownie flask

23) PythonAnywhere has a whitelisting of allowed websites:
https://www.pythonanywhere.com/whitelist/