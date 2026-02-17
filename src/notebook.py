class Notebook:
    def __init__(self):
        self.notas = []

    def add_note(self, title: str, text: str, importance: str) -> int:
        new_code = len(self.notas) + 1
        note = Note(new_code, title, text, importance)
        self.notas.append(note)
        return new_code
