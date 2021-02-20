import requests

class YaUploader:
  def __init__(self, token: str):
    self.token = token

  def new_folder(self,file_name: str):
    response = requests.put(
        "https://cloud-api.yandex.net/v1/disk/resources",
        params={"path": file_name},
        headers={"Authorization": f"OAuth {self.token}"},
    )
    result = str(response) 
    return(result)