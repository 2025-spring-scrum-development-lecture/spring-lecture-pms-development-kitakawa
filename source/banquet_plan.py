import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=900, height=600)
        self.pack()
        
        master.geometry('900x600')
        master.title('Hello Tkinter')
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(text="宴会プラン選択", font=("", 16))
        self.label.place(x=150, y=100)
        self.course_one = tk.Button(self, text="豪華コース", font=("", 15), command=self.next_one, bg="white", relief="groove")
        self.course_one.place(x=200, y=150, width=250, height=150)
        self.course_two = tk.Button(self, text="雅(みやび)コース", font=("", 15), command=self.next_two, bg="white", relief="groove")
        self.course_two.place(x=460, y=150, width=250, height=150)
        self.course_three = tk.Button(self, text="錦(にしき)コース", font=("", 15), command=self.next_three, bg="white", relief="groove")
        self.course_three.place(x=200, y=320, width=250, height=150)
        self.course_four = tk.Button(self, text="椿(つばき)コース", font=("", 15), command=self.next_four, bg="white", relief="groove")
        self.course_four.place(x=460, y=320, width=250, height=150)
        
    def next_one(self):
        plan_name = "豪華コース"
        self.next_page(plan_name)
    def next_two(self):
        plan_name = "雅(みやび)コース"
        self.next_page(plan_name)
    def next_three(self):
        plan_name = "錦(にしき)コース"
        self.next_page(plan_name)
    def next_four(self):
        plan_name = "椿(つばき)コース"
        self.next_page(plan_name)
        
        
    def next_page(self, plan_name):
        plan_name = f"宴会-{plan_name}"
        from check_plan import Check_page
        self.destroy()
        Check_page(self.master, plan_name)
    
 
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()