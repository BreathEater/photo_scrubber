from fastapi import APIRouter 

router = APIRouter()

@router.get("/log/{session_id}")
async def get_log(session_id: str):
   with open(f"uploads/{session_id}/log.txt", "r") as f:
       return {"log": f.read()}


