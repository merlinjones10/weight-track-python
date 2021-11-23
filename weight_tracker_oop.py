import tkinter as tk
from tkinter import messagebox
from datetime import date
from db import Database
#Global Vars
db = Database('weight_app.db')
today = date.today().strftime("%d/%m/%Y")
dayInWeek = date.today().strftime("%a")

# Main App/GUI

class Application(tk.Frame):
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        #
        main.geometry('700x350')
        self.create_widgets()
        self.populate_list()
    def create_widgets(self):
        # ENTRY BOXES
        # Date
        self.date_label = tk.Label(self.main, text='Date:', font=('bold', 14))
        self.date_label.grid(row=0, column=0, sticky=tk.W)
        self.date_text = tk.StringVar()
        self.date_entry = tk.Entry(self.main, textvariable=self.date_text)
        self.date_entry.insert(0, today)
        self.date_entry.grid(row=0, column=1)
        # Weight
        self.weight_label = tk.Label(self.main, text='Weight:', font=('bold', 14))
        self.weight_label.grid(row=1, column=0, sticky=tk.W)
        self.weight_text = tk.StringVar()
        self.weight_entry = tk.Entry(self.main, textvariable=self.weight_text)
        self.weight_entry.grid(row=1, column=1)
        #
        # BUTTONS
        self.add_btn = tk.Button(self.main, text="Add Item", width=12, command=self.add_data)
        self.add_btn.grid(row=2, column=0, pady=20)

        self.remove_btn = tk.Button(
            self.main, text="Remove Item", width=12, command=self.remove_item)
        self.remove_btn.grid(row=2, column=1)

        self.update_btn = tk.Button(
            self.main, text="Update Item", width=12, command=self.update_item)
        self.update_btn.grid(row=2, column=2)

        self.exit_btn = tk.Button(
            self.main, text="Clear Input", width=12, command=self.clear_text)
        self.exit_btn.grid(row=2, column=3)
        # Average Label
        self.display_btn = tk.Button(self.main, text="Show Average", width=12, command=self.calculate_average)
        self.display_btn.grid(row=2, column=4)
        self.display_label = tk.Label(self.main, text='7 Day average:', font=(14))
        self.average_text = tk.StringVar()
        self.average_text.set('')
        self.display_average_label = tk.Label(self.main, textvariable=self.average_text, font=(14))

        self.display_label.grid(row=3, column=5)
        self.display_average_label.grid(row=4, column=5)
        ##
        ## View box
        ##
        self.weights_list = tk.Listbox(self.main, height=8, width=50, border=0)
        self.weights_list.grid(row=3, column=0, columnspan=3)
        # Scroll bar
        self.scrollbar = tk.Scrollbar(self.main)
        self.scrollbar.grid(row=3, column=3)
        self.weights_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.weights_list.yview)
        #Binding
        self.weights_list.bind('<<ListboxSelect>>', self.select_item)
        ##
        ## end view box end
        ##


    def add_data(self):
        if self.weight_text.get() == '' or self.date_text.get() == '':
            messagebox.showerror('Error, Please enter all values')
            return
        db.insert(self.date_text.get(), int(self.weight_text.get()))
        self.weights_list.delete(0, tk.END)
        # self.weights_list
        self.clear_text()
        self.populate_list()

    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()


    def update_item(self):
        db.update(self.selected_item[0], self.date_text.get(
        ), int(self.weight_text.get()))
        self.populate_list()

    def populate_list(self):
        self.weights_list.delete(0, tk.END)
        for row in db.fetch():
            self.weights_list.insert(tk.END, row)

    def select_item(self, event):
        # # Create global selected item to use in other functions
        # global self.selected_item
        try:
            # Get index
            index = self.weights_list.curselection()[0]
            # Get selected item
            self.selected_item = self.weights_list.get(index)
            # print(selected_item) # Print tuple
            # Add text to entries
            self.weight_entry.delete(0, tk.END)
            self.weight_entry.insert(tk.END, self.selected_item[2])
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(tk.END, self.selected_item[1])
        except IndexError:
            pass

    def clear_text(self):
        self.weight_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def calculate_average(self):
            list_weights = [x[0] for x in db.fetch_seven()]
            average = round(sum(list_weights) / 7, 1)
            self.average_text.set(f'{average} lbs or {round(average /2.2046, 1)}kgs')





root = tk.Tk()
app = Application(main=root)
app.mainloop()