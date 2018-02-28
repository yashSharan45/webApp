# WebApp-Python

STEPS FOR GIT
===============================================================
PUSH
1. In your Desktop or Documents or wherever's terminal type -> 
	git clone https://github.com/aneeshverma04/WebApp-Python.git

NOTE: make sure wherever you are cloning the repo, the folder name shouldn't have a space    	   between the words e.g. $ /Desktop/Flask Project/WebApp-Python will not work when        
      installing flask 

2. Make your own branch, my branch would be ->
	git branch aneesh1      # aneesh1 is branch name
3. Switch to branch ->
	git checkout aneesh1
4. Add/Delete your code 
5. Then add your code to local git ->
	git add .
6. Commit your code ->
	git commit -m "Message about today's work done "
7. Set up an alias for 'origin' ->
	git remote add origin https://github.com/aneeshverma04/WebApp-Python.git
8. Push your code to github ->
	git push origin aneesh1  # Your branch name instead of aneesh1
							 # Enter your username and password when asked
 							 
PULL
1. git pull origin aneesh1 

Merge
1. When need to merge we will create a pull request on github


STEPS FOR SETTING UP PYTHON AND FLASK
================================================================
When you will clone the repo, virtual environment would already have been set up so

Commands to run our Web-App:
1. . venv/bin/activate  #flask will already be installed
2. python app.py   #Now open localhost:5000 and see our first page .. to quit press Ctrl+c 

**
Still if you want to know the steps to Set Up flask ->
1. Make sure you have python 2.7 installed. ( Command : python --version )
2. Set up virtual environment. ( Command : virtualenv venv ) # venv is name of virtual env
3. Activate virtual environment. ( Command : . venv/bin/activate)
4. Install flask. ( Command : pip install flask )
5. python app.py





OTHER
pip install Flask-Mail


pip freeze > requirements.txt
pip install -r requirements.txt