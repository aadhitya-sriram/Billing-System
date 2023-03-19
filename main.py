import tkinter as tk
import datetime as dt
import random as rd

MAIN_FONT = ("Consolas",25)

class App:
    
    def __init__(self):
        '''This function initializes the Application and the required attributes'''
        
        self.objs = []
        self.win = tk.Tk()
        self.win.eval('tk::PlaceWindow . Center')
        self.win.resizable(False,False)
        self.win.title = "Billing project"
        self.win.geometry = "1000x100"
        self.phase1()

    def check_num(self,number):
        '''This function checks if the entered phone number is valid or not'''
        
        while len(number) != 10 or number.isdigit() == False:
            self.invalid_label.destroy()
            self.invalid_label = tk.Label(self.win, text='INVALID Phone Number!', font=MAIN_FONT, fg="red")
            self.invalid_label.grid()
            break
        else:
            self.phase2()

    def phase1(self):
        '''This function initializes the first phase of the application'''
        
        tk.Label(self.win,text="Enter phone number:",font=MAIN_FONT).grid(padx=20,pady=20)
        self.invalid_label = tk.Label(self.win,text="")
        ent_lab = tk.Entry(self.win,font=MAIN_FONT)
        ent_lab.grid()
        tk.Button(self.win,text="Submit",command=lambda:self.phase1to2(ent_lab.get()),font=MAIN_FONT).grid(padx=20,pady=20)

    def phase1to2(self,num):
        '''This function is the bridge between Phases 1 and 2'''
        
        self.phonenum = num
        self.items()
        self.check_num(num)

    def phase2(self):
        '''This function initializes the second phase of the application'''
        
        self.clear()
        tk.Label(self.win,text="ITEM",font=MAIN_FONT).grid(row=0,column=0,padx=20,pady=20)
        tk.Label(self.win,text="PRICE",font=MAIN_FONT).grid(row=0,column=1,padx=20,pady=20)
        tk.Label(self.win,text="QUANTITY",font=MAIN_FONT).grid(row=0,column=2,columnspan=3,padx=20,pady=20)

        r=1
        for frt in self.objs:
            frt.place_cart(r)
            r+=1
        submit_btn = tk.Button(self.win,text="Submit",command=lambda:self.phase3(), font=MAIN_FONT)
        submit_btn.grid(row=r,column = 1,padx=20,pady=20)

    def total_bill(self):
        '''This function returns the total bill amount'''
        
        total=0
        for frt in self.objs:
            total+=frt.price*frt.qty
        return total

    def phase3(self):
        '''This function initializes the third phase of the application'''
        
        self.clear()
        total= self.total_bill()

        tk.Label(self.win,text="ITEM",font=MAIN_FONT).grid(row=0,column=0,padx=20,pady=20)
        tk.Label(self.win,text="QUANTITY",font=MAIN_FONT).grid(row=0,column=1,padx=20,pady=20)
        tk.Label(self.win,text="AMOUNT",font=MAIN_FONT).grid(row=0,column=2,padx=20,pady=20)

        r=1
        for item in self.objs:
            if item.qty !=0:
                item.place_bill(r)
                r+=1
            if r==1:
                tk.Label(self.win,text="None",font=MAIN_FONT).grid(row=r,column=0,padx=20,pady=20)
                tk.Label(self.win,text="0",font=MAIN_FONT).grid(row=r,column=1,padx=20,pady=20)
                tk.Label(self.win,text="0",font=MAIN_FONT).grid(row=r,column=2,padx=20,pady=20)
                r+=1
                    
        total_lab = tk.Label(self.win,text="TOTAL:",font=MAIN_FONT)
        total_lab.grid(row=r,column=1,padx=20,pady=20)
        total_amt = tk.Label(self.win,text=total,font=MAIN_FONT)
        total_amt.grid(row=r,column=2,padx=20,pady=20)

        back_btn = tk.Button(self.win,text="Back",command=lambda:self.phase2(),font=MAIN_FONT)
        back_btn.grid(row=r+1,column=0,padx=20,pady=20)
        next_btn = tk.Button(self.win,text="NEXT",command=self.phase4,font=MAIN_FONT)
        next_btn.grid(row=r+1,column=2,padx=20,pady=20)
        
    def phase4(self):
        '''This function initializes the final phase of the application'''
        
        self.clear()
        self.write_txt_file()
        tk.Label(self.win,text="Thank you for shopping with us!",font=MAIN_FONT).grid(padx=20,pady=20)

    #MISC FUNCTIONS:
    def clear(self):
        '''This function erases the widgets in the GUI window'''

        for wid in self.win.winfo_children():
            wid.destroy()

    def items(self):
        '''This function is used to add items to the billing system'''
        
        apple = Item("Apple",60)
        mango = Item("Mango",40)
        banana = Item("Banana",30)
        orange = Item("Orange",60)

    def run(self):
        self.win.mainloop()

    def write_txt_file(self):
        ''''''

        bno = rd.randint(1,100)
        date_time = dt.datetime.now()
        date_now = date_time.strftime("%d.%m.%Y")
        time_now = date_time.strftime("%H:%M:%S")
        bill_str = f"Bill No: {bno}\nDate: {date_now}\nTime: {time_now}\n"
        bill_str += "\nS.no\tPrice\tQuantity\tAmount\tItem\n"
        
        c=1
        for item in self.objs:
            amount = item.price * item.qty
            bill_str += f"{c}\t{item.price}\t{item.qty}\t\t{amount}\t\t{item.name}\n"
            c+=1

        bill_str += f"\n\nTotal Bill: {self.total_bill()}\n\nThank you for shopping with us!\nCome again soon!\n"

        file_name = f"[{self.phonenum}] - [{date_now}]"
        f = open(f"./Reciepts/{file_name}.txt","w")
        f.write(bill_str)
        f.close()

