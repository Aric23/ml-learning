import json 
import os
from datatime import datetime

NOTES_FILE = "notes_json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError:
         print("Ошибка: файл повреждён, создаём новый")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")
        return []

def save_notes(notes):
    """Сохраняет заметки в файл"""
    try:
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
        return False

def add_note(notes, title, content):
    """Добавляет новую заметку"""
    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(note)
    return save_notes(notes)

def list_notes(notes):
    """Выводит список всех заметок"""
    if not notes:
        print("\n📭 Нет заметок")
        return
    
    print("\n📋 Мои заметки:")
    for note in notes:
        print(f"  [{note['id']}] {note['title']} ({note['created']})")

def view_note(notes, note_id):
    """Показывает конкретную заметку"""
    for note in notes:
        if note["id"] == note_id:
            print(f"\n📄 {note['title']}")
            print(f"📅 {note['created']}")
            print("-" * 40)
            print(note['content'])
            return
    print(f"❌ Заметка с id {note_id} не найдена")

def delete_note(notes, note_id):
    """Удаляет заметку"""
    for i, note in enumerate(notes):
        if note["id"] == note_id:
            del notes[i]
            # Перенумеровываем id
            for j, n in enumerate(notes, 1):
                n["id"] = j
            return save_notes(notes)
    print(f"❌ Заметка с id {note_id} не найдена")
    return False

# Основная программа
print("📝 Журнал заметок")
print("Команды: add, list, view, delete, exit")

notes = load_notes()

while True:
    command = input("\n> ").strip().lower()
    
    if command == "exit":
        print("До свидания!")
        break
    
    elif command == "add":
        title = input("Название: ")
        content = input("Содержание: ")
        if add_note(notes, title, content):
            print("✅ Заметка добавлена")
        else:
            print("❌ Ошибка при сохранении")
    
    elif command == "list":
        list_notes(notes)
    
    elif command == "view":
        try:
            note_id = int(input("ID заметки: "))
            view_note(notes, note_id)
        except ValueError:
            print("❌ Введите число")
    
    elif command == "delete":
        try:
            note_id = int(input("ID заметки для удаления: "))
            if delete_note(notes, note_id):
                print("✅ Заметка удалена")
        except ValueError:
            print("❌ Введите число")
    
    else:
        print("❌ Неизвестная команда")
