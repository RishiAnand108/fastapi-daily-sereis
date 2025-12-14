import os
from fastapi import APIRouter, UploadFile, File, BackgroundTasks, HTTPException
from services.tasks import log_file_upload

router = APIRouter(
    prefix='/files',
    tags=['File Uploads']
)

UPLOAD_DIR="uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):
    #validate file type
    if not file.filename.endswitch((".png",".jpg",'.jpeg','.pdf')):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    file_path  = os.path.join(UPLOAD_DIR, file.filename)

    #Save File
    with open(file_path,"wb") as f:
        content = await file.read()
        f.write(content)

    # Background Task
    background_tasks.add_task(log_file_upload, file.filename)

    return{
        "filename":file.filename,
        "message":"File UPloaded Successfully"
    }    