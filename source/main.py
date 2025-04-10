import tkinter as tk
from PIL import Image, ImageTk  # Pillowライブラリが必要です
from hotel_plan import stayplan_page
class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=900, height=600)
        self.pack()
        master.geometry('900x600')
        master.title('ホーム画面')
        self.create_widgets()
    def create_widgets(self):
        # タイトルラベル
        self.label = tk.Label(self, text="予約選択", font=("Arial", 20))
        self.label.place(x=80, y=90)
        # 宿泊ボタン
        syukuimg = Image.open("img/hotel.png")
        resized_syuku = syukuimg.resize((100, 100))
        self.hotel_icon_resized = ImageTk.PhotoImage(resized_syuku)
        self.btn_accommodation = tk.Button(self, text="宿泊", font=("Arial", 18), image=self.hotel_icon_resized, compound="top",
                                           bg="lightblue", fg="black",
                                           width=200, height=190, command=self.select_accommodation)
        self.btn_accommodation.place(x=200, y=200)
        # 宴会ボタン（画像付き）
        blueimg = Image.open("img/enkai.png")
        resized_blue = blueimg.resize((100, 100))
        self.blue_icon_resized = ImageTk.PhotoImage(resized_blue)
        self.btn_banquet = tk.Button(self, text="宴会", image=self.blue_icon_resized,
                                     compound="top", font=("Arial", 18),
                                     bg="lightblue", fg="black",
                                     width=200, height=190, command=self.select_banquet)
        self.btn_banquet.place(x=500, y=200)
    def select_accommodation(self):        
        from hotel_plan import stayplan_page
        self.destroy()
        stayplan_page(root)
        
    def select_banquet(self):
        pass
        from banquet_plan import Application
        self.destroy()
        Application(root)
        
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()







