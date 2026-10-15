from datetime import datetime

DATE_FORMAT = '%m-%d-%Y'
SEPARATOR = ' | '

def check_date(date_text):
    datetime.strptime(date_text, DATE_FORMAT)
    
def add_entry(filename, date_text, text):
    with open(filename, 'a') as diary_file:
        diary_file.write(f'{date_text}{SEPARATOR}{text}\n')

def read_entries(filename):
    entries = []
    try:
        with open(filename) as diary_file:
            for line in diary_file:
                date_text, text = line.strip().split(SEPARATOR, 1)
                entries.append((date_text, text))
    
    except FileNotFoundError:
        pass 
    return entries

def filter_entries(entries, date_text):
    return [entry for entry in entries if entry [0] == date_text]
    
    

