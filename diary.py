import json
from datetime import datetime

DIARY_FILE = "diary.json"

def load_diary():
    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_diary(entries):
    with open(DIARY_FILE, "w", encoding="utf-8") as file:
        json.dump(entries, file, ensure_ascii=False, indent=4)

def add_entry():
    title = input("Введите заголовок: ")
    content = input("Введите текст записи: ")
    
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "title": title,
        "content": content
    }
    
    entries = load_diary()
    entries.append(entry)
    save_diary(entries)
    
    print("\nЗапись добавлена!")

def view_entries():
    entries = load_diary()
    
    if not entries:
        print("\nЗаписей пока нет.")
        return
    
    print("\nВаши записи:")
    for i, entry in enumerate(entries, 1):
        print(f"\n{i}. [{entry['date']}] {entry['title']}")
        print(f"   {entry['content']}")

def main():
    while True:
        print("\n=== Дневник ===")
        print("1. Добавить запись")
        print("2. Просмотреть записи")
        print("3. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()