from tkinter import Tk

import pandas as pd

from dropbox import Dropbox
from cloudbox import constants

def get_images_result():
    token = constants.token
    dbx = Dropbox(token)
    
    result = dbx.files_list_folder(constants.images_path)
    return result.entries

def get_images_df():
    """
    return a dataframe of images uploaded to
    constants.images_path
    """
    result = get_images_result()
    dfdict = {}
    params = ['name',
              'path_display',
              'client_modified']
    images_dfs = []
    for i, file in enumerate(result):

        dfdict['name'] = file.name
        dfdict['path_display'] = file.path_display
        dfdict['client_modified'] = file.client_modified
        dfdict['server_modified'] = file.server_modified
        df = pd.DataFrame(dfdict, index=[i])
        images_dfs.append(df)

    images_df = pd.concat(images_dfs)
    return images_df

def get_direct_link(filename="measurement_rois.png"):

    token = constants.token
    dbx = Dropbox(token)
    path = f'{constants.images_path}{filename}'

    link = dbx.sharing_create_shared_link(path=path, short_url=False)
    direct_url = link.url.replace('dl=0', 'raw=true')
    print(direct_url)

    return direct_url
def load_clipboard(string):
    """
    Add the string passed to load_clipboard
    to the system clipboard
    """
    # If this is run on cmd using AHK, the string
    # loaded to the clipboard will disappear once
    # the python process executes, so we wait 5 sec
    # for the user to paste the url before destroying
    # the root Tk()
    if type(string) == str:
        root = Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(string)
        root.after(5000, root.destroy)
        root.mainloop()
    else:
        print("not a string")

def recently_modified_link():
    """
    Return the direct link to the most modified 
    uploaded image in constants.images_path on 
    the user dropbox
    """
    df = get_images_df()
    df = df.sort_values(by='client_modified', ascending=False, ignore_index=True)
    filename = df.loc[0, 'name']

    direct_url = get_direct_link(filename=filename)
    load_clipboard(direct_url)
    return direct_url

def recently_uploaded_link():
    """
    Return the direct link to the most recently 
    uploaded image in constants.images_path on 
    the user dropbox
    """
    df = get_images_df()
    df = df.sort_values(by='server_modified', ascending=False, ignore_index=True)
    filename = df.loc[0, 'name']

    direct_url = get_direct_link(filename=filename)
    load_clipboard(direct_url)
    return direct_url
