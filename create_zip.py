import os
import zipfile

def create_zip():
    zip_file = 'vellore-aqi-predictor.zip'
    
    # List of files to include
    files_to_zip = [
        'app.py',
        'requirements.txt',
        'Procfile',
        'train_model.py',
        '.ebextensions/python.config'
    ]
    
    # Create a ZIP file
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add each file to the ZIP
        for file in files_to_zip:
            if os.path.exists(file):
                zipf.write(file)
        
        # Add templates directory
        if os.path.exists('templates'):
            for root, dirs, files in os.walk('templates'):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path)
                    zipf.write(file_path, arcname)
        
        # Add model directory
        if os.path.exists('model'):
            for root, dirs, files in os.walk('model'):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path)
                    zipf.write(file_path, arcname)

if __name__ == '__main__':
    create_zip()
    print("Created vellore-aqi-predictor.zip successfully!")
