import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
import os
from tkinter import Toplevel
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox
import json

class Amount_page(tk.Frame):
    def __init__(self, master, plan_name, room, adult, child, day):
        super().__init__(master, width=900, height=600)
        self.pack()
        self.plan_name = plan_name
        root = master
        self.room = room
        self.adult = adult
        self.child = child
        self.date = day
        master.geometry('900x600')
        master.title('Hello Tkinter')
        self.canvas = tk.Canvas(root)
        self.frame = tk.Frame(self.canvas)
        
        self.create_widgets()
        
    def create_widgets(self):        

        self.canvas = Canvas(self, height=500, width=850)
        self.canvas.place(x=25, y=90)
        self.inner_frame = tk.Frame(self.canvas)

        self.total = 0
        self.flg = False
        
        self.all_plan_amounts = [
            ["1【１泊２食のお子様3000円！】【2025年春休み】家族旅行応援！お子様歓迎♪早いもの勝ち！春休み限定プラン", 15600],
            ["2【イースター復活祭】×【女子旅】お部屋にはチョコレートたまご型お菓子などたくさん♪まったりしてねプラン(*´ω｀)", 13800],
            ["3【2025ゴールデンウィーク★プレミアムプラン】前沢牛の豪華会席GWバージョンで特別なひと時を♪夜のイベントも大満足！", 9000],
            ["4【スタンダード】【HP特価】八幡平産杜仲茶ポークの和食膳プラン", 12400],
            ["5【岩手県産牛】【HP特価】岩手県産牛と八幡平産杜仲茶ポークを味わう旬の味覚和食膳", 15400],
            ["6【前沢牛】【HP予約特典付き】≪ちょっと贅沢なご夕食≫ 前沢牛のせいろ蒸しとロースト前沢牛の握り付き和食膳プラン", 18400],
            ["7【前沢牛】【HP予約特典付き】≪ちょっと贅沢なご夕食≫ 前沢牛の網焼きとロースト前沢牛の握り付き和食膳プラン", 18400],
            ["8【前沢牛】【３つの特典付き】前沢牛＆伊勢海老＆あわび＆ズワイガニのおまねきプラン", 24000],
            ["9【前沢牛】前沢牛・伊勢海老・あわび・ズワイガニの豪華和食膳プラン", 21400],
            ["10【お誕生・記念日プラン】(*≧∇≦)/ ホールケーキ付♪サプライズでお祝いしましょ♪", 19600],
            ["11【早期割90日までご予約で15％割引】岩手県産牛と八幡平産杜仲茶ポークを味わう旬の味覚 和食膳", 13260],
            ["12【早期割90日までご予約で15％割引】前沢牛・伊勢海老・あわび・ズワイガニの和食膳", 18360],
            ["13【早期割60日までご予約で10％割引】岩手県産牛と八幡平産杜仲茶ポークを味わう旬の味覚 和食膳", 14040],
            ["14【早期割60日までご予約で10％割引】前沢牛・伊勢海老・あわび・ズワイガニの和食膳", 19440],
            ["15【赤ちゃんプラン】～お子様歓迎♪パパママも嬉しい12個の特典付き", 18800],
            ["16【赤ちゃんプラン・お食い初め】これからの成長と健康の願いを込めて～パパママも嬉しい12個の特典付き～", 18800],
            ["17【早期割90日までご予約で15％割引】温泉露天風呂付『黒倉の間』『源太の間』", 22950],
            ["18【早期割60日までご予約で10％割引】温泉露天風呂付『黒倉の間』『源太の間』", 24300],
            ["19【別館姫神】檜の温泉露天風呂付き『黒倉の間』『源太の間』", 27000],
            ["20【早期割90日までご予約で15％割引】温泉内風呂付き『見返の間』", 25500],
            ["21【早期割60日までご予約で10％割引】温泉内風呂付き『見返の間』", 27000],
            ["22【別館姫神】檜の温泉内風呂付き『見返の間』", 30000],
            ["23【早期割90日までご予約で15％割引】檜の温泉内風呂付き『茶臼の間』『七時雨の間』", 25500],
            ["24【早期割60日までご予約で10％割引】檜の温泉内風呂付き『茶臼の間』『七時雨の間』", 27000],
            ["25【別館姫神】檜の温泉内風呂付き『茶臼の間』『七時雨の間』", 30000],
            ["26【別館姫神】檜の温泉内風呂付き『貴賓室』", 35000],
            ["27【北投石の岩盤浴】豊かな八幡平の自然と岩盤浴でリフレッシュする旅を～八幡平産杜仲茶ポークの和食膳～", 13600],
            ["28【朝食付き】観光、ビジネス！一泊朝食プランでお気軽に八幡平を満喫！", 8500],
            ["29【8/13～8/15】2025お盆期間限定♪お子様歓迎！スイカ割り・森のスタンプラリー・ミニ縁日や夜のイベントなどお楽しみ盛りだくさん", 19000],
            ["30【八幡平の地ビール・ドラゴンアイビールで乾杯】八幡平の地産の恵みと八幡平のクラフトビールを楽しむプラン", 13000],
            ["宴会-豪華コース", 21600],
            ["宴会-雅(みやび)コース", 18600],
            ["宴会-錦(にしき)コース", 15600],
            ["宴会-椿(つばき)コース", 12600]
        ]
        
        
        # プラン名と予約フォームの文字
        self.plan_label = tk.Label(self, text=self.plan_name, font=("", 11))
        self.plan_label.place(x=30, y=50)
        # self.plan_label2 = tk.Label(self, text="プラン", font=("", 10))
        # self.plan_label2.place(x=840, y=70)
        self.fomu_label = tk.Label(self.canvas, text="予約フォーム", font=("", 15))
        self.fomu_label.place(x=110, y=50)
        # 宿泊日
        self.date_label = tk.Label(self.canvas, text="宿泊日", font=("", 13))
        self.date_label.place(x=50, y=90)
        self.date_label_two = tk.Label(self.canvas, text=self.date, font=("", 13))
        self.date_label_two.place(x=200, y=90)
        # 部屋種類
        self.room_label = tk.Label(self.canvas, text="部屋種類", font=("", 13))
        self.room_label.place(x=50, y=120)
        self.room_name = tk.Label(self.canvas, text=self.room, font=("", 13))
        self.room_name.place(x=200, y=120)
        # 泊数
        self.day_label = tk.Label(self.canvas, text="泊数", font=("", 13))
        self.day_label.place(x=50, y=150)
        self.day_select = ttk.Combobox(self.canvas, values=list(map(str, range(1, 11))), width=5, font=("", 13))
        self.day_select.set(1)
        self.day_select.place(x=200, y=150)
        self.day_label_two = tk.Label(self.canvas, text="泊", font=("", 12))
        self.day_label_two.place(x=270, y=150)
        # # 部屋数
        # self.room_label = tk.Label(self.canvas, text="部屋数", font=("", 13))
        # self.room_label.place(x=50, y=180)
        # self.room_select = ttk.Combobox(self.canvas, values=list(map(str, range(1, 7))), width=5, font=("", 13))
        # self.room_select.place(x=200, y=180)
        # self.room_label_two = tk.Label(self.canvas, text="部屋", font=("", 12))
        # self.room_label_two.place(x=270, y=180)
        # 人数
        self.big_people = tk.Label(self.canvas, text="大人", font=("", 13))
        self.big_people.place(x=50, y=180)
        self.big_people_entry = tk.Entry(self.canvas, font=("", 13), width=6)
        self.big_people_entry.insert(tk.END, self.adult)
        self.big_people_entry.place(x=200, y=180)
        self.big_people_label = tk.Label(self.canvas, text="名", font=("", 12))
        self.big_people_label.place(x=245, y=180)
        self.small_people = tk.Label(self.canvas, text="子供", font=("", 12))
        self.small_people.place(x=50, y=210)
        self.small_people_entry = tk.Entry(self.canvas, font=("", 13), width=6)
        self.small_people_entry.insert(tk.END, self.child)
        self.small_people_entry.place(x=200, y=210)
        self.small_people_label = tk.Label(self.canvas, text="名", font=("", 13))
        self.small_people_label.place(x=245, y=210)
        # 氏名・メール・電話番号
        self.name_label = tk.Label(self.canvas, text="氏名", font=("", 13))
        self.name_label.place(x=50, y=270)
        self.name_entry = tk.Entry(self.canvas, font=("", 13), width=20)
        self.name_entry.place(x=200, y=270)
        self.mail_label = tk.Label(self.canvas, text="メールアドレス", font=("", 13))
        self.mail_label.place(x=50, y=300)
        self.mail_entry = tk.Entry(self.canvas, font=("", 13), width=20)
        self.mail_entry.place(x=200, y=300)
        # self.tel_label = tk.Label(self.canvas, text="電話番号", font=("", 13))
        # self.tel_label.place(x=50, y=330)
        # self.tel_entry = tk.Entry(self.canvas, font=("", 13), width=20)
        # self.tel_entry.place(x=200, y=330)
        
        self.button = tk.Button(self, text="金額表示", command=self.amount_button, width=13, height=2, font=("", 12))
        self.button.place(x=285, y=460)
  
        self.new_post_button = tk.Button(self, text='オプション選択', font=("", 12), command=self.option_window, width=12, height=2)
        self.new_post_button.place(x=70, y=460)
        
        self.home_back = tk.Button(self, text="< ホームへ戻る", command=self.home_back_click, font=("", 10), width=11, height=1, relief="flat")
        self.home_back.place(x=20, y=20)
        
    def home_back_click(self):
        from main import Application
        self.destroy()
        Application(self.master)
    
        
        
    def option_window(self):
        self.option_newwindow = Toplevel(self)
        # ウィンドウサイズ設定
        self.option_newwindow.geometry("800x450")
        self.option_newwindow.title("オプション選択")

        x_margin = 20  # 左右の文字の間隔を縮める
        y_margin = 20
        label_font = ("", 12)
        title_font = ("", 12, "bold")
        # ---- 左カラム：追加料理 ----
        y = y_margin
        tk.Label(self.option_newwindow, text="追加料理", font=title_font).place(x=x_margin, y=y)
        y += 30
        self.addmeal_prices = [
            ("牛タン焼き（1250円）", 1250),
            ("ホルモン焼き（1100円）", 1100),
            ("岩手県産牛の串焼き（750円）", 750),
            ("前沢牛ミニステーキ（3600円）", 3600),
            ("ロースト前沢牛握り（1350円）", 1350),
            ("姫神サーモンの釜めし（900円）", 900),
            ("前沢牛のおせいろ蒸し（3600円）", 3600),
            ("ズワイガニのしゃぶしゃぶ（2100円）", 2100),
            ("岩名の塩焼き（720円）", 720)
        ]
        self.addmeal_combos = []
        for meal, price in self.addmeal_prices:
            tk.Label(self.option_newwindow, text=meal, font=label_font).place(x=x_margin, y=y)
            combo = ttk.Combobox(self.option_newwindow, values=[str(i) for i in range(10)], width=4, font=("", 11))
            combo.set("0")
            combo.place(x=x_margin + 260, y=y)  # 少し右にずらす
            self.addmeal_combos.append((combo, price))
            y += 25
            
        self.drink_label = tk.Label(self.option_newwindow, text="2時間飲み放題プラン (2000円)", font=(label_font)).place(x=20, y=300)
        self.drink_combo = ttk.Combobox(self.option_newwindow, values=[str(i) for i in range(10)], width=4, font=("", 11))
        self.drink_combo.set("0")
        self.drink_combo.place(x=x_margin + 260, y=300)
        
        # ---- 右カラム：ペット ----
        x_right = 400  # 右カラムの文字の間隔を狭める
        y = y_margin
        tk.Label(self.option_newwindow, text="ペット", font=title_font).place(x=x_right, y=y)
        y += 30
        self.pet_prices = [
            ("一泊（ペット）(1000円)", 1000),
            ("スパ入浴利用料(1800円)", 1800),
            ("スパ入浴利用料（二泊目）(1000円)", 1000)
        ]
        self.pet_combos = []
        for pet, price in self.pet_prices:
            tk.Label(self.option_newwindow, text=pet, font=label_font).place(x=x_right, y=y)
            combo = ttk.Combobox(self.option_newwindow, values=[str(i) for i in range(10)], width=4, font=("", 11))
            combo.set("0")
            combo.place(x=x_right + 260, y=y)  # 少し右にずらす
            self.pet_combos.append((combo, price))
            y += 25
        # ---- 日帰り入浴 ----
        y += 20
        tk.Label(self.option_newwindow, text="日帰り入浴", font=title_font).place(x=x_right, y=y)
        y += 30
        self.dayuse_prices = [
            ("大人(650円)", 650),
            ("子供(300円)", 300)
        ]
        self.dayuse_combos = []
        for item, price in self.dayuse_prices:
            tk.Label(self.option_newwindow, text=item, font=label_font).place(x=x_right, y=y)
            combo = ttk.Combobox(self.option_newwindow, values=[str(i) for i in range(10)], width=4, font=("", 11))
            combo.set("0")
            combo.place(x=x_right + 260, y=y)
            self.dayuse_combos.append((combo, price))
            y += 25
        # ---- 岩盤浴 ----
        y += 20
        tk.Label(self.option_newwindow, text="岩盤浴", font=title_font).place(x=x_right, y=y)
        y += 30
        self.rockbath_prices = [
            ("浴衣だけ(2000円)", 2000),
            ("宿泊の人(1500円)", 1500)
        ]
        self.rockbath_combos = []
        for item, price in self.rockbath_prices:
            tk.Label(self.option_newwindow, text=item, font=label_font).place(x=x_right, y=y)
            combo = ttk.Combobox(self.option_newwindow, values=[str(i) for i in range(10)], width=4, font=("", 11))
            combo.set("0")
            combo.place(x=x_right + 260, y=y)
            self.rockbath_combos.append((combo, price))
            y += 25
        # ---- 合計ボタンと合計金額 ----
        tk.Button(self.option_newwindow, text="合計", font=("", 13), command=self.calculate_total).place(x=270, y=370)
        self.total_label = tk.Label(self.option_newwindow, text="合計金額: 0円", font=("", 13))
        self.total_label.place(x=370, y=370)
        
        self.option_next = tk.Button(self.option_newwindow, text="決定", font=("", 13), command=self.back_amount, fg="white", bg="#576FC5")
        self.option_next.place(x=600, y=370)
        
    def back_amount(self):
        self.option_newwindow.destroy()
        
    def calculate_total(self):
        self.total = 0
        for combo, price in self.addmeal_combos:
            self.total += int(combo.get()) * price
        for combo, price in self.pet_combos:
            self.total += int(combo.get()) * price
        for combo, price in self.dayuse_combos:
            self.total += int(combo.get()) * price
        for combo, price in self.rockbath_combos:
            self.total += int(combo.get()) * price
        self.total += int(self.drink_combo.get()) *2000
        self.total_label.config(text=f"合計金額: {self.total}円")
        
    
    def amount_button(self):
        if self.flg == True:
            self.plan_basic_num.place_forget()
            self.plan_basic_num2.place_forget()
            self.plan_basic_num3.place_forget()
            self.final_amount.place_forget()
            self.sum_once.place_forget()
            self.sum_once_num2.place_forget()
            
            
        self.sum_amount = 0
        self.room_grade = 0
        if self.room == "岩手山展望露天風呂付き和室" or self.room == "檜の内風呂付き本館和洋室":
            self.room_grade = 2000
            if self.room == "岩手山展望露天風呂付き和室":
                self.room_grade = 3000
        for self.plan in self.all_plan_amounts:
            if self.plan[0] == self.plan_name:
                self.now_plan = self.plan
    
        # 料金の表示
        # 大人計算
        self.plan_basic = tk.Label(self.canvas, text="基本料金（大人）", font=("", 13))
        self.plan_basic.place(x=500, y=120)
        self.sum_amount = self.sum_amount + self.now_plan[1]*int(self.big_people_entry.get())
        self.plan_basic_num = tk.Label(self.canvas, text=f"{self.now_plan[1]}  ×  {self.big_people_entry.get()}", font=("", 13))
        self.plan_basic_num.place(x=650, y=120)
        # 子供計算
        self.plan_basic2 = tk.Label(self.canvas, text="　　　　　　 （子供）", font=("", 13))
        self.plan_basic2.place(x=500, y=150)
        self.sum_amount = self.sum_amount + 7500*int(self.small_people_entry.get())
        self.plan_basic_num2 = tk.Label(self.canvas, text=f"7500  ×  {self.small_people_entry.get()}", font=("", 13))
        self.plan_basic_num2.place(x=650, y=150)
        # お部屋グレード計算
        self.plan_basic3 = tk.Label(self.canvas, text="部屋グレードアップ", font=("", 13))
        self.plan_basic3.place(x=500, y=180)
        self.sum_amount = self.sum_amount + self.room_grade
        self.plan_basic_num3 = tk.Label(self.canvas, text=self.room_grade, font=("", 13))
        self.plan_basic_num3.place(x=650, y=180)
        # 線表示 & 一時合計金額表示
        self.canvas.create_line(500, 220, 750, 220, fill = "black")
        self.sum_once = tk.Label(self.canvas, text="泊数", font=("", 13))
        self.sum_once.place(x=500, y=240)
        self.sum_once_num = tk.Label(self.canvas, text=f"{self.sum_amount}  ×  {self.day_select.get()}", font=("", 13))
        self.sum_once_num.place(x=650, y=240)
        self.sum_amount = self.sum_amount * int(self.day_select.get())
        # オプション計算
        self.sum_once2 = tk.Label(self.canvas, text="オプション", font=("", 13))
        self.sum_once2.place(x=500, y=270)
        self.sum_once_num2 = tk.Label(self.canvas, text=self.total, font=("", 13))
        self.sum_once_num2.place(x=650, y=270)
        # 線表示 & 最終合計金額表示
        self.canvas.create_line(500, 310, 750, 310, fill = "black")
        self.canvas.create_line(500, 315, 750, 315, fill = "black")
        self.sum_amount = self.sum_amount + self.total
        self.final_amount = tk.Label(self.canvas, text=self.sum_amount, font=("", 14))
        self.final_amount.place(x=700, y=330)
        
        self.button = tk.Button(text="予約確定", command=self.final_click, width=13, height=2, font=("", 12))
        self.button.place(x=660, y=460)

        self.flg = True
    
    def final_click(self):
        if self.name_entry.get() == "" or self.mail_entry.get() == "":
            messagebox.showwarning("エラー", "名前とメールを入力してください。")
        else:
            # メール送信
            to = self.mail_entry.get()
            subject = "【〇〇ホテル】ご予約内容のお知らせ"
            body = f"""
                    <html>
                    <head></head>
                    <body>
                    <h3>{self.name_entry.get()}様</h3>
                    <h4>この度は、〇〇ホテルをご予約いただき、誠にありがとうございます。<br>
                    以下の内容でご予約を承りました。</h4>
                    <ul>
                        <li>プラン: {self.plan_name}</li>
                        <li>部屋タイプ: {self.room}</li>
                        <li>チェックイン日: {self.date}</li>
                        <li>大人: {self.big_people_entry.get()}名</li>
                        <li>子供: {self.big_people_entry.get()}名</li>
                    </ul>
                    <h4>合計金額：{self.sum_amount}円</h4>
                    <h4>ご到着を心よりお待ちしております。</h4>
                    <p>〇〇ホテル</p>
                    </body>
                    </html>
                    """
            self.send_mail(to, subject, body)
        name = self.name_entry.get()
        email = self.mail_entry.get()
        data = {
            "お名前": name,
            "メールアドレス": email,
            "選択プラン": self.plan_name,
            "料金": self.sum_amount
        }
        with open("user_info.json", "a", encoding="utf-8") as f:    #aは追記モード
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.write('\n') # JSONオブジェクトを改行で区切る (読み込みやすくするため)
            
    def send_mail(self, to, subject, body):
        # 後で変更
        ID = to
        PASS = os.environ['MAIL_PASS']
        HOST = 'smtp.gmail.com'
        PORT = 587

        # メールのインスタンスを作ってる
        msg = MIMEMultipart()
        # html形式で送るよー！（画像とか色とかできる）
        msg.attach(MIMEText(body, 'html'))

        msg['Subject'] = subject
        msg['From'] = ID
        msg['To'] = to

        # ここから送信処理
        server = SMTP(HOST, PORT)
        # tls = 暗号化通信　https
        server.starttls()
        server.login(ID, PASS)

        server.send_message(msg)
        server.quit() 
             
            
if __name__ == '__main__':
    root = tk.Tk()
    app = Amount_page(root, "2【イースター復活祭】×【女子旅】お部屋にはチョコレートたまご型お菓子などたくさん♪まったりしてねプラン(*´ω｀)", "岩手山展望露天風呂付き和室", 2, 0, "2025-01-01")
    app.pack()
    root.mainloop()