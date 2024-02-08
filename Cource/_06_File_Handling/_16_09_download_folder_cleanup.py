import os
import shutil

# Define your download folder and destination folders for each file type
download_folder = "C:\\Users\Santosh Sankpal\Downloads"
image_folder = "C:\\Users\Santosh Sankpal\Desktop\picutes"
document_folder = "C:\\Users\Santosh Sankpal\Desktop\pdf"
video_folder = "C:\\Users\Santosh Sankpal\Desktop\\video"
other_folder = "C:\\Users\Santosh Sankpal\Desktop\other"

# Create the destination folders if they don't exist
for folder in [image_folder, document_folder, video_folder, other_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to categorize files
def categorize_file(file_path):
    _, file_extension = os.path.splitext(file_path.lower())
    if file_extension in (".jpg", ".jpeg", ".png", ".gif"):
        return "image"
    elif file_extension in (".pdf", ".doc", ".docx", ".txt"):
        return "document"
    elif file_extension in (".mp4", ".avi", ".mkv", ".mov"):
        return "video"
    else:
        return "other"

# Iterate through files in the download folder and move them to the appropriate folder
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    if os.path.isfile(file_path):
        category = categorize_file(file_path)
        if category == "image":
            shutil.move(file_path, os.path.join(image_folder, filename))
        elif category == "document":
            shutil.move(file_path, os.path.join(document_folder, filename))
        elif category == "video":
            shutil.move(file_path, os.path.join(video_folder, filename))
        else:
            shutil.move(file_path, os.path.join(other_folder, filename))

print("Download folder cleanup completed.")