class Item:
    
    def __init__(self,name,price):
        '''This function initializes the Items and the required attributes'''
        
        self.name = name
        self.price = price
        self.qty = 0
        app.objs.append(self)

    def place_cart(self,r):
        '''This function displays all the item data in Phase 2 of the application'''
        
        self.flab = tk.Label(app.win,text=self.name,font=MAIN_FONT)
        self.mlab = tk.Label(app.win,text=self.price,font=MAIN_FONT)
        self.pbut = tk.Button(app.win,text="+",command=lambda:self.add(),font=MAIN_FONT)
        self.qlab = tk.Label(app.win,text=self.qty,font=MAIN_FONT)
        self.mbut = tk.Button(app.win,text="-",command=lambda:self.sub(),font=MAIN_FONT)
        self.flab.grid(row=r,column=0)
        self.mlab.grid(row=r,column=1)
        self.pbut.grid(row=r,column=4)
        self.qlab.grid(row=r,column=3)
        self.mbut.grid(row=r,column=2)
    
    def place_bill(self,r):
        '''This function displays the selected item data in Phase 3 of the application'''
        
        self.name_lab = tk.Label(app.win,text=self.name,font=MAIN_FONT)
        self.quant_lab = tk.Label(app.win,text=self.qty,font=MAIN_FONT)
        self.amount_lab = tk.Label(app.win,text=self.price*self.qty,font=MAIN_FONT)
        self.name_lab.grid(row=r,column=0)
        self.quant_lab.grid(row=r,column=1)
        self.amount_lab.grid(row=r,column=2)

    def add(self):
        '''This function increments the quantity of an item'''
        
        q = int(self.get_count())
        self.qlab.configure(text=str(q+1))
        self.qty+=1

    def sub(self):
        '''This function decrements the quantity of an item'''
        
        q = int(self.get_count())
        if q != 0:
            self.qlab.configure(text=str(q-1))
            self.qty-=1
    
    def get_count(self):
        '''This function returns the quantity of the item'''
        
        return self.qlab.cget("text")
        
if __name__ == "__main__":
    app = App()
    app.run()