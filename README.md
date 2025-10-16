# 📝 Notes Manager

**🇬🇧 Description:**  
This is a simple **Notes Manager** application written in Python. It allows users to **create, view, edit, and delete notes**, and stores them in a JSON file. Each note contains an **ID, title, body, and timestamp**.

---

## ⚡ Features
- Add a new note with title and body
- List all notes with IDs and timestamps
- View a specific note by ID
- Edit a note by ID
- Delete a note by ID
- Stores notes in `notes.json` file

---

## 🛠 Technologies
- Python 3
- JSON for storage
- File I/O
- Datetime module

---

## 💻 Example Usage

```python
# Add a new note
Enter note title: Shopping list
Enter note body: Buy milk, eggs, and bread
Note added!

# List all notes
ID: 1, Title: Shopping list, Date: 2025-10-16T14:30:15.123456

# View a note
Enter note ID to view: 1
Title: Shopping list
Body: Buy milk, eggs, and bread
Date: 2025-10-16T14:30:15.123456

# Edit a note
Enter note ID to edit: 1
Enter new title (old: Shopping list): Grocery list
Enter new body (old: Buy milk, eggs, and bread): Buy milk, eggs, bread, and butter
Note updated!

# Delete a note
Enter note ID to delete: 1
Note deleted!

## 📂 File Structure
```notes_manager/
├── notes.py       # Main Python script
├── notes.json     # JSON file storing notes
└── README.md      # Project documentation
```

## 🚀 How to Run

1. Clone the repository:
```
git clone https://github.com/yourusername/notes_manager.git
```

2. Navigate to the project folder:
```
cd notes_manager
```

3. Run the script:
```
python notes.py
```

✨ “Keep your notes organized and never forget anything!”
