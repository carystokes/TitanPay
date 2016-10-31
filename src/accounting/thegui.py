import tkinter
from src.accounting import runpayroll
from src.accounting import employee_database
from src.accounting import receipts_db
from src.accounting import timecard_db


class TopGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('300x325+500+200')

        self.frame = tkinter.Frame(self.main_window)

        self.labelspace = tkinter.Label(self.frame, text='')
        self.label = tkinter.Label(self.frame, text='What would you like to do?')
        self.labelspace2 = tkinter.Label(self.frame, text='')

        self.import_employees_button = tkinter.Button(self.frame, width='25', bg='white', text='Import employees', command=employee_database.import_employees)
        self.import_timecards_button = tkinter.Button(self.frame, width='25', bg='white', text='Import timecards', command=timecard_db.import_timecards)
        self.import_receipts_button = tkinter.Button(self.frame, width='25', bg='white', text='Import receipts', command=receipts_db.import_receipts)
        self.process_payroll_button = tkinter.Button(self.frame, width='25', bg='white', text='Process payroll',
                                                     command=runpayroll.run_payroll)

        self.frame.pack()
        self.labelspace.pack()
        self.label.pack()
        self.labelspace2.pack()
        self.import_employees_button.pack()
        self.import_timecards_button.pack()
        self.import_receipts_button.pack()
        self.process_payroll_button.pack()

        tkinter.mainloop()

top_gui = TopGUI()