from dotenv import load_dotenv
load_dotenv()
import os
dbUser = os.environ.get("dbUser")
dbPassword= os.environ.get("dbPassword")
dbHost= os.environ.get("dbHost")
dbName= os.environ.get("dbName")
