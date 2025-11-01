from fastapi import APIRouter, Form, HTTPException
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter(prefix="/students", tags=["Students"])

# Initialize Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@router.post("/register")
async def register_student(
    name: str = Form(...),
    email: str = Form(...),
    phone_number: str = Form(...),
    dob: str = Form(...),
    gender: str = Form(...),
    college: str = Form(...),
    department: str = Form(...),
    year_of_study: str = Form(...),
    course: str = Form(...),
    address: str = Form(...),
    
    
    
):
    """
    Register a new student and store details in Supabase.
    """
    try:
        # Check for duplicate email
        existing = supabase.table("students").select("*").eq("email", email).execute()
        if existing.data:
            raise HTTPException(status_code=400, detail="Email already registered")

        # Prepare student data
        data = {
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "dob": dob,
            "gender": gender,
            "college": college,
            "department": department,
            "course": course,
            "year_of_study": year_of_study,
            "address": address,
        }

        # Insert into Supabase table
       
        response = supabase.table("students").insert(data).execute()
       
        return {"message": "Student registered successfully", "data": response.data}

    except Exception as e:
        # raise HTTPException(status_code=500, detail=f"Error saving student: {str(e)}")
        print("❌ Backend error:", str(e))
        return {"error": str(e)}


@router.get("/all")
async def get_all_students():
    """
    Fetch all student records from Supabase.
    """
    try:
        response = supabase.table("students").select("*").execute()
        return {"students": response.data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching students: {str(e)}")
