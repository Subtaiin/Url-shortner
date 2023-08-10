
import tkinter as tk
from tkinter import font
import pyshorteners
import pyperclip

def on_enter(e):
    shorten_button['background'] = '#4CAF50'
    copy_button['background'] = '#4CAF50'

def on_leave(e):
    shorten_button['background'] = '#45a049'
    copy_button['background'] = '#45a049'

def shorten_url():
    url = url_input.get()
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    shortened_url_label.config(text=shortened_url)
    copy_button.config(state=tk.NORMAL)

def copy_url():
    url_to_copy = shortened_url_label.cget("text")
    pyperclip.copy(url_to_copy)

root = tk.Tk()
root.geometry('400x200')
root.title('URL Shortener')
root.configure(bg='#f4f4f4')

app_font = font.Font(size=12, weight='bold')
url_input = tk.Entry(root, width=50, font=app_font)
url_input.pack(pady=10)

shorten_button = tk.Button(root, text='Shorten URL', command=shorten_url, bg='#45a049', fg='white', font=app_font)
shorten_button.pack(pady=10)
shorten_button.bind("<Enter>", on_enter)
shorten_button.bind("<Leave>", on_leave)

shortened_url_label = tk.Label(root, text='', bg='#f4f4f4', font=app_font)
shortened_url_label.pack(pady=10)

copy_button = tk.Button(root, text='Copy URL', state=tk.DISABLED, command=copy_url, bg='#45a049', fg='white', font=app_font)
copy_button.pack(pady=10)
copy_button.bind("<Enter>", on_enter)
copy_button.bind("<Leave>", on_leave)

root.mainloop()
