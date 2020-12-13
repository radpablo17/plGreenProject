from tkinter import *
import sqlite3
from tkcalendar import DateEntry
from tkinter import messagebox

root = Tk()
root.title("Expense Calculator")
root.geometry("500x400")


def reset():
    global query_label
    global tot_label
    name.delete(0, END)
    value.delete(0, END)
    box_delete.delete(0, END)
    query_label.config(text="")
    tot_label.config(text="")


def delete():
    conn = sqlite3.connect("Expense.db")
    c = conn.cursor()
    try:
        if int(box_delete.get()) != 0:
            if date.get() >= "1/1/20" and date.get() <= "1/31/20":
                c.execute("DELETE from januaryExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
            elif date.get() >= "2/1/20" and date.get() <= "2/29/20":
                c.execute("DELETE from februaryExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
            elif date.get() >= "3/1/20" and date.get() <= "3/31/20":
                c.execute("DELETE from marchExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
            elif date.get() >= "4/1/20" and date.get() <= "4/30/20":
                c.execute("DELETE from aprilExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
            elif date.get() >= "5/1/20" and date.get() <= "5/31/20":
                c.execute("DELETE from mayExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
            elif date.get() >= "6/1/20" and date.get() <= "6/30/20":
                c.execute("DELETE from juneExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
            elif date.get() >= "7/1/20" and date.get() <= "7/31/20":
                c.execute("DELETE from julyExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
            elif date.get() >= "8/1/20" and date.get() <= "8/31/20":
                c.execute("DELETE from augustExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
            elif date.get() >= "9/1/20" and date.get() <= "9/30/20":
                c.execute("DELETE from septemberExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
            elif date.get() >= "10/1/20" and date.get() <= "10/31/20":
                c.execute("DELETE from octoberExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
            elif date.get() >= "11/1/20" and date.get() <= "11/30/20":
                c.execute("DELETE from novemberExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
            elif date.get() >= "12/1/20" and date.get() <= "12/31/20":
                c.execute("DELETE from decemberExpenses WHERE oid= " + box_delete.get())
                box_delete.delete(0, END)
        else:
            messagebox.showerror("Error", "ID number cannot be 0")
    except ValueError:
        messagebox.showerror("Error", "ID number cannot be blank")
    conn.commit()
    conn.close()


def create_database():
    conn = sqlite3.connect("Expense.db")
    c = conn.cursor()
    if date.get() in ['1/1/20', '1/2/20', '1/3/20', '1/4/20', '1/5/20', '1/6/20', '1/7/20', '1/8/20',
                      '1/9/20', '1/10/20', '1/11/20', '1/12/20', '1/13/20', '1/14/20', '1/15/20', '1/16/20',
                      '1/17/20', '1/18/20', '1/19/20', '1/20/20', '1/21/20', '1/22/20', '1/23/20', '1/24/20',
                      '1/25/20', '1/26/20', '1/27/20', '1/28/20', '1/29/20', '1/30/20', '1/31/20', '2/1/20', '2/2/20',
                      '2/3/20', '2/4/20', '2/5/20', '2/6/20', '2/7/20', '2/8/20',
                      '2/9/20', '2/10/20', '2/11/20', '2/12/20', '2/13/20', '2/14/20', '2/15/20', '2/16/20',
                      '2/17/20', '2/18/20', '2/19/20', '2/20/20', '2/21/20', '2/22/20', '2/23/20', '2/24/20',
                      '2/25/20', '2/26/20', '2/27/20', '2/28/20', '2/29/20', '3/1/20', '3/2/20',
                      '3/3/20', '3/4/20', '3/5/20', '3/6/20', '3/7/20', '3/8/20',
                      '3/9/20', '3/10/20', '3/11/20', '3/12/20', '3/13/20', '3/14/20', '3/15/20', '3/16/20',
                      '3/17/20', '3/18/20', '3/19/20', '3/20/20', '3/21/20', '3/22/20', '3/23/20', '3/24/20',
                      '3/25/20', '3/26/20', '3/27/20', '3/28/20', '3/29/20', '3/30/20', '3/31/20', '4/1/20', '4/2/20',
                      '4/3/20', '4/4/20', '4/5/20', '4/6/20', '4/7/20', '4/8/20',
                      '4/9/20', '4/10/20', '4/11/20', '4/12/20', '4/13/20', '4/14/20', '4/15/20', '4/16/20',
                      '4/17/20', '4/18/20', '4/19/20', '4/20/20', '4/21/20', '4/22/20', '4/23/20', '4/24/20',
                      '4/25/20', '4/26/20', '4/27/20', '4/28/20', '4/29/20', '4/30/20', '5/1/20', '5/2/20',
                      '5/3/20', '5/4/20', '5/5/20', '5/6/20', '5/7/20', '5/8/20',
                      '5/9/20', '5/10/20', '5/11/20', '5/12/20', '5/13/20', '5/14/20', '5/15/20', '5/16/20',
                      '5/17/20', '5/18/20', '5/19/20', '5/20/20', '5/21/20', '5/22/20', '5/23/20', '5/24/20',
                      '5/25/20', '5/26/20', '5/27/20', '5/28/20', '5/29/20', '5/30/20', '5/31/20', '6/1/20', '6/2/20', '6/3/20',
                      '6/4/20', '6/5/20', '6/6/20', '6/7/20', '6/8/20',
                      '6/9/20', '6/10/20', '6/11/20', '6/12/20', '6/13/20', '6/14/20', '6/15/20', '6/16/20',
                      '6/17/20', '6/18/20', '6/19/20', '6/20/20', '6/21/20', '6/22/20', '6/23/20', '6/24/20',
                      '6/25/20', '6/26/20', '6/27/20', '6/28/20', '6/29/20', '6/30/20', '7/1/20', '7/2/20', '7/3/20',
                      '7/4/20', '7/5/20', '7/6/20', '7/7/20', '7/8/20',
                      '7/9/20', '7/10/20', '7/11/20', '7/12/20', '7/13/20', '7/14/20', '7/15/20', '7/16/20',
                      '7/17/20', '7/18/20', '7/19/20', '7/20/20', '7/21/20', '7/22/20', '7/23/20', '7/24/20',
                      '7/25/20', '7/26/20', '7/27/20', '7/28/20', '7/29/20', '7/30/20', '7/31/20', '8/1/20', '8/2/20',
                      '8/3/20', '8/4/20', '8/5/20', '8/6/20', '8/7/20', '8/8/20',
                      '8/9/20', '8/10/20', '8/11/20', '8/12/20', '8/13/20', '8/14/20', '8/15/20', '8/16/20',
                      '8/17/20', '8/18/20', '8/19/20', '8/20/20', '8/21/20', '8/22/20', '8/23/20', '8/24/20',
                      '8/25/20', '8/26/20', '8/27/20', '8/28/20', '8/29/20', '8/30/20', '8/31/20', '9/1/20', '9/2/20',
                      '9/3/20', '9/4/20', '9/5/20', '9/6/20', '9/7/20', '9/8/20',
                      '9/9/20', '9/10/20', '9/11/20', '9/12/20', '9/13/20', '9/14/20', '9/15/20', '9/16/20',
                      '9/17/20', '9/18/20', '9/19/20', '9/20/20', '9/21/20', '9/22/20', '9/23/20', '9/24/20',
                      '9/25/20', '9/26/20', '9/27/20', '9/28/20', '9/29/20', '9/30/20', '10/1/20', '10/2/20', '10/3/20',
                      '10/4/20', '10/5/20', '10/6/20', '10/7/20', '10/8/20',
                      '10/9/20', '10/10/20', '10/11/20', '10/12/20', '10/13/20', '10/14/20', '10/15/20', '10/16/20',
                      '10/17/20', '10/18/20', '10/19/20', '10/20/20', '10/21/20', '10/22/20', '10/23/20', '10/24/20',
                      '10/25/20', '10/26/20', '10/27/20', '10/28/20', '10/29/20', '10/30/20', '10/31/20', '11/1/20', '11/2/20',
                      '11/3/20', '11/4/20', '11/5/20', '11/6/20', '11/7/20', '11/8/20',
                      '11/9/20', '11/10/20', '11/11/20', '11/12/20', '11/13/20', '11/14/20', '11/15/20', '11/16/20',
                      '11/17/20', '11/18/20', '11/19/20', '11/20/20', '11/21/20', '11/22/20', '11/23/20', '11/24/20',
                      '11/25/20', '11/26/20', '11/27/20', '11/28/20', '11/29/20', '11/30/20', '12/1/20', '12/2/20',
                      '12/3/20', '12/4/20', '12/5/20', '12/6/20', '12/7/20', '12/8/20',
                      '12/9/20', '12/10/20', '12/11/20', '12/12/20', '12/13/20', '12/14/20', '12/15/20', '12/16/20',
                      '12/17/20', '12/18/20', '12/19/20', '12/20/20', '12/21/20', '12/22/20', '12/23/20', '12/24/20',
                      '12/25/20',
                      '12/26/20', '12/27/20', '12/28/20', '12/29/20', '12/30/20', '12/31/20']:
        c.execute("""CREATE TABLE januaryExpenses(
            date date,
            name text,
            expense integer
        )""")
        c.execute("""CREATE TABLE februaryExpenses(
            date date,
            name text,
            expense integer
        );""")
        c.execute("""CREATE TABLE marchExpenses(
                date date,
                name text,
                expense integer
            )""")
        c.execute("""CREATE TABLE aprilExpenses(
                date date,
                name text,
                expense integer
            );""")
        c.execute("""CREATE TABLE mayExpenses(
                date date,
                name text,
                expense integer
            )""")
        c.execute("""CREATE TABLE juneExpenses(
                date date,
                name text,
                expense integer
            );""")
        c.execute("""CREATE TABLE julyExpenses(
                date date,
                name text,
                expense integer
            )""")
        c.execute("""CREATE TABLE augustExpenses(
                date date,
                name text,
                expense integer
            );""")
        c.execute("""CREATE TABLE septemberExpenses(
                    date date,
                    name text,
                    expense integer
                )""")
        c.execute("""CREATE TABLE octoberExpenses(
                    date date,
                    name text,
                    expense integer
                );""")
        c.execute("""CREATE TABLE novemberExpenses(
                    date date,
                    name text,
                    expense integer
                )""")
        c.execute("""CREATE TABLE decemberExpenses(
                    date date,
                    name text,
                    expense integer
                );""")
    conn.commit()
    conn.close()


def query():
    try:
        global query_label
        global tot_label
        conn = sqlite3.connect("Expense.db")
        c = conn.cursor()
        query_label.config(text="")
        tot_label.config(text="")
        tot = 0
        if date.get() in ['1/1/20', '1/2/20', '1/3/20', '1/4/20', '1/5/20', '1/6/20', '1/7/20', '1/8/20',
                            '1/9/20', '1/10/20', '1/11/20', '1/12/20', '1/13/20', '1/14/20', '1/15/20', '1/16/20',
                            '1/17/20', '1/18/20', '1/19/20', '1/20/20', '1/21/20', '1/22/20', '1/23/20', '1/24/20',
                            '1/25/20', '1/26/20', '1/27/20', '1/28/20', '1/29/20', '1/30/20', '1/31/20']:
            c.execute("SELECT *, oid FROM januaryExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM januaryExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot_label = Label(root, text=tot)
            tot_label.grid(row=1, column=3)
        elif date.get() in ['2/1/20', '2/2/20', '2/3/20', '2/4/20', '2/5/20', '2/6/20', '2/7/20', '2/8/20',
                            '2/9/20', '2/10/20', '2/11/20', '2/12/20', '2/13/20', '2/14/20', '2/15/20', '2/16/20',
                            '2/17/20', '2/18/20', '2/19/20', '2/20/20', '2/21/20', '2/22/20', '2/23/20', '2/24/20',
                            '2/25/20', '2/26/20', '2/27/20', '2/28/20', '2/29/20']:
            c.execute("SELECT *, oid FROM februaryExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM februaryExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot_label = Label(root, text=tot)
            tot_label.grid(row=1, column=3)
        elif date.get() in ['3/1/20', '3/2/20', '3/3/20', '3/4/20', '3/5/20', '3/6/20', '3/7/20', '3/8/20',
                            '3/9/20', '3/10/20', '3/11/20', '3/12/20', '3/13/20', '3/14/20', '3/15/20', '3/16/20',
                            '3/17/20', '3/18/20', '3/19/20', '3/20/20', '3/21/20', '3/22/20', '3/23/20', '3/24/20',
                            '3/25/20', '3/26/20', '3/27/20', '3/28/20', '3/29/20', '3/30/20', '3/31/20']:
            c.execute("SELECT *, oid FROM marchExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM marchExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot_label = Label(root, text=tot)
            tot_label.grid(row=1, column=3)
        elif date.get() in ['4/1/20', '4/2/20', '4/3/20', '4/4/20', '4/5/20', '4/6/20', '4/7/20', '4/8/20',
                            '4/9/20', '4/10/20', '4/11/20', '4/12/20', '4/13/20', '4/14/20', '4/15/20', '4/16/20',
                            '4/17/20', '4/18/20', '4/19/20', '4/20/20', '4/21/20', '4/22/20', '4/23/20', '4/24/20',
                            '4/25/20', '4/26/20', '4/27/20', '4/28/20', '4/29/20', '4/30/20']:
            c.execute("SELECT *, oid FROM aprilExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM aprilExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot_label = Label(root, text=tot)
            tot_label.grid(row=1, column=3)
        elif date.get() in ['5/1/20', '5/2/20', '5/3/20', '5/4/20', '5/5/20', '5/6/20', '5/7/20', '5/8/20',
                            '5/9/20', '5/10/20', '5/11/20', '5/12/20', '5/13/20', '5/14/20', '5/15/20', '5/16/20',
                            '5/17/20', '5/18/20', '5/19/20', '5/20/20', '5/21/20', '5/22/20', '5/23/20', '5/24/20',
                            '5/25/20', '5/26/20', '5/27/20', '5/28/20', '5/29/20', '5/30/20', '5/31/20']:
            c.execute("SELECT *, oid FROM mayExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM mayExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot_label = Label(root, text=tot)
            tot_label.grid(row=1, column=3)
        elif date.get() in ['6/1/20', '6/2/20', '6/3/20', '6/4/20', '6/5/20', '6/6/20', '6/7/20', '6/8/20',
                            '6/9/20', '6/10/20', '6/11/20', '6/12/20', '6/13/20', '6/14/20', '6/15/20', '6/16/20',
                            '6/17/20', '6/18/20', '6/19/20', '6/20/20', '6/21/20', '6/22/20', '6/23/20', '6/24/20',
                            '6/25/20', '6/26/20', '6/27/20', '6/28/20', '6/29/20', '6/30/20']:
            c.execute("SELECT *, oid FROM juneExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM juneExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot_label = Label(root, text=tot)
            tot_label.grid(row=1, column=3)
        elif date.get() in ['7/1/20', '7/2/20', '7/3/20', '7/4/20', '7/5/20', '7/6/20', '7/7/20', '7/8/20',
                            '7/9/20', '7/10/20', '7/11/20', '7/12/20', '7/13/20', '7/14/20', '7/15/20', '7/16/20',
                            '7/17/20', '7/18/20', '7/19/20', '7/20/20', '7/21/20', '7/22/20', '7/23/20', '7/24/20',
                            '7/25/20', '7/26/20', '7/27/20', '7/28/20', '7/29/20', '7/30/20', '7/31/20']:
            c.execute("SELECT *, oid FROM julyExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM julyExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot = Label(root, text=tot)
            tot.grid(row=1, column=3)
        elif date.get() in ['8/1/20', '8/2/20', '8/3/20', '8/4/20', '8/5/20', '8/6/20', '8/7/20', '8/8/20',
                            '8/9/20', '8/10/20', '8/11/20', '8/12/20', '8/13/20', '8/14/20', '8/15/20', '8/16/20',
                            '8/17/20', '8/18/20', '8/19/20', '8/20/20', '8/21/20', '8/22/20', '8/23/20', '8/24/20',
                            '8/25/20', '8/26/20', '8/27/20', '8/28/20', '8/29/20', '8/30/20', '8/31/20']:
            c.execute("SELECT *, oid FROM augustExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM augustExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot = Label(root, text=tot)
            tot.grid(row=1, column=3)
        elif date.get() in ['9/1/20', '9/2/20', '9/3/20', '9/4/20', '9/5/20', '9/6/20', '9/7/20', '9/8/20',
                            '9/9/20', '9/10/20', '9/11/20', '9/12/20', '9/13/20', '9/14/20', '9/15/20', '9/16/20',
                            '9/17/20', '9/18/20', '9/19/20', '9/20/20', '9/21/20', '9/22/20', '9/23/20', '9/24/20',
                            '9/25/20', '9/26/20', '9/27/20', '9/28/20', '9/29/20', '9/30/20']:
            c.execute("SELECT *, oid FROM septemberExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM septemberExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot = Label(root, text=tot)
            tot.grid(row=1, column=3)
        elif date.get() in ['10/1/20', '10/2/20', '10/3/20', '10/4/20', '10/5/20', '10/6/20', '10/7/20', '10/8/20',
                            '10/9/20', '10/10/20', '10/11/20', '10/12/20', '10/13/20', '10/14/20', '10/15/20',
                            '10/16/20', '10/17/20', '10/18/20', '10/19/20', '10/20/20', '10/21/20', '10/22/20',
                            '10/23/20', '10/24/20', '10/25/20', '10/26/20', '10/27/20', '10/28/20', '10/29/20',
                            '10/30/20', '10/31/20']:
            c.execute("SELECT *, oid FROM octoberExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM octoberExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot_label = Label(root, text=tot)
            tot_label.grid(row=1, column=3)
        elif date.get() in ['11/1/20', '11/2/20', '11/3/20', '11/4/20', '11/5/20', '11/6/20', '11/7/20', '11/8/20',
                            '11/9/20', '11/10/20', '11/11/20', '11/12/20', '11/13/20', '11/14/20', '11/15/20',
                            '11/16/20', '11/17/20', '11/18/20', '11/19/20', '11/20/20', '11/21/20', '11/22/20',
                            '11/23/20', '11/24/20', '11/25/20', '11/26/20', '11/27/20', '11/28/20', '11/29/20',
                            '11/30/20']:
            c.execute("SELECT *, oid FROM novemberExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM novemberExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot_label = Label(root, text=tot)
            tot_label.grid(row=1, column=3)
        elif date.get() in ['12/1/20', '12/2/20', '12/3/20', '12/4/20', '12/5/20', '12/6/20', '12/7/20', '12/8/20',
                            '12/9/20', '12/10/20', '12/11/20', '12/12/20', '12/13/20', '12/14/20', '12/15/20',
                            '12/16/20', '12/17/20', '12/18/20', '12/19/20', '12/20/20', '12/21/20', '12/22/20',
                            '12/23/20', '12/24/20', '12/25/20', '12/26/20', '12/27/20', '12/28/20', '12/29/20',
                            '12/30/20', '12/31/20']:
            c.execute("SELECT *, oid FROM decemberExpenses")
            records = c.fetchall()
            print_records = ""
            for records in records:
                print_records += str(records) + "\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=7, column=1)
            c.execute("SELECT sum(expense), oid FROM decemberExpenses")
            data = c.fetchall()
            for row in data:
                tot += row[0]
            tot = Label(root, text=tot)
            tot.grid(row=1, column=3)
        else:
            messagebox.showerror("Error", "Error")
        c.execute("SELECT expense, oid FROM januaryExpenses")
        datum = c.fetchall()
        total = 0
        for row in datum:
            total += row[0]
        c.execute("SELECT expense, oid FROM februaryExpenses")
        datum = c.fetchall()
        for row in datum:
            total += row[0]
        c.execute("SELECT expense, oid FROM marchExpenses")
        datum = c.fetchall()
        for row in datum:
            total += row[0]
        c.execute("SELECT expense, oid FROM aprilExpenses")
        datum = c.fetchall()
        for row in datum:
            total += row[0]
        c.execute("SELECT expense, oid FROM mayExpenses")
        datum = c.fetchall()
        for row in datum:
            total += row[0]
        c.execute("SELECT expense, oid FROM juneExpenses")
        datum = c.fetchall()
        for row in datum:
            total += row[0]
        c.execute("SELECT expense, oid FROM julyExpenses")
        datum = c.fetchall()
        for row in datum:
            total += row[0]
        c.execute("SELECT expense, oid FROM augustExpenses")
        datum = c.fetchall()
        for row in datum:
            total += row[0]
        c.execute("SELECT expense, oid FROM septemberExpenses")
        datum = c.fetchall()
        for row in datum:
            total += row[0]
        c.execute("SELECT expense, oid FROM octoberExpenses")
        datum = c.fetchall()
        for row in datum:
            total += row[0]
        c.execute("SELECT expense, oid FROM novemberExpenses")
        datum = c.fetchall()
        for row in datum:
            total += row[0]
        c.execute("SELECT expense, oid FROM decemberExpenses")
        datum = c.fetchall()
        for row in datum:
            total += row[0]
        total = Label(root, text=total)
        total.grid(row=2, column=3)
    except TypeError:
        messagebox.showerror("Error", "No data was found")


def submit():
    conn = sqlite3.connect("Expense.db")
    c = conn.cursor()
    try:
        if int(value.get()) != 0:
            if date.get() in ['1/1/20', '1/2/20', '1/3/20', '1/4/20', '1/5/20', '1/6/20', '1/7/20', '1/8/20',
                            '1/9/20', '1/10/20', '1/11/20', '1/12/20', '1/13/20', '1/14/20', '1/15/20', '1/16/20',
                            '1/17/20', '1/18/20', '1/19/20', '1/20/20', '1/21/20', '1/22/20', '1/23/20', '1/24/20',
                            '1/25/20', '1/26/20', '1/27/20', '1/28/20', '1/29/20', '1/30/20', '1/31/20']:
                c.execute("INSERT INTO januaryExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
            elif date.get() in ['2/1/20', '2/2/20', '2/3/20', '2/4/20', '2/5/20', '2/6/20', '2/7/20', '2/8/20',
                            '2/9/20', '2/10/20', '2/11/20', '2/12/20', '2/13/20', '2/14/20', '2/15/20', '2/16/20',
                            '2/17/20', '2/18/20', '2/19/20', '2/20/20', '2/21/20', '2/22/20', '2/23/20', '2/24/20',
                            '2/25/20', '2/26/20', '2/27/20', '2/28/20', '2/29/20']:
                c.execute("INSERT INTO februaryExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
            elif date.get() in ['3/1/20', '3/2/20', '3/3/20', '3/4/20', '3/5/20', '3/6/20', '3/7/20', '3/8/20',
                            '3/9/20', '3/10/20', '3/11/20', '3/12/20', '3/13/20', '3/14/20', '3/15/20', '3/16/20',
                            '3/17/20', '3/18/20', '3/19/20', '3/20/20', '3/21/20', '3/22/20', '3/23/20', '3/24/20',
                            '3/25/20', '3/26/20', '3/27/20', '3/28/20', '3/29/20', '3/30/20', '3/31/20']:
                c.execute("INSERT INTO marchExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
            elif date.get() in ['4/1/20', '4/2/20', '4/3/20', '4/4/20', '4/5/20', '4/6/20', '4/7/20', '4/8/20',
                            '4/9/20', '4/10/20', '4/11/20', '4/12/20', '4/13/20', '4/14/20', '4/15/20', '4/16/20',
                            '4/17/20', '4/18/20', '4/19/20', '4/20/20', '4/21/20', '4/22/20', '4/23/20', '4/24/20',
                            '4/25/20', '4/26/20', '4/27/20', '4/28/20', '4/29/20', '4/30/20']:
                c.execute("INSERT INTO aprilExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
            elif date.get() in ['5/1/20', '5/2/20', '5/3/20', '5/4/20', '5/5/20', '5/6/20', '5/7/20', '5/8/20',
                            '5/9/20', '5/10/20', '5/11/20', '5/12/20', '5/13/20', '5/14/20', '5/15/20', '5/16/20',
                            '5/17/20', '5/18/20', '5/19/20', '5/20/20', '5/21/20', '5/22/20', '5/23/20', '5/24/20',
                            '5/25/20', '5/26/20', '5/27/20', '5/28/20', '5/29/20', '5/30/20', '5/31/20']:
                c.execute("INSERT INTO mayExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
            elif date.get() in ['6/1/20', '6/2/20', '6/3/20', '6/4/20', '6/5/20', '6/6/20', '6/7/20', '6/8/20',
                            '6/9/20', '6/10/20', '6/11/20', '6/12/20', '6/13/20', '6/14/20', '6/15/20', '6/16/20',
                            '6/17/20', '6/18/20', '6/19/20', '6/20/20', '6/21/20', '6/22/20', '6/23/20', '6/24/20',
                            '6/25/20', '6/26/20', '6/27/20', '6/28/20', '6/29/20', '6/30/20']:
                c.execute("INSERT INTO juneExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
            elif date.get() in ['7/1/20', '7/2/20', '7/3/20', '7/4/20', '7/5/20', '7/6/20', '7/7/20', '7/8/20',
                            '7/9/20', '7/10/20', '7/11/20', '7/12/20', '7/13/20', '7/14/20', '7/15/20', '7/16/20',
                            '7/17/20', '7/18/20', '7/19/20', '7/20/20', '7/21/20', '7/22/20', '7/23/20', '7/24/20',
                            '7/25/20', '7/26/20', '7/27/20', '7/28/20', '7/29/20', '7/30/20', '7/31/20']:
                c.execute("INSERT INTO julyExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
            elif date.get() in ['8/1/20', '8/2/20', '8/3/20', '8/4/20', '8/5/20', '8/6/20', '8/7/20', '8/8/20',
                            '8/9/20', '8/10/20', '8/11/20', '8/12/20', '8/13/20', '8/14/20', '8/15/20', '8/16/20',
                            '8/17/20', '8/18/20', '8/19/20', '8/20/20', '8/21/20', '8/22/20', '8/23/20', '8/24/20',
                            '8/25/20', '8/26/20', '8/27/20', '8/28/20', '8/29/20', '8/30/20', '8/31/20']:
                c.execute("INSERT INTO augustExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
            elif date.get() in ['9/1/20', '9/2/20', '9/3/20', '9/4/20', '9/5/20', '9/6/20', '9/7/20', '9/8/20',
                            '9/9/20', '9/10/20', '9/11/20', '9/12/20', '9/13/20', '9/14/20', '9/15/20', '9/16/20',
                            '9/17/20', '9/18/20', '9/19/20', '9/20/20', '9/21/20', '9/22/20', '9/23/20', '9/24/20',
                            '9/25/20', '9/26/20', '9/27/20', '9/28/20', '9/29/20', '9/30/20']:
                c.execute("INSERT INTO septemberExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
            elif date.get() in ['10/1/20', '10/2/20', '10/3/20', '10/4/20', '10/5/20', '10/6/20', '10/7/20', '10/8/20',
                            '10/9/20', '10/10/20', '10/11/20', '10/12/20', '10/13/20', '10/14/20', '10/15/20',
                            '10/16/20', '10/17/20', '10/18/20', '10/19/20', '10/20/20', '10/21/20', '10/22/20',
                            '10/23/20', '10/24/20', '10/25/20', '10/26/20', '10/27/20', '10/28/20', '10/29/20',
                            '10/30/20', '10/31/20']:
                c.execute("INSERT INTO octoberExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
            elif date.get() in ['11/1/20', '11/2/20', '11/3/20', '11/4/20', '11/5/20', '11/6/20', '11/7/20', '11/8/20',
                            '11/9/20', '11/10/20', '11/11/20', '11/12/20', '11/13/20', '11/14/20', '11/15/20',
                            '11/16/20', '11/17/20', '11/18/20', '11/19/20', '11/20/20', '11/21/20', '11/22/20',
                            '11/23/20', '11/24/20', '11/25/20', '11/26/20', '11/27/20', '11/28/20', '11/29/20',
                            '11/30/20']:
                c.execute("INSERT INTO novemberExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
            elif date.get() in ['12/1/20', '12/2/20', '12/3/20', '12/4/20', '12/5/20', '12/6/20', '12/7/20', '12/8/20',
                            '12/9/20', '12/10/20', '12/11/20', '12/12/20', '12/13/20', '12/14/20', '12/15/20',
                            '12/16/20', '12/17/20', '12/18/20', '12/19/20', '12/20/20', '12/21/20', '12/22/20',
                            '12/23/20', '12/24/20', '12/25/20', '12/26/20', '12/27/20', '12/28/20', '12/29/20',
                            '12/30/20', '12/31/20']:
                c.execute("INSERT INTO decemberExpenses VALUES(:date, :name, :value)",
                            {
                                  "date": date.get(),
                                  "name": name.get(),
                                  "value": value.get()
                            })
        else:
            messagebox.showerror("Error", "Value cannot be 0")
    except ValueError:
        messagebox.showerror("Error", "Value cannot be letter and empty")
    conn.commit()
    conn.close()
    name.delete(0, END)
    value.delete(0, END)


date = DateEntry(root, width=10, height=5, background="blue", foreground="white")
date.grid(row=0, column=0, columnspan=1)
name = Entry(root, width="30")
name.grid(row=1, column=1, padx=20)
value = Entry(root, width="30")
value.grid(row=2, column=1, padx=20)
box_delete = Entry(root, width="30")
box_delete.grid(row=4, column=1, padx=20)

name_label = Label(root, text="Name")
name_label.grid(row=1, column=0)
value_label = Label(root, text="Value")
value_label.grid(row=2, column=0)
results_label = Label(root, text="Results")
results_label.grid(row=6, column=0)
box_delete_label = Label(root, text="ID Number")
box_delete_label.grid(row=4, column=0)
query_label = Label(root, text="")
query_label.grid(row=7, column=1)
total_label = Label(root, text="Monthly Expense")
total_label.grid(row=1, column=2)
yearlytotal_label = Label(root, text="Yearly Expense")
yearlytotal_label.grid(row=2, column=2)
tot_label = Label(root, text="")
tot_label.grid(row=1, column=3)

add_btn1 = Button(root, text="Add Record", command=submit)
add_btn1.grid(row=3, column=0, columnspan=1, pady=10, padx=10)
show_btn2 = Button(root, text="Show Records", command=query)
show_btn2.grid(row=3, column=1, columnspan=1, pady=10, padx=10)
create_database_btn3 = Button(root, text="Create DataBase", command=create_database)
create_database_btn3.grid(row=3, column=2, columnspan=1, pady=10, padx=10)
delete_btn4 = Button(root, text="Delete", command=delete)
delete_btn4.grid(row=5, column=0, pady=10, padx=10)
reset_btn5 = Button(root, text="Reset", command=reset)
reset_btn5.grid(row=5, column=1, pady=10, padx=10)

root.mainloop()
