import os
import json
from flask import Flask
import logging
import printColors

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
     handlers=[
         logging.FileHandler("app.log"),  # Log to a file
         logging.StreamHandler()          # Also log to the console
     ]
    )

app = Flask(__name__)

@app.route("/")
def hello():
    logging.info("The user has accessed the path /")
    return printColors.printBlack("Welcome to system, Please login")


@app.route("/addName/<name>")
def addName(name):
    allowed_names.add(name)
    logging.info("The user " + name + " has added to permissions user list")
    with open("config.json", "w") as file:
       json.dump(list(allowed_names), file, indent=4)
    msg = "Name " + name + " Added successfully"
    logging.info(msg)
    return printColors.printGreen(msg)


@app.route("/login/<name>")
def newPath(name):
    if name in allowed_names:
        logging.info("name " + name + " exists in the list")
        return printColors.printGreen("Access Granted")
    logging.warning("name " + name + " doesnt not exists in the list")
    return printColors.printRed("Access Denied")

          
with open("config.json") as config:
    try:
        allowed_names_list = json.load(config)
        for name in allowed_names_list:
            logging.info(name + " is approved user")
        allowed_names = set(allowed_names_list)
    except Exception as e:
        logging.critical("config file missing :" + str(e))
        

if __name__ == "__main__":
    app.run(host=os.environ.get("HOST_IP"), port=80)



