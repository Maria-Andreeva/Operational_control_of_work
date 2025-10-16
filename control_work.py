import json
import os
import datetime

NOTES_FILE = 'notes.json'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

def create_note():
    title = input('Enter note title: ')
    body = input('Enter note body: ')
    timestamp = datetime.datetime.now().isoformat()
    note = {
        'id': len(load_notes()) + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print('Note added!')

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}, Title: {note['title']}, Date: {note['timestamp']}")

def view_note():
    note_id = int(input('Enter note ID to view: '))
    notes = load_notes()
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        print(f"Title: {note['title']}")
        print(f"Body: {note['body']}")
        print(f"Date: {note['timestamp']}")
    else:
        print('Note not found.')

def edit_note():
    note_id = int(input('Enter note ID to edit: '))
    notes = load_notes()
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        note['title'] = input(f"Enter new title (old: {note['title']}): ")
        note['body'] = input(f"Enter new body (old: {note['body']}): ")
        note['timestamp'] = datetime.datetime.now().isoformat()
        save_notes(notes)
        print('Note updated!')
    else:
        print('Note not found.')

def delete_note():
    note_id = int(input('Enter note ID to delete: '))
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print('Note deleted!')

def main():
    while True:
        print("\nCommands:")
        print("1. Add note")
        print("2. List all notes")
        print("3. View note")
        print("4. Edit note")
        print("5. Delete note")
        print("6. Exit")
        
        command = input('Enter command: ')
        
        if command == '1':
            create_note()
        elif command == '2':
            list_notes()
        elif command == '3':
            view_note()
        elif command == '4':
            edit_note()
        elif command == '5':
            delete_note()
        elif command == '6':
            break
        else:
            print('Invalid command, please try again.')

if __name__ == "__main__":
    main()
