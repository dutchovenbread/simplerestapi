from zipfile import ZipFile
import os

def unzip_locally(local_object_path, directory_to_extract_to):
  if not os.path.isdir(directory_to_extract_to):
    os.mkdir(directory_to_extract_to)
  with ZipFile(local_object_path, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)
  # return a list of paths
  return os.listdir(directory_to_extract_to)
