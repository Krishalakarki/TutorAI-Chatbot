import os
import shutil
from fastapi import UploadFile
from pathlib import Path

UPLOAD_DIR = "./uploaded_docs"

def save_uploaded_files(files: list[UploadFile]) -> list[str]:
    # ✅ Ensure upload folder exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    
    saved_paths = []
    
    for file in files:
        # Use Path for cross-platform compatibility
        safe_filename = Path(file.filename).name  # removes any folder paths
        save_path = Path(UPLOAD_DIR) / safe_filename
        
        # Save the uploaded file
        with open(save_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        
        saved_paths.append(str(save_path))
    
    return saved_paths
