import tkinter as tk
from tkinter import ttk
import threading

def convert_to_fancy_text(text, language='all', style='style1'):
    english_fancy_letters = {
        'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ꜰ', 'g': 'ɢ', 'h': 'ʜ',
        'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ',
        'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ', 'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x',
        'y': 'ʏ', 'z': 'ᴢ',
        ' ': ' '
    }
    
    russian_fancy_styles = {
        'style1': {
            'а': 'ᗩ', 'б': 'Б', 'в': 'ᗷ', 'г': 'Г', 'д': 'Д', 'е': 'ᕮ', 'ё': 'Ё', 'ж': 'Ж',
            'з': '3', 'и': 'И', 'й': 'Й', 'к': '𐌊', 'л': 'Л', 'м': 'Ⲙ', 'н': 'ᕼ', 'о': '〇',
            'п': 'П', 'р': 'ᑭ', 'с': 'ᙅ', 'т': 'Ƭ', 'у': 'Ⴤ', 'ф': 'Ф', 'х': 'Ⲭ', 'ц': 'Ц',
            'ч': 'Ч', 'ш': 'ᙡ', 'щ': 'Щ', 'ъ': 'Ъ', 'ы': 'Ы', 'ь': 'Ь', 'э': 'Э', 'ю': 'Ю',
            'я': 'Я', 'А': 'ᗩ', 'Б': 'Б', 'В': 'ᗷ', 'Г': 'Г', 'Д': 'Д', 'Е': 'ᕮ', 'Ё': 'Ё',
            'Ж': 'Ж', 'З': '3', 'И': 'И', 'Й': 'Й', 'К': '𐌊', 'Л': 'Л', 'М': 'Ⲙ', 'Н': 'ᕼ',
            'О': '〇', 'П': 'П', 'Р': 'ᑭ', 'С': 'ᙅ', 'Т': 'Ƭ', 'У': 'Ⴤ', 'Ф': 'Ф', 'Х': 'Ⲭ',
            'Ц': 'Ц', 'Ч': 'Ч', 'Ш': 'ᙡ', 'Щ': 'Щ', 'Ъ': 'Ъ', 'Ы': 'Ы', 'Ь': 'Ь', 'Э': 'Э',
            'Ю': 'Ю', 'Я': 'Я', ' ': ' '
        },
        'style2': {
            'а': '𝓐', 'б': 'Б', 'в': 'ẞ', 'г': 'Г', 'д': 'Д', 'е': 'Ɛ', 'ё': 'Ё', 'ж': 'Ж',
            'з': '3', 'и': 'И', 'й': 'Й', 'к': 'Ⲕ', 'л': 'Л', 'м': 'ᙏ', 'н': 'Ԩ', 'о': 'O',
            'п': 'П', 'р': 'ᑭ', 'с': 'C', 'т': '㆜', 'у': 'У', 'ф': 'Ф', 'х': 'ⵋ', 'ц': 'Ц',
            'ч': 'Ч', 'ш': 'ᗯ', 'щ': 'Щ', 'ъ': 'Ъ', 'ы': 'Ы', 'ь': 'Ƅ', 'э': 'Э', 'ю': 'Ю',
            'я': 'Я', 'А': '𝓐', 'Б': 'Б', 'В': 'ẞ', 'Г': 'Г', 'Д': 'Д', 'Е': 'Ɛ', 'Ё': 'Ё',
            'Ж': 'Ж', 'З': '3', 'И': 'И', 'Й': 'Й', 'К': 'Ⲕ', 'Л': 'Л', 'М': 'ᙏ', 'Н': 'Ԩ',
            'О': 'O', 'П': 'П', 'Р': 'ᑭ', 'С': 'C', 'Т': '㆜', 'У': 'У', 'Ф': 'Ф', 'Х': 'ⵋ',
            'Ц': 'Ц', 'Ч': 'Ч', 'Ш': 'ᗯ', 'Щ': 'Щ', 'Ъ': 'Ъ', 'Ы': 'Ы', 'Ь': 'Ƅ', 'Э': 'Э',
            'Ю': 'Ю', 'Я': 'Я', ' ': ' '
        },
        'style3': {
            'а': '𝒜', 'б': 'Б', 'в': 'ℬ', 'г': 'Г', 'д': 'Д', 'е': 'ℰ', 'ё': 'Ё', 'ж': 'Ж',
            'з': '3', 'и': 'И', 'й': 'Й', 'к': '𝒦', 'л': 'Л', 'м': 'ℳ', 'н': 'ℋ', 'о': '𝒪',
            'п': 'П', 'р': '𝒫', 'с': '𝒞', 'т': '𝒯', 'у': '𝒴', 'ф': 'Ф', 'х': '𝒳', 'ц': 'Ц',
            'ч': 'Ч', 'ш': '𝒲', 'щ': 'Щ', 'ъ': 'Ъ', 'ы': 'Ы', 'ь': 'Ь', 'э': 'Э', 'ю': 'Ю',
            'я': 'Я', 'А': '𝒜', 'Б': 'Б', 'В': 'ℬ', 'Г': 'Г', 'Д': 'Д', 'Е': 'ℰ', 'Ё': 'Ё',
            'Ж': 'Ж', 'З': '3', 'И': 'И', 'Й': 'Й', 'К': '𝒦', 'Л': 'Л', 'М': 'ℳ', 'Н': 'ℋ',
            'О': '𝒪', 'П': 'П', 'Р': '𝒫', 'С': '𝒞', 'Т': '𝒯', 'У': '𝒴', 'Ф': 'Ф', 'Х': '𝒳',
            'Ц': 'Ц', 'Ч': 'Ч', 'Ш': '𝒲', 'Щ': 'Щ', 'Ъ': 'Ъ', 'Ы': 'Ы', 'Ь': 'Ь', 'Э': 'Э',
            'Ю': 'Ю', 'Я': 'Я', ' ': ' '
        },
        'style4': {
            'а': '𝐀', 'б': 'Б', 'в': '𝐁', 'г': 'Г', 'д': 'Д', 'е': '𝐄', 'ё': 'Ё', 'ж': 'Ж',
            'з': '3', 'и': 'И', 'й': 'Й', 'к': '𝐊', 'л': 'Л', 'м': '𝐌', 'н': '𝐇', 'о': '𝐎',
            'п': 'П', 'р': '𝐏', 'с': '𝐂', 'т': '𝐓', 'у': '𝐘', 'ф': 'Ф', 'х': '𝐗', 'ц': 'Ц',
            'ч': 'Ч', 'ш': '𝐖', 'щ': 'Щ', 'ъ': 'Ъ', 'ы': 'Ы', 'ь': 'Ь', 'э': 'Э', 'ю': 'Ю',
            'я': 'Я', 'А': '𝐀', 'Б': 'Б', 'В': '𝐁', 'Г': 'Г', 'Д': 'Д', 'Е': '𝐄', 'Ё': 'Ё',
            'Ж': 'Ж', 'З': '3', 'И': 'И', 'Й': 'Й', 'К': '𝐊', 'Л': 'Л', 'М': '𝐌', 'Н': '𝐇',
            'О': '𝐎', 'П': 'П', 'Р': '𝐏', 'С': '𝐂', 'Т': '𝐓', 'У': '𝐘', 'Ф': 'Ф', 'Х': '𝐗',
            'Ц': 'Ц', 'Ч': 'Ч', 'Ш': '𝐖', 'Щ': 'Щ', 'Ъ': 'Ъ', 'Ы': 'Ы', 'Ь': 'Ь', 'Э': 'Э',
            'Ю': 'Ю', 'Я': 'Я', ' ': ' '
        },
        'style5': {
            'а': '𝔸', 'б': 'Б', 'в': '𝔹', 'г': 'Г', 'д': 'Д', 'е': '𝔼', 'ё': 'Ё', 'ж': 'Ж',
            'з': '3', 'и': 'И', 'й': 'Й', 'к': '𝕂', 'л': 'Л', 'м': '𝕄', 'н': 'ℍ', 'о': '𝕆',
            'п': 'П', 'р': 'ℙ', 'с': 'ℂ', 'т': '𝕋', 'у': '𝕐', 'ф': 'Ф', 'х': '𝕏', 'ц': 'Ц',
            'ч': 'Ч', 'ш': '𝕎', 'щ': 'Щ', 'ъ': 'Ъ', 'ы': 'Ы', 'ь': 'Ь', 'э': 'Э', 'ю': 'Ю',
            'я': 'Я', 'А': '𝔸', 'Б': 'Б', 'В': '𝔹', 'Г': 'Г', 'Д': 'Д', 'Е': '𝔼', 'Ё': 'Ё',
            'Ж': 'Ж', 'З': '3', 'И': 'И', 'Й': 'Й', 'К': '𝕂', 'Л': 'Л', 'М': '𝕄', 'Н': 'ℍ',
            'О': '𝕆', 'П': 'П', 'Р': 'ℙ', 'С': 'ℂ', 'Т': '𝕋', 'У': '𝕐', 'Ф': 'Ф', 'Х': '𝕏',
            'Ц': 'Ц', 'Ч': 'Ч', 'Ш': '𝕎', 'Щ': 'Щ', 'Ъ': 'Ъ', 'Ы': 'Ы', 'Ь': 'Ь', 'Э': 'Э',
            'Ю': 'Ю', 'Я': 'Я', ' ': ' '
        }
    }

    fancy_text = ''
    if language == 'english':
        for char in text:
            if char in english_fancy_letters:
                fancy_text += english_fancy_letters[char]
            else:
                fancy_text += char
    elif language == 'russian':
        fancy_letters = russian_fancy_styles[style]
        for char in text:
            if char in fancy_letters:
                fancy_text += fancy_letters[char]
            else:
                fancy_text += char
    else:  # 'all'
        for char in text:
            if char in english_fancy_letters:
                fancy_text += english_fancy_letters[char]
            else:
                fancy_letters = russian_fancy_styles[style]
                if char in fancy_letters:
                    fancy_text += fancy_letters[char]
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
    global selected_language, selected_style
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
                fancy_text = convert_to_fancy_text(current_text, language=selected_language, style=selected_style)
                root.clipboard_clear()
                root.clipboard_append(fancy_text)

