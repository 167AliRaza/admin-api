from fastapi import FastAPI  
from pymongo import MongoClient

     
    
app = FastAPI()


def get_db_client():
    try:
        client = MongoClient("mongodb+srv://ali:PLztqH3DFAOWYsQy@cluster0.dogd0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        print("Connected to the database")
        return client
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    
        return None
client = get_db_client()
    
db = client["admin_db"]

@app.get("/")
def read_root():
    return {
       "status": "success",
        "error": None,
        "message": "Welcome to the Admins API",
         "data": None
            }

 
 
        
@app.get("/read_admin/{cnic_no}")
def read_admin(cnic_no: int):
    try:
        admin = db.admins.find_one({"cnic": cnic_no})
        if admin is None:
            raise Exception("No record found with this CNIC")
        return {
            "status": "success",
            "error": None,
            "message": "ADMIN read successfully",
            "data": {
                "name": admin["name"],	
                "email": admin["email"],
                "reg_no": admin["cnic"] },
            
        }
    except Exception as e:
        return {
            "status": "failed",
            "error": "Error reading user",
            "message": str(e),
            "data": None
            
        }