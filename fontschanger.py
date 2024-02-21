import tkinter as tk
from tkinter import ttk
import threading

def convert_to_fancy_text(text, language='all'):
    english_fancy_letters = {
        'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ꜰ', 'g': 'ɢ', 'h': 'ʜ',
        'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ',
        'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ', 'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x',
        'y': 'ʏ', 'z': 'ᴢ',
        ' ': ' '
    }
    
    russian_fancy_letters = {
        'а': 'ᴀ', 'б': 'б', 'в': 'в', 'г': 'ᴦ', 'д': 'д', 'е': 'ᴇ', 'ё': 'ᴇ', 'ж': 'ж',
        'з': 'з', 'и': 'ᴎ', 'й': 'й', 'к': 'к', 'л': 'ᴫ', 'м': 'м', 'н': 'н', 'о': 'ᴏ',
        'п': 'п', 'р': 'ᴩ', 'с': 'ᴄ', 'т': 'т', 'у': 'у', 'ф': 'ф', 'х': 'ⅹ', 'ц': 'ц',
        'ч': 'ч', 'ш': 'ш', 'щ': 'щ', 'ъ': 'ъ', 'ы': 'ы', 'ь': 'ь', 'э': 'э', 'ю': 'ю',
        'я': 'я',
        'А': 'ᴀ', 'Б': 'б', 'В': 'в', 'Г': 'ᴦ', 'Д': 'д', 'Е': 'ᴇ', 'Ё': 'ᴇ', 'Ж': 'ж',
        'З': 'з', 'И': 'ᴎ', 'Й': 'й', 'К': 'к', 'Л': 'ᴫ', 'М': 'м', 'Н': 'н', 'О': 'ᴏ',
        'П': 'п', 'Р': 'ᴩ', 'С': 'ᴄ', 'Т': 'т', 'У': 'у', 'Ф': 'ф', 'Х': 'ⅹ', 'Ц': 'ц',
        'Ч': 'ч', 'Ш': 'ш', 'Щ': 'ш', 'Ъ': 'ъ', 'Ы': 'ы', 'Ь': 'ь', 'Э': 'э', 'Ю': 'ю',
        'Я': 'я',
        ' ': ' '
    }

    fancy_text = ''
    if language == 'english':
        for char in text:
            if char in english_fancy_letters:
                fancy_text += english_fancy_letters[char]
            else:
                fancy_text += char
    elif language == 'russian':
        for char in text:
            if char in russian_fancy_letters:
                fancy_text += russian_fancy_letters[char]
            else:
                fancy_text += char
    else:  # 'all'
        for char in text:
            if char in english_fancy_letters:
                fancy_text += english_fancy_letters[char]
            elif char in russian_fancy_letters:
                fancy_text += russian_fancy_letters[char]
            else:
                fancy_text += char
    return fancy_text

def toggle_conversion():
    global converting
    converting = not converting
    if converting:
        convert_button.config(text="Выключить конвертацию", style="Red.TButton")
    else:
        convert_button.config(text="Включить конвертацию", style="Green.TButton")

def monitor_clipboard():
    global selected_language
    current_text = None
    while True:
        root.update()
        try:
            clipboard_text = root.clipboard_get()
        except tk.TclError:
            clipboard_text = None
        
        if clipboard_text and clipboard_text != current_text:
            current_text = clipboard_text
            if converting:
                fancy_text = convert_to_fancy_text(current_text, language=selected_language)
                root.clipboard_clear()
                root.clipboard_append(fancy_text)

converting = True
selected_language = 'all'

root = tk.Tk()
root.title("FontsChanger")
root.geometry("400x300")  # Устанавливаем начальный размер окна
root.minsize(400, 300)  # Устанавливаем минимальный размер окна
root.maxsize(600, 400)  # Устанавливаем максимальный размер окна

# Применяем темную тему оформления
style = ttk.Style()
style.theme_use("clam")  # Вы можете выбрать любую доступную тему, поддерживаемую tkinter

# Устанавливаем цвета для темной темы
style.configure("TLabel", background="black", foreground="white")
style.configure("Red.TButton", background="red", foreground="white", font=("Helvetica", 12))
style.configure("Green.TButton", background="green", foreground="white", font=("Helvetica", 12))

title_label = tk.Label(root, text="FontsChanger", font=("Helvetica", 24))
title_label.pack(pady=10)

convert_button = ttk.Button(root, text="Выключить конвертацию", command=toggle_conversion, style="Red.TButton")
convert_button.pack(pady=5)

info_label = tk.Label(root, text="Скопируйте и вставьте текст", font=("Helvetica", 16))
info_label.pack(pady=5)

credits_label = tk.Label(root, text="ʙʏ ᴡᴀᴍᴀʟᴅɪ ᴀɴᴅ ᴀᴋɪᴛᴀ__", font=("Helvetica", 10))
credits_label.pack(pady=10)

# Добавляем меню настроек
def open_settings():
    global selected_language
    settings_window = tk.Toplevel(root)
    settings_window.title("Настройки")
    settings_window.geometry("200x150")
    settings_window.transient(root)  # Делаем окно настроек модальным

    # Добавляем выбор языка
    language_frame = ttk.LabelFrame(settings_window, text="Выбор языка для конвертации.")
    language_frame.pack(pady=10)

    def set_language(lang):
        global selected_language
        selected_language = lang

    english_radio = ttk.Radiobutton(language_frame, text="Английский", value="english", command=lambda: set_language('english'))
    english_radio.pack(anchor="w")
    russian_radio = ttk.Radiobutton(language_frame, text="Русский", value="russian", command=lambda: set_language('russian'))
    russian_radio.pack(anchor="w")
    all_radio = ttk.Radiobutton(language_frame, text="Все", value="all", command=lambda: set_language('all'))
    all_radio.pack(anchor="w")

menu_bar = tk.Menu(root)
settings_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_command(label="Открыть настройки", command=open_settings)
menu_bar.add_cascade(label="Настройки", menu=settings_menu)

root.config(menu=menu_bar)

monitor_thread = threading.Thread(target=monitor_clipboard)
monitor_thread.daemon = True
monitor_thread.start()

root.mainloop()
