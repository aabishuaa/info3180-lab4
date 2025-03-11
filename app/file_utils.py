import os



def get_uploaded_images():
    upload_folder = os.path.join(os.getcwd(), 'uploads')  
    image_files = []

    
    for subdir, dirs, files in os.walk(upload_folder):
        for file in files:
            if file.endswith(('jpg', 'png')):  
                image_files.append(file)

    return image_files