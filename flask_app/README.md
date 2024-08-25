# 1. Environment Setup: create a python virtual environment
    - sudo apt install python3-venv
    - python3 -m venv venv



# 2. Install packages: install necessary packages
    - pip install flask



# 3. Create App: create flask_app folder and necesscary files
    - mkdir flask_app
    - cd flask_app/

    - touch requirement.txt
    - touch README.md

    - mkdir app
    - cd app/

    - touch __init__.py
    - touch app.py
    - touch utils.py

#                        OR

    - Unzip the flask_app.zip



# 4. Run the app:
    - cd flask_app/app/
    - python app.py

    // This will generate the default url locally (http://127.0.0.1:5000)
    


# 5. Check the API's
    // This will output the success messgae
    - curl http://127.0.0.1:5000/fetch-data/

    // This will output the stored precessed data
    - curl http://127.0.0.1:5000/get-processed-data/






