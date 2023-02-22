from model import Note, NotebookEditor, NotebookFileOperation

class Controller:
    def __init__(self):
        self.editor = NotebookEditor()
        self.file = NotebookFileOperation()
    
    def saveNote(self, note: Note):
        self.editor.add_note(note)

    def read_all_notes(self):
        notes = self.editor.get_all_notes()
        return notes

    def read_note(self, id: str):
        self.check_id(id)
        notes = self.editor.get_all_notes()
        return notes[id]

    def update_note(self, id: str, note: Note):
        self.check_id(id)
        self.editor.edit_note(id, note)

    def delete_note(self, id: str):
        self.check_id(id)
        self.editor.delete_note(id)
    
    def check_id(self, id: str):
        notes = self.editor.get_all_notes()
        if not id in notes.keys():
            raise ValueError("Нет заметки с таким идентификационным номером!")

    def save_json(self):
        self.file.save_json()

    def sort_notes(self, date):
        notes = self.editor.sort_notes(date)
        return notes