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
    title = input('Введите заголовок заметки: ')
    body = input('Введите тело заметки: ')
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
    print('Заметка добавлена!')

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")

def view_note():
    note_id = int(input('Введите ID заметки для просмотра: '))
    notes = load_notes()
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['body']}")
        print(f"Дата: {note['timestamp']}")
    else:
        print('Заметка не найдена.')

def edit_note():
    note_id = int(input('Введите ID заметки для редактирования: '))
    notes = load_notes()
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        note['title'] = input(f"Введите новый заголовок (старый: {note['title']}): ")
        note['body'] = input(f"Введите новое тело заметки (старое: {note['body']}): ")
        note['timestamp'] = datetime.datetime.now().isoformat()
        save_notes(notes)
        print('Заметка обновлена!')
    else:
        print('Заметка не найдена.')

def delete_note():
    note_id = int(input('Введите ID заметки для удаления: '))
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print('Заметка удалена!')

def main():
    while True:
        print("\nКоманды:")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Просмотреть заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти")
        
        command = input('Введите команду: ')
        
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
            print('Неверная команда, попробуйте снова.')

if __name__ == "__main__":
    main()
