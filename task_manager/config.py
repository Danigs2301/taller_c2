import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/taskdb")
