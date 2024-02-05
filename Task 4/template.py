import os
from pathlib import Path

root_dir = Path(os.getcwd())


def create_project_structure(root_dir):
   """Creates the specified project structure with .py files in subfolders."""

   # Create main directories
   os.makedirs(os.path.join(root_dir, "src"), exist_ok=True)

   # Create subdirectories within src and their respective .py files
   sub_dirs = [
       ("data_collection", "data_collection.py"),
       ("data_preprocessing", "data_preprocessing.py"),
       ("data_transformation", "data_transformation.py"),
       ("model_training_evaluation", "model_training_evaluation.py"),
       ("prediction_pipeline","predict_pipeline.py")
   ]
   for sub_dir, py_file in sub_dirs:
       dir_path = os.path.join(root_dir, "src", sub_dir)
       os.makedirs(dir_path, exist_ok=True)
       open(os.path.join(dir_path, py_file), "w").close()  # Create empty .py file

   # Create __init__.py files in each directory
   for dir_path, _, _ in os.walk(root_dir):
       if "__init__.py" not in os.listdir(dir_path):
           open(os.path.join(dir_path, "__init__.py"), "w").close()



if __name__ == "__main__":
    create_project_structure(root_dir)
