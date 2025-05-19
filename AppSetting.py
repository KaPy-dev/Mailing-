import tkinter as tk
from tkinter import messagebox

class BotConfigApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bot Configuration")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

       
        tk.Label(root, text="Введите токен бота:", font=("Arial", 12)).pack(pady=10)
        self.token_entry = tk.Entry(root, width=50, font=("Arial", 10))
        self.token_entry.pack(pady=5)

       
        tk.Label(root, text="Введите ID владельца:", font=("Arial", 12)).pack(pady=10)
        self.id_entry = tk.Entry(root, width=50, font=("Arial", 10))
        self.id_entry.pack(pady=5)

       
        tk.Button(root, text="Сохранить", command=self.save_config, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=20)

    def save_config(self):
        token = str("".join(self.token_entry.get().strip()))
        print(token)
        owner_id = self.id_entry.get().strip()

        if not token or not owner_id:
            messagebox.showerror("Ошибка", "Заполните все поля!")
            return

        
        if not owner_id.isdigit():
            messagebox.showerror("Ошибка", "ID владельца должен содержать только цифры!")
            return

        try:
            import sqlite3, os, pathlib
            global DIR
            DIR = pathlib.Path(__file__).parent.resolve()
            os.chdir(DIR)
            os.chdir("..")
            os.chdir("..")
            print(DIR)
            # messagebox.showinfo(f"?",(str(DIR)))

            with sqlite3.connect('base.db') as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM System")
                if len(cur.fetchall()) >0 :
                    cur.execute(fr"UPDATE System SET OwnerId = ?, TokenBots = ?",(owner_id,token))
                else:
                    cur.execute(fr"INSERT INTO System(OwnerId, TokenBots) VALUES({owner_id},{ str(token)})")
            messagebox.showinfo("Успех", "Конфигурация сохранена")
            self.root.quit()
        except Exception as e:
            print(e)
            messagebox.showerror("Ошибка", f"Не удалось сохранить: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BotConfigApp(root)
    root.mainloop()
