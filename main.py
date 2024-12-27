from flask import Flask
import json
import os
import logging
import printColors


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ])

app = Flask(__name__)


@app.route('/')
def welcome():
    logging.info('The user accessed the path /')
    return printColors.printBlack('Welcome to my system, Please login')


@app.route('/login/<username>')
def login(username):
    logging.info('The user accessed the path /login/' + username)
    if username in allowed_names:
        return printColors.printGreen('Access granted')
    else:
        logging.warning(f'Name: {username} not found')
        return printColors.printRed('Access denied')


@app.route('/addName/<username>')
def addName(username):
    logging.info('The user accessed the path /addName/' + username)
    if not username in allowed_names:
        allowed_names.add(username)
        with open("config.json", "w") as config:
            json.dump(list(allowed_names), config)
        logging.info(f'Name: {username} added successfully')
        return printColors.printGreen('Name added successfully')
    else:
        logging.warning(f'Name: {username} already exists')
        return printColors.printRed('Name already exists')


with open("config.json") as config:
    try:
        allowed_names_list = json.load(config)
        allowed_names = set(allowed_names_list)
        logging.info(f'Allowed names: {allowed_names}')
    except:
        logging.critical('Error: Config file missing')

if __name__ == '__main__':
    app.run(host=os.environ.get("HOST_IP"), port=80)
