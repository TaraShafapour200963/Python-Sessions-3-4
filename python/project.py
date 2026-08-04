import tkinter as tk
from tkinter import messagebox


# ثبت مخاطب
def add_contact():
    name = name_entry.get()
    family = family_entry.get()
    phone = phone_entry.get()

    if name == "" or family == "" or phone == "":
        messagebox.showwarning("خطا", "همه قسمت‌ها را پر کنید")
    else:
        with open("contacts.txt", "a", encoding="utf-8") as file:
            file.write(name + "," + family + "," + phone + "\n")

        messagebox.showinfo("موفق", "مخاطب ثبت شد")

        name_entry.delete(0, tk.END)
        family_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)

        show_contacts()


# نمایش مخاطبین
def show_contacts():
    listbox.delete(0, tk.END)

    try:
        with open("contacts.txt", "r", encoding="utf-8") as file:

            for line in file:
                data = line.strip().split(",")

                name = data[0]
                family = data[1]
                phone = data[2]

                listbox.insert(
                    tk.END,
                    name + " " + family + " - " + phone
                )

    except:
        pass

    count_label.config(
        text="تعداد مخاطبین: " + str(listbox.size())
    )


# جستجوی مخاطب
def search_contact():
    search = search_entry.get()

    listbox.delete(0, tk.END)

    try:
        with open("contacts.txt", "r", encoding="utf-8") as file:

            for line in file:
                data = line.strip().split(",")

                name = data[0]
                family = data[1]
                phone = data[2]

                if search in name or search in family or search in phone:
                    listbox.insert(
                        tk.END,
                        name + " " + family + " - " + phone
                    )

    except:
        pass

    count_label.config(
        text="تعداد مخاطبین: " + str(listbox.size())
    )


# حذف مخاطب
def delete_contact():
    selected = listbox.curselection()

    if selected == ():
        messagebox.showwarning(
            "خطا",
            "یک مخاطب را انتخاب کنید"
        )
        return

    number = selected[0]

    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    del lines[number]

    with open("contacts.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)

    messagebox.showinfo("موفق", "مخاطب حذف شد")

    show_contacts()


# ---------------- پنجره برنامه ----------------

window = tk.Tk()
window.title("دفترچه مدیریت مخاطبین")
window.geometry("500x700")
window.resizable(False, False)


# عنوان
tk.Label(window,text="دفترچه مدیریت مخاطبین",font=("Arial", 18, "bold")).pack(pady=15)

# نام
tk.Label(window,text="نام").pack()
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

# نام خانوادگی
tk.Label(window,text="نام خانوادگی").pack()
family_entry = tk.Entry(window)
family_entry.pack(pady=5)

# شماره تلفن
tk.Label(window,text="شماره تلفن").pack()
phone_entry = tk.Entry(window)
phone_entry.pack(pady=5)

# ثبت مخاطب
tk.Button(window,text="ثبت مخاطب",command=add_contact).pack(pady=10)

# نمایش مخاطبین
tk.Button(window,text="نمایش مخاطبین",command=show_contacts).pack(pady=5)

# جستجو
tk.Label(window,text="جستجو").pack(pady=(15, 5))
search_entry = tk.Entry(window)
search_entry.pack()
tk.Button(window,text="جستجو",command=search_contact).pack(pady=5)

# لیست مخاطبین
listbox = tk.Listbox(window,width=45,height=10)
listbox.pack(pady=10)


# حذف
tk.Button(window,text="حذف مخاطب",command=delete_contact).pack(pady=5)

# تعداد مخاطبین
count_label = tk.Label(window,text="تعداد مخاطبین: 0")
count_label.pack(pady=10)

# خروج
tk.Button(window,text="خروج",command=window.destroy).pack()

# نمایش اولیه
show_contacts()
window.mainloop()