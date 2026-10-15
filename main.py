import diary_manager

def ask_for_date():
    while True:
        date_text = input('Date (MM-DD-YYYY): ').strip()
        try:
            diary_manager.check_date(date_text)
            return date_text
        except ValueError as e:
            print(f'Problem processing date value. Please try again!: {e}')
def main():
    filename = input('Diary file to use: ').strip()
    
    while True:
        print()
        print(f'Diary file: {filename}')
        print('1. Add entry')
        print('2. Print entries for a date')
        print('3. Load a different diary file')
        print('4. Quit')
        choice = input('> ').strip()
        
        if choice == '1':
            date_text = ask_for_date()
            text = input('Entry: ').strip()
            diary_manager.add_entry(filename, date_text, text)
            print('Saved')
        
        elif choice == '2':
            date_text = ask_for_date()
            entries = diary_manager.read_entries(filename)
            matches = diary_manager.filter_entries(entries, date_text)
            if len(matches) == 0:
                print('No entries found.')
            for entry_date, text in matches:
                print(f'{entry_date}: {text}')
        
        elif choice == '3':
            filename = input('Diary file to load: ').strip()
            
        elif choice == '4':
            break
        
        else:
            print('Please pick a number from 1 to 4.')

if __name__ == '__main__':
    main()
    
                            
                        