converting = True
selected_language = 'all'
selected_style = 'style1'

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
    global selected_language, selected_style
    settings_window = tk.Toplevel(root)
    settings_window.title("Настройки")
    settings_window.geometry("300x300")
    settings_window.transient(root)  # Делаем окно настроек модальным

    # Добавляем выбор языка
    language_frame = ttk.LabelFrame(settings_window, text="Выбор языка для конвертации.")
    language_frame.pack(pady=10, fill="x")

    def set_language(lang):
        global selected_language
        selected_language = lang

    english_radio = ttk.Radiobutton(language_frame, text="Английский", value="english", command=lambda: set_language('english'))
    english_radio.pack(anchor="w")
    russian_radio = ttk.Radiobutton(language_frame, text="Русский", value="russian", command=lambda: set_language('russian'))
    russian_radio.pack(anchor="w")
    all_radio = ttk.Radiobutton(language_frame, text="Все", value="all", command=lambda: set_language('all'))
    all_radio.pack(anchor="w")

    if selected_language == 'english':
        english_radio.invoke()
    elif selected_language == 'russian':
        russian_radio.invoke()
    else:
        all_radio.invoke()

    # Добавляем выбор стиля
    style_frame = ttk.LabelFrame(settings_window, text="Выбор стиля шрифта для русского.")
    style_frame.pack(pady=10, fill="x")

    def set_style(sty):
        global selected_style
        selected_style = sty

    style1_radio = ttk.Radiobutton(style_frame, text="Большой стиль", value="style1", command=lambda: set_style('style1'))
    style1_radio.pack(anchor="w")
    style2_radio = ttk.Radiobutton(style_frame, text="БOЛƄᗯOЙ стиль 2", value="style2", command=lambda: set_style('style2'))
    style2_radio.pack(anchor="w")
    style3_radio = ttk.Radiobutton(style_frame, text="непонятный какой то шрифт", value="style3", command=lambda: set_style('style3'))
    style3_radio.pack(anchor="w")
    style4_radio = ttk.Radiobutton(style_frame, text="Вроде норм", value="style4", command=lambda: set_style('style4'))
    style4_radio.pack(anchor="w")
    style5_radio = ttk.Radiobutton(style_frame, text="Полупрозрачный", value="style5", command=lambda: set_style('style5'))
    style5_radio.pack(anchor="w")

    if selected_style == 'style1':
        style1_radio.invoke()
    elif selected_style == 'style2':
        style2_radio.invoke()
    elif selected_style == 'style3':
        style3_radio.invoke()
    elif selected_style == 'style4':
        style4_radio.invoke()
    else:
        style5_radio.invoke()

menu_bar = tk.Menu(root)
settings_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_command(label="Открыть настройки", command=open_settings)
menu_bar.add_cascade(label="Настройки", menu=settings_menu)

root.config(menu=menu_bar)

monitor_thread = threading.Thread(target=monitor_clipboard)
monitor_thread.daemon = True
monitor_thread.start()

root.mainloop()
