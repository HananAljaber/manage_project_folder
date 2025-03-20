import os,shutil
class ProjectManager:
    def __init__(self):
        self.project_path = None   
        
    def create_project_main_folder(self, project_name, project_storage_path):
        self.project_path = os.path.join(project_storage_path, project_name)
        if os.path.exists(self.project_path):
            print(f"The main project folder '{project_name}' already exists.")
        else:
            
            os.makedirs(self.project_path)
            print(f"Main project folder '{project_name}' created successfully at {self.project_path}")
        return self.project_path

    def create_sub_folder(self, folder_path):
        if not self.project_path:
            print("Project main folder is not set. Please create it first.")
            return
        full_path = os.path.join(self.project_path, folder_path)

        if os.path.exists(folder_path):
            print(f"The folder '{folder_path}' already exists.")
        else:
            os.makedirs(full_path, exist_ok=True)
            print(f"Folder '{folder_path}' created successfully at {folder_path}")

    def delete_folder(self, folder_name):
        if not self.project_path:
            print("Project main folder is not set. Please create it first.")
            return
        folder_path = os.path.join(self.project_path, folder_name)
        if os.path.exists(folder_path):
            response = input("Do you want to remove its content? (yes/no): ").strip().lower()
            if response == "yes":
                shutil.rmtree(folder_path)
                print(f"Folder '{folder_name}' has been deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"The folder '{folder_name}' does not exist.")

    def display_menu(self):
        while True:
            print("\nChoose an option:")
            print("1. Create project main folder")
            print("2. Create subfolders")
            print("3. Delete a folder")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ").strip()

            if choice == '1':
                
                project_name = input("Enter your project name: ").strip()
                project_storage_path = input("Enter your project storage path: ").strip()
                
                self.create_project_main_folder(project_name, project_storage_path)

            elif choice == '2':
                if self.project_path:
                    folder_path = input("Enter your subfolder path (e.g., css/frameworks/bootstrap): ").strip()

                    self.create_sub_folder(folder_path)
                else:
                    print("Please create the project main folder first.")

            elif choice == '3':
                if self.project_path:
                    folder_to_delete = input("Enter the folder name you want to delete: ").strip()
                    self.delete_folder(folder_to_delete)
                else:
                    print("Please create the project main folder first.")

            elif choice == '4':
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid choice, please try again.")


def main():
    manager = ProjectManager()
    manager.display_menu()
    print("Project setup is complete!")

if __name__ == "__main__":
    main()