import os
from datetime import datetime

class CloudStorageExplorer:
    def __init__(self, storage_path="my_cloud_bucket"):
        self.storage_path = storage_path
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)
        print(f"Connected to Cloud Storage: {storage_path}")

    def list_files(self):
        print("\n--- Files in Cloud Storage ---")
        files = os.listdir(self.storage_path)
        if not files:
            print("No files found.")
            return
        for idx, f in enumerate(files, 1):
            file_path = os.path.join(self.storage_path, f)
            size = os.path.getsize(file_path)
            print(f"{idx}. {f} - {size} bytes")

    def upload_file(self, file_name, content="Sample cloud content"):
        file_path = os.path.join(self.storage_path, file_name)
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Uploaded: {file_name}")

    def download_file(self, file_name):
        file_path = os.path.join(self.storage_path, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                print(f"Content of {file_name}: {f.read()}")
        else:
            print("File not found!")

    def delete_file(self, file_name):
        file_path = os.path.join(self.storage_path, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_name}")
        else:
            print("File not found!")

    def create_folder(self, folder_name):
        path = os.path.join(self.storage_path, folder_name)
        os.makedirs(path, exist_ok=True)
        print(f"Folder created: {folder_name}")

if __name__ == "__main__":
    explorer = CloudStorageExplorer()
    print("=== CLOUD STORAGE EXPLORER BY SAILAJA ===")
    explorer.upload_file("report.txt", "Codtech Task 1 by Sailaja - Cloud Storage Explorer")
    explorer.upload_file("data.csv", "id,name\n1,Sailaja")
    explorer.create_folder("images")
    explorer.list_files()
    explorer.download_file("report.txt")
    explorer.list_files()
    print("Project Completed Successfully!")