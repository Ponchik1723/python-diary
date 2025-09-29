import json
from datetime import datetime

class Note:
    def __init__(self, title: str, content: str):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.title = title
        self.content = content
    
    def to_dict(self) -> dict:
        return {
            "date": self.date,
            "title": self.title,
            "content": self.content
        }
    
    def __str__(self) -> str:
        return f"[{self.date}] {self.title}\n{self.content}"

class Diary:
    def __init__(self, filename: str = "diary.json"):
        self.filename = filename
        self.entries = self.load_entries()
    
    def load_entries(self) -> list:
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Note(title=item["title"], content=item["content"]) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_entries(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([entry.to_dict() for entry in self.entries], file, ensure_ascii=False, indent=4)
    
    def add_entry(self, title: str, content: str):
        new_note = Note(title, content)
        self.entries.append(new_note)
        self.save_entries()
        print("\nЗапись добавлена!")
    
    def view_entries(self):
        if not self.entries:
            print("\nЗаписей пока нет.")
            return
        
        print("\nВаши записи:")
        for i, entry in enumerate(self.entries, 1):
            print(f"\n{i}. {entry}")

def main():
    my_diary = Diary()
    
    while True:
        print("\n=== Дневник ===")
        print("1. Добавить запись")
        print("2. Просмотреть записи")
        print("3. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            title = input("Введите заголовок: ")
            content = input("Введите текст записи: ")
            my_diary.add_entry(title, content)
        
        elif choice == "2":
            my_diary.view_entries()
        
        elif choice == "3":
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()