from os import path
from cloudbox import secrets

token = secrets.token
images_path = '/images/'
local_images_path = "C:/Users/John Cooper/Dropbox/images/"
local_text_path = "C:/Users/John Cooper/Dropbox/text/"

def package_path(**kwargs):
    """
    Return the path to the local installation
    of cloudbox
    """
    import cloudbox
    file = cloudbox.__file__
    try:
        package_path = path.dirname(file)
    except Exception as exc: # this will work on windows
        package_path = None
        print(f"No package_path found:\n{exc}")
    
    return package_path

package_path = package_path()