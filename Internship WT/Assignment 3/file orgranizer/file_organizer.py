# #3.File Organizer – Write a script that sorts files in a folder into subfolders (e.g., images, documents, videos).
import os
import shutil

# Step 1: Create Demo Files
def create_demo_files(base_path):
    demo_files = {
        "Images": ["photo1.jpg", "photo2.png", "pic.gif"],
        "Videos": ["movie.mp4", "clip.mkv"],
        "Documents": ["report.docx", "notes.txt", "slides.pptx"],
        "Music": ["song.mp3", "tune.wav"],
        "Archives": ["backup.zip", "data.rar"],
        "Code": ["script.py", "program.cpp", "index.html"],
        "Others": ["randomfile.xyz", "unknownfile.bin"]
    }

    for category, files in demo_files.items():
        for file in files:
            file_path = os.path.join(base_path, file)
            # Create fake file with text content
            with open(file_path, "w") as f:
                f.write(f"This is a demo file for {category}: {file}\n")

    print("✅ Demo files created in:", base_path)


# Step 2: Organize Files
def organize_files(folder_path):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Music": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"],
        "Others": []
    }

    # Create category folders
    for folder in file_types.keys():
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    # Sort files
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        moved = False
        for folder, extensions in file_types.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", file))

    print("✅ Files organized successfully!")


# Run Demo
if __name__ == "__main__":
    current_folder = os.getcwd()  
    
    # Create Demo Files
    create_demo_files(current_folder)

    # Organize Demo Files
    organize_files(current_folder)


# import os
# import shutil


# def revert_organization(folder_path):
#     if not os.path.exists(folder_path):
#         print("Error: Folder not found.")
#         return

#     # Loop through all subfolders
#     for subfolder in os.listdir(folder_path):
#         subfolder_path = os.path.join(folder_path, subfolder)

#         # Only check inside folders (not files directly in main folder)
#         if os.path.isdir(subfolder_path):
#             for file in os.listdir(subfolder_path):
#                 file_path = os.path.join(subfolder_path, file)
#                 # Move file back to main folder
#                 shutil.move(file_path, folder_path)

#     print("Files have been reverted back to the main folder.")


# # Example usage
# folder_path = r"#"  # Change this to your folder
# revert_organization(folder_path)
