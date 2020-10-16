# HTTP Redirection Check with Python

This http redirection package helps you to find the web site whether has http redirection or not?

 # 1. Installation & Build
  * Clone this repo ``` git clone https://github.com/SemihOzden/http_redirection_check.git ```
  * Create your virtual environment in your downloaded repo by typing in your terminal
  ``` python3.6 -m venv /path/of/your/venv```
  * run your venv by typing ``` source /venv/bin/activate ```
  * Type ``` pip install -r requirements.txt ```
  * your development environment is ready.
  
 # 2. Run Options 
  * You can run this package from terminal by typing following commands
    ``` python3.6 https-redirection-check/app.py -i ```
    OR 
    ``` python3.6 https-redirection-check/app.py -u http://example.com ```
 
 # 3. CLI Arguments 
 
 CLI with Arguments
* for search URL ```-u --url``` // -u option must be set
* for interactivity ```-i --interactivity``` action='store_true' // This means that if -i is given as an argument, user will use terminal prompt to enter values one by one