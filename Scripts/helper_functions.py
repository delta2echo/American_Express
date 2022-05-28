#--- imports needed for retrieving data
import zipfile
import tarfile



def unzip_files(file_name):
  """
    Will extract provided zip or tar.gz file.
  """
  #---Determine File Type
  if '.zip' in file_name.lower()[-4:]:
    zip_ref = zipfile.ZipFile(file_name)
  elif '.tar.gz' in file_name.lower()[-7:]:
    zip_ref = tarfile.open(file_name)
  else:
    print("File must be a '.zip' or '.tar.gz', file has not been extracted.")
    return None
    
  #---Extract the downloaded file:   
  zip_ref.extractall()
  zip_ref.close()
  print('Done!')