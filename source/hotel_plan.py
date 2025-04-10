import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class stayplan_page(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        master.geometry('900x600')
        master.title('Hello Tkinter')
        
        self.create_widgets()
        
    def create_widgets(self):

        self.all_plans = [
            "1【2025年春休み】家族旅行応援！お子様歓迎♪早いもの勝ち！春休み限定プラン",
            "2【イースター復活祭】×【女子旅】お部屋にはチョコレートたまご型お菓子などたくさん♪まったりしてねプラン",
            "3【2025ゴールデンウィーク★プレミアムプラン】前沢牛の豪華会席GWバージョンで特別なひと時を♪",
            "4【スタンダード】【HP特価】八幡平産杜仲茶ポークの和食膳プラン",
            "5【岩手県産牛】【HP特価】岩手県産牛と八幡平産杜仲茶ポークを味わう旬の味覚和食膳",
            "6【前沢牛】【HP予約特典付き】≪ちょっと贅沢なご夕食≫ 前沢牛のせいろ蒸しとロースト前沢牛の握り付き和食膳プラン",
            "7【前沢牛】【HP予約特典付き】≪ちょっと贅沢なご夕食≫ 前沢牛の網焼きとロースト前沢牛の握り付き和食膳プラン",
            "8【前沢牛】【３つの特典付き】前沢牛＆伊勢海老＆あわび＆ズワイガニのおまねきプラン",
            "9【前沢牛】前沢牛・伊勢海老・あわび・ズワイガニの豪華和食膳プラン",
            "10【お誕生・記念日プラン】(*≧∇≦)/ ホールケーキ付♪サプライズでお祝いしましょ♪",
            "11【早期割90日までご予約で15％割引】岩手県産牛と八幡平産杜仲茶ポークを味わう旬の味覚 和食膳",
            "12【早期割90日までご予約で15％割引】前沢牛・伊勢海老・あわび・ズワイガニの和食膳",
            "13【早期割60日までご予約で10％割引】岩手県産牛と八幡平産杜仲茶ポークを味わう旬の味覚 和食膳",
            "14【早期割60日までご予約で10％割引】前沢牛・伊勢海老・あわび・ズワイガニの和食膳",
            "15【赤ちゃんプラン】～お子様歓迎♪パパママも嬉しい12個の特典付き",
            "16【赤ちゃんプラン・お食い初め】これからの成長と健康の願いを込めて～パパママも嬉しい12個の特典付き～",
            "17【早期割90日までご予約で15％割引】温泉露天風呂付『黒倉の間』『源太の間』",
            "18【早期割60日までご予約で10％割引】温泉露天風呂付『黒倉の間』『源太の間』",
            "19【別館姫神】檜の温泉露天風呂付き『黒倉の間』『源太の間』",
            "20【早期割90日までご予約で15％割引】温泉内風呂付き『見返の間』",
            "21【早期割60日までご予約で10％割引】温泉内風呂付き『見返の間』",
            "22【別館姫神】檜の温泉内風呂付き『見返の間』",
            "23【早期割90日までご予約で15％割引】檜の温泉内風呂付き『茶臼の間』『七時雨の間』",
            "24【早期割60日までご予約で10％割引】檜の温泉内風呂付き『茶臼の間』『七時雨の間』",
            "25【別館姫神】檜の温泉内風呂付き『茶臼の間』『七時雨の間』",
            "26【別館姫神】檜の温泉内風呂付き『貴賓室』",
            "27【北投石の岩盤浴】豊かな八幡平の自然と岩盤浴でリフレッシュする旅を～八幡平産杜仲茶ポークの和食膳～",
            "28【朝食付き】観光、ビジネス！一泊朝食プランでお気軽に八幡平を満喫！",
            "29【8/13～8/15】2025お盆期間限定♪お子様歓迎！スイカ割り・森のスタンプラリー・ミニ縁日や夜のイベントなどお楽しみ盛りだくさん",
            "30【八幡平の地ビール・ドラゴンアイビールで乾杯】八幡平の地産の恵みと八幡平のクラフトビールを楽しむプラン"
        ]
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.top_frame = tk.Frame(self)
        self.top_frame.grid(row=0, column=0, padx=10, pady=25, sticky="nsew")
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.plan_listbox = tk.Listbox(self.top_frame, selectmode=tk.SINGLE, font=("Helvetica", 10), height=22)
        self.plan_listbox.grid(row=0, column=0, sticky="nsew")
        self.scrollbar = tk.Scrollbar(self.top_frame, orient=tk.VERTICAL, command=self.plan_listbox.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.plan_listbox.config(yscrollcommand=self.scrollbar.set)
        self.plan_listbox.bind("<<ListboxSelect>>", self.on_plan_select)
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.left_bottom_frame = tk.Frame(self.bottom_frame)
        self.left_bottom_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        tk.Label(self.left_bottom_frame, text="オプション", font=("Helvetica", 12, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.option_keywords = {
            "早割・早得": ["早期割90", "早期割60"],
            "ご夕食は岩手県産牛": ["岩手県産牛"],
            "別館姫神温泉付き客室": ["別館姫神"],
            "お子様歓迎！赤ちゃんと一緒♪": ["赤ちゃん", "お子様歓迎"],
            "ご夕食は前沢牛": ["前沢牛", "お誕生", "記念日", "黒倉の間", "源太の間", "見返の間", "茶臼の間", "七時雨の間"],
            "ご夕食はスタンダード": ["スタンダード"],
            "記念日・お祝い": ["記念日", "お誕生"],
            "1泊朝食付・素泊まり": ["朝食付き", "素泊まり"]
        }
        self.check_vars = {}
        for i, option in enumerate(self.option_keywords.keys()):
            var = tk.BooleanVar()
            self.check_vars[option] = var
            cb = tk.Checkbutton(self.left_bottom_frame, text=option, variable=var, command=self.update_plan_list)
            cb.grid(row=i//4 + 1, column=i%4, sticky="w", padx=5, pady=3)
        self.right_bottom_frame = tk.Frame(self.bottom_frame)
        self.right_bottom_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.next_button = tk.Button(self.right_bottom_frame, text="この条件で検索する", command=self.next_page, height=3)
        self.next_button.grid(row=2, column=1, columnspan=6, pady=10)
        self.update_plan_list()
        
    def update_plan_list(self):
        selected_keywords = []
        for option, var in self.check_vars.items():
            if var.get():
                selected_keywords.extend(self.option_keywords[option])
        self.plan_listbox.delete(0, tk.END)
        for plan in self.all_plans:
            if not selected_keywords or any(keyword in plan for keyword in selected_keywords):
                self.plan_listbox.insert(tk.END, plan)
    def on_plan_select(self, event):
        selected_index = self.plan_listbox.curselection()
        if selected_index:
            self.plan_listbox.selection_clear(0, tk.END)
            self.plan_listbox.selection_set(selected_index)
            self.plan_listbox.activate(selected_index)
            
    # 次ページへの遷移（プラン名を引き渡し）
    def next_page(self):
        if self.plan_listbox.selection_get():
            plan_name = self.plan_listbox.selection_get()
            from check_plan import Check_page
            self.destroy()
            Check_page(self.master, plan_name)
         
if __name__ == '__main__':
    root = tk.Tk()
    app = stayplan_page(root)
    app.mainloop()









