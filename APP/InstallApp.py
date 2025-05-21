import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import urllib.request
import zipfile
import shutil

# Конфигурация (можно изменить)
VALID_LICENSE_KEY = "12345-ABCDE-67890"  # Пример ключа
GITHUB_REPO_URL = "https://github.com/example/example-repo"  # Замените на нужный репозиторий
DOWNLOAD_METHOD = "git"  # "git" или "zip"

def check_license():
    entered_key = license_entry.get().strip()
    
    if entered_key == VALID_LICENSE_KEY:
        messagebox.showinfo("Успех", "Лицензия подтверждена! Скачиваю проект...")
        download_project()
    else:
        messagebox.showerror("Ошибка", "Неверный ключ лицензии!")

def download_project():
    try:
        if DOWNLOAD_METHOD == "git":
            # Клонируем репозиторий через git (должен быть установлен git)
            repo_name = GITHUB_REPO_URL.split("/")[-1]
            if not os.path.exists(repo_name):
                subprocess.run(["git", "clone", GITHUB_REPO_URL], check=True)
                messagebox.showinfo("Готово", f"Проект скачан в папку: {repo_name}")
            else:
                messagebox.showwarning("Внимание", "Папка с проектом уже существует!")
        
        elif DOWNLOAD_METHOD == "zip":
            # Скачиваем ZIP-архив и распаковываем
            repo_name = GITHUB_REPO_URL.split("/")[-1]
            zip_url = f"{GITHUB_REPO_URL}/archive/refs/heads/main.zip"
            zip_path = "project.zip"
            
            # Скачивание
            urllib.request.urlretrieve(zip_url, zip_path)
            
            # Распаковка
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall()
            
            # Удаляем ZIP (опционально)
            os.remove(zip_path)
            
            messagebox.showinfo("Готово", f"Проект скачан и распакован в: {repo_name}-main")
        
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось скачать проект: {e}")

# Создаем GUI
root = tk.Tk()
root.title("Лицензионный менеджер")
root.geometry("400x200")

tk.Label(root, text="Введите ключ лицензии:", font=("Arial", 12)).pack(pady=10)
license_entry = tk.Entry(root, width=40, font=("Arial", 10))
license_entry.pack(pady=5)

tk.Button(root, text="Проверить и скачать", command=check_license, bg="green", fg="white").pack(pady=20)

root.mainloop()
