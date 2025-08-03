from datetime import datetime


class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(self, code: int, title: str, text: str, importance: str):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags = []

    def add_tag(self, tag: str):
        self.tags.append(tag)

    def __str__(self):
        return f"[{self.creation_date}] {self.title}: {self.text} ({self.importance})"
