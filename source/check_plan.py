import tkinter as tk
import tkcalendar as tkc
from datetime import datetime, timedelta
from hotel_plan import stayplan_page
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Check_page(tk.Frame):
    def __init__(self, master, plan):
        super().__init__(master)
        self.master = master
        self.hotelplan = plan
        self.pack(fill='both', expand=True)
        master.geometry('900x600')
        master.title('検索')
        start_date = datetime(2025, 1, 1)
        end_date = datetime(2030, 12, 31)
        self.availability = {}
        
        current_date = start_date
        while current_date <= end_date:
            self.availability[current_date.strftime('%Y-%m-%d')] = '○'
            current_date += timedelta(days=1)
        
        self.create_widgets()
        
    def create_widgets(self):
        redimg = Image.open("red.png") # リサイズしたいアイコンのファイル名
        red_width = 10  # 希望の幅 (ピクセル)
        red_height = 10 # 希望の高さ (ピクセル)
        resized_red = redimg.resize((red_width, red_height))
        self.red_icon_resized = ImageTk.PhotoImage(resized_red)
        
        blueimg = Image.open("blue.png") # リサイズしたいアイコンのファイル名
        blue_width = 10  # 希望の幅 (ピクセル)
        blue_height = 10 # 希望の高さ (ピクセル)
        resized_blue = blueimg.resize((blue_width, blue_height))
        self.blue_icon_resized = ImageTk.PhotoImage(resized_blue)
        
        doorimg = Image.open("door.png") # リサイズしたいアイコンのファイル名
        door_width = 30  # 希望の幅 (ピクセル)
        door_height = 30 # 希望の高さ (ピクセル)
        resized_door = doorimg.resize((door_width, door_height))
        self.door_icon_resized = ImageTk.PhotoImage(resized_door)
        
        calimg = Image.open("cal.png") # リサイズしたいアイコンのファイル名
        cal_width = 30  # 希望の幅 (ピクセル)
        cal_height = 30 # 希望の高さ (ピクセル)
        resized_cal = calimg.resize((cal_width, cal_height))
        self.cal_icon_resized = ImageTk.PhotoImage(resized_cal)
        
        hitoimg = Image.open("hito2.png") # リサイズしたいアイコンのファイル名
        hito_width = 30  # 希望の幅 (ピクセル)
        hito_height = 30 # 希望の高さ (ピクセル)
        resized_hito = hitoimg.resize((hito_width, hito_height))
        self.hito_icon_resized = ImageTk.PhotoImage(resized_hito)
        
        self.plan = tk.Label(self, text=f'選択プラン：{self.hotelplan}', font=("", 10))
        self.plan.place(x=50, y=50)
        
        self.hito_label = tk.Label(self, image=self.hito_icon_resized)
        self.hito_label.place(x=65, y=125)
        self.adult = tk.Label(self, text='大人', font=("", 12))
        self.adult.place(x=100, y=110)
        self.adEntry = tk.Entry(self, font=("", 16))
        self.adEntry.place(x=100, y=130, height=30, width=100)
        self.adult2 = tk.Label(self, text='名')
        self.adult2.place(x=210, y=145)
        
        self.child = tk.Label(self, text='子供', font=("", 12))
        self.child.place(x=230, y=110)
        self.chEntry = tk.Entry(self, font=("", 16))
        self.chEntry.place(x=230, y=130, height=30, width=100)
        self.child2 = tk.Label(self, text='名')
        self.child2.place(x=330, y=145)
        
        self.cal_label = tk.Label(self, image=self.cal_icon_resized)
        self.cal_label.place(x=60, y=220)
        self.day = tk.Label(self, text='日付', font=("", 12))
        self.day.place(x=100, y=200)
        self.daEntry = tk.Entry(self, font=("", 16))
        self.daEntry.place(x=100, y=220, height=35, width=120)
        
        self.door_label = tk.Label(self, image=self.door_icon_resized)
        self.door_label.place(x=60, y=320)
        self.roch = tk.Label(self, text='部屋選択', font=("", 12))
        self.roch.place(x=100, y=300)
        list = ["岩手山展望露天風呂付き和室", "檜の内風呂付き本館和洋室", "岩手山側和室10畳間", "本館 和室7.5畳間", "西館和室28畳間", "西館和室10畳間", "西館洋室（ツイン）禁煙", "西館和洋室（バリアフリー／ツイン+和室7.5畳間"]
        self.combo = ttk.Combobox(self, values=list, state="readonly")
        self.combo.current(0)
        self.combo.place(x=100, y=320, height=35, width=260)
        
        self.cal = tkc.Calendar(self, selectmode = 'day', year = 2025, font = "Arial 15", date_pattern='yyyy-mm-dd')
        self.cal.bind("<<CalendarSelected>>", self.update_date_entry)
        self.cal.tag_config('availability', background='light blue', foreground='black')
        self.cal.place(x=480, y=120)
        
        self.hito_label = tk.Label(self, image=self.blue_icon_resized)
        self.hito_label.place(x=765, y=382)
        self.label3 = tk.Label(self, text='青は空室', font=("", 12))
        self.label3.place(x=785, y=380)
        self.hito_label = tk.Label(self, image=self.red_icon_resized)
        self.hito_label.place(x=765, y=402)
        self.label4 = tk.Label(self, text='赤は満室', font=("", 12))
        self.label4.place(x=785, y=400)
        
        self.back = tk.Button(self, text='戻る', command=self.back_crick, font=("", 12))
        self.back.place(x=60, y=490, width=100, height=35)
        self.enter = tk.Button(self, text='料金計算へ', command=self.enter_crick, fg="white", bg="#576FC5", font=("", 12))
        self.enter.place(x=477, y=490, width=120, height=35)
        
        self.mark_availability()
        
    def mark_availability(self):
        for date_str, status in self.availability.items():
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            self.cal.calevent_create(date, status, 'availability')
            
    def update_date_entry(self, event):
        selected_date = self.cal.get_date()
        self.daEntry.delete(0, tk.END)
        self.daEntry.insert(0, selected_date)
        
    def back_crick(self):
        from main import Application
        self.destroy()
        Application(self.master)
        
    def enter_crick(self):
        from amount_banquet2 import Amount_page
        room = self.combo.get()
        adult = self.adEntry.get()
        child = self.chEntry.get()
        day = self.daEntry.get()
        if not adult:
            messagebox.showerror("エラー", "大人の人数を選択してください。")
        elif not day:
            messagebox.showerror("エラー", "日付を選択してください。")
        else:
            self.destroy()
            Amount_page(self.master, self.hotelplan, room, adult, child, day)
        
if __name__ == '__main__':
    root = tk.Tk()
    # 単独実行時のテスト用として、何らかのプラン名を渡す
    app = Check_page(master=root, plan="29【8/13～8/15】2025お盆期間限定♪お子様歓迎！スイカ割り・森のスタンプラリー・ミニ縁日や夜のイベントなどお楽しみ盛りだくさん")
    app.mainloop()
    