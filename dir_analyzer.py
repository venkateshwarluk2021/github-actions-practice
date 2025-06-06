import os

def get_folder_size(folder_path):
  total_size=0
  for dirpath, dirnames, filenames in os.walk(folder_path):
    for f in filenames:
      fp = os.path.join(dirpath, f)
      if(os.path.isfile(fp)):
        total_size+=os.path.getsize(fp)
  return total_size

def format_size(bytes_size):
  mb = bytes_size / ( 1024 )
  return f"{mb:.4f} KB"


def analyze_directory(root_folder):
  print(f"Directory size analysis for : {root_folder}\n")
  for item in os.listdir(root_folder):
    item_path = os.path.join(root_folder, item)
    if os.path.isdir(item_path):
      size=get_folder_size(item_path)
      print(f"{item:30} : {format_size(size)}")


target_directory = "."
analyze_directory(target_directory)
