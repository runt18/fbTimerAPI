import os
import models
from flask import Flask
from flask import jsonify
from bson.objectid import ObjectId
from bson.errors import InvalidId
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)   # create our flask app

# --------- Database Connection ---------
# MongoDB connection to MongoLab's database
app.config['MONGODB_SETTINGS'] = {'HOST':os.environ.get('MONGOLAB_URI'),'DB': 'fbTimeDB'}
app.logger.debug("Connecting to MongoLabs")
db = MongoEngine(app) # connect MongoEngine with Flask App


# Logging sessions API
@app.route("/fbusage/<name>")
def start_session(name):
  try:
      ObjectId(name)
      users = models.UserDocument.objects(id = name)
  except (InvalidId, ValueError, TypeError):
      users = []

  if(len(users) == 0):
    user = {"status": "No love for the timer", "message": "The user you mentioned loves Facebook too much to download the extension"}
  else:
    user = {"status": "OK", "data": users[0].to_mongo().to_dict()}
    del user['data']['_id']

  return jsonify(user)

# start the webserver
if __name__ == "__main__":
    app.debug = True

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)