import os
from datetime import datetime
import re

import pyperclip

import notespy.constants
from cloudbox import clipboard, constants, text

def raw_text(text):
    
    if type(text) == str:
        text = text.replace('\\', '/')
        text = text.replace('\n', ' ')
    else:
        text = None
        print("Must be string")
        
    return text
        
def example_icloud_note():
    
    dailynotesdir = notespy.constants.dailydir
    with open(os.path.join(dailynotesdir, r"example_icloud.txt"), 'r') as file:
        # Replace \ characters in path names written in the text
        # with '/', so it doesn't need to be escaped    
        text = raw_text(file.read())
        
    return text

def find_date(text):
    
    found_dates = []
    
    centuries = '|'.join([str(num) for num in range(19, 22)])
    years = '|'.join([str(num).zfill(2) for num in range(0, 100)])
    months = '|'.join([str(num).zfill(2) for num in range(0, 12)])
    days = '|'.join([str(num).zfill(2) for num in range(0, 31)])

    datespattern = f"({centuries})({years})({months})({days})"
    
    results = re.findall(datespattern, text)
    
    if results:
        found_dates = [''.join(result) for result in results]
    else:
        pass
            
    return found_dates

def new_note_path(found_dates, words):
    
    dailynotesdir = notespy.constants.dailydir

    if len(found_dates) == 1:  
        
        date = found_dates[0]
        tag = words[1]
        writepath = os.path.join(dailynotesdir, f"{date}_{tag}.txt")

    elif len(found_dates) > 1:
        
        date = found_dates[0]
        print(f"Found multiple dates, choosing the first one: {date}")
        tag = words[1]
        writepath = os.path.join(dailynotesdir, f"{date}_{tag}.txt")

    elif len(found_dates) == 0:
        
        today = datetime.today()
        year, month, day = [str(today.year),
                            str(today.month).zfill(2),
                            str(today.day).zfill(2)]
                
        date = f'{year}{month}{day}'        
        print(f"No date found, using today's date: {date}")
        tag = words[0]
        writepath = os.path.join(dailynotesdir, f"{date}_{tag}.txt")

    return writepath

def write_note_from_clipboard(**kwargs):

    text = kwargs.get('text', raw_text(pyperclip.paste()))
    words = text.split(' ')
    
    dailynotesdir = notespy.constants.dailydir
    found_dates = find_date(text)
    writepath = new_note_path(found_dates, words)

    if os.path.exists(writepath):
        with open(writepath, 'a') as file:
            file.write(f'\n{text}')
            print(f'Added to existing note at: {writepath}')
    else:
        with open(writepath, 'w') as file:
            file.write(text)
            print(f'Saved new note at: {writepath}')    
        
def test_write_note_from_clipboard():
    
    write_note_from_clipboard(text=example_icloud_note())