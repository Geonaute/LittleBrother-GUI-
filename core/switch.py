from tkinter import *
from tkinter import messagebox
from core import searchPersonne, searchInstagram,searchUserName,employee_lookup,searchAdresse,ipFinder,searchNumber
from core import settings,google


# setting switch function:
def switch(navself, topFrame, btnState):
    # create animated Navbar closing:
    if btnState is True:
        for x in range(301):
            navself.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        topFrame.config(bg="#252726")

        # turning button OFF:
        btnState = False
    else:
        # make self dim:
        topFrame.config(bg="#252726")

        # created animated Navbar opening:
        for x in range(-300, 0):
            navself.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# to show profile if exist
def seeProfle(profile, navself):
    profile.destroy()
    return messagebox.showinfo("info ","seeprofile")

# to show all existing profile in database
def allprofile(profile, navself):
    profile.destroy()
    return messagebox.showinfo("info","allprofile")


# to create a profile
def createprofile(profile, navself, topFrame):
    switch(navself, topFrame, btnState=True)
    profile.destroy()
    navself = Toplevel(navself)
    navself.title("Create Profile")
    navself.minsize(713, 398)
    navself.maxsize(713, 398)
    navself.config(bg="grey17")
    Label(navself, text="Profile Name:", bg="grey17", fg="red", font=("comicsansms", 15, "bold"), relief=FLAT).place(x=5, y=20)
    Label(navself, text="(Format: First name Last name)", bg="grey17", fg="red", font=("comicsansms", 15, "bold"), relief=FLAT).place(x=150 ,y=130)
    name = Entry(navself)
    name.place(x=150 ,y=60) # profile name
    name = name.get()
    Button(navself, text="submit").place(x=50, y=100)

    # p1 = Entry(navself)
    # p1.place(x=150, y=20)
    # Label(navself, text="(Format: First name Last name)", bg="grey17", fg="red", font=("comicsansms", 10, "bold"),
    #       relief=FLAT).place(x=100, y=50)

    navself.mainloop()

# to decrypte hash
def hashdecrypter(more_tools, navself):
    more_tools.destroy()
    return messagebox.showinfo("info","hash")

def Person_lookup(self, text, navself, topFrame):
    switch(navself, topFrame, btnState=True)
    # lookup.destroy()
    person_lookup = Toplevel(self)
    person_lookup.title("Person Lookup")
    person_lookup.config(bg="grey17")
    person_lookup.geometry("600x300+200+200")
    person_lookup.maxsize(600,300)
    person_lookup.minsize(600,300)
    l = Label(person_lookup, text="Name:", bg="black", fg="Grey",
              font=("comicsansms", 16, "bold"),relief=FLAT).place(x=60,y=60)
    l = Label(person_lookup, text="City/Department:", bg="black", fg="Grey",
              font=("comicsansms", 16, "bold"),relief=FLAT).place(x=60, y=160)
    l = Label(person_lookup, text="Last name first name.", bg="black", fg="red",
              font=("comicsansms", 16, "bold"),relief=FLAT).place(x=300, y=100)
    nom = Entry(person_lookup, relief=FLAT,  font=("comicsansms", 20, "bold"))
    nom.place(x=290,y=60)
    city = Entry(person_lookup, relief=FLAT,  font=("comicsansms", 20, "bold"))
    city.place(x=290,y=160)
    btn = Button(person_lookup, text="Search", font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=lambda: searchPersonne.searchPersonne(self,text,person_lookup,nom.get(),city.get(),settings.countrycode)).place(x=120, y=260)
    person_lookup.mainloop()


def Mail_tracer(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "Mail_tracer")


def Username_lookup(self, text, navself, topFrame):
    switch(navself, topFrame, btnState=True)
    # lookup.destroy()
    username_lookup = Toplevel(self)
    username_lookup.title("Username Lookup")
    username_lookup.config(bg="grey17")
    username_lookup.geometry("600x300+200+200")
    username_lookup.maxsize(600, 300)
    username_lookup.minsize(600, 300)
    l = Label(username_lookup, text="Psudo:", bg="black", fg="Grey",
              font=("comicsansms", 16, "bold"), relief=FLAT).place(x=60, y=60)
    psudo = Entry(username_lookup, relief=FLAT, font=("comicsansms", 20, "bold"))
    psudo.place(x=290, y=60)
    btn = Button(username_lookup, text="Search", font="BahnschriftLight 15", bg="gray17", fg="white",
                 activebackground="gray17", activeforeground="green", bd=0,
                 command=lambda: searchUserName.searchUserName(self, text, username_lookup, psudo.get())).place(x=120, y=160)
    username_lookup.mainloop()


def Employees_search(self,text, navself, topFrame):
    switch(navself, topFrame, btnState=True)
    # lookup.destroy()
    Employees_search = Toplevel(self)
    Employees_search.title("Employees Lookup")
    Employees_search.config(bg="grey17")
    Employees_search.geometry("600x300+200+200")
    Employees_search.maxsize(600, 300)
    Employees_search.minsize(600, 300)
    l1 = Label(Employees_search, text="Bussiness:", bg="black", fg="Grey",
              font=("comicsansms", 16, "bold"), relief=FLAT).place(x=60, y=60)
    l2 = Label(Employees_search, text="City:", bg="black", fg="Grey",
              font=("comicsansms", 16, "bold"), relief=FLAT).place(x=60, y=160)
    bus = Entry(Employees_search, relief=FLAT, font=("comicsansms", 20, "bold"))
    bus.place(x=290, y=60)
    cit = Entry(Employees_search, relief=FLAT, font=("comicsansms", 20, "bold"))
    cit.place(x=290, y=160)
    btn = Button(Employees_search, text="Search", font="BahnschriftLight 15", bg="gray17", fg="white",
                 activebackground="gray17", activeforeground="green", bd=0,
                 command=lambda: employee_lookup.employee_lookup(self, text, Employees_search, bus, cit)).place(x=120, y=260)
    Employees_search.mainloop()


def Lookup_address(self, text, navself, topFrame):
    switch(navself, topFrame, btnState=True)
    # lookup.destroy()
    Lookup_addr = Toplevel(self)
    Lookup_addr.title("Address Lookup")
    Lookup_addr.config(bg="grey17")
    Lookup_addr.geometry("600x300+200+200")
    Lookup_addr.maxsize(600, 300)
    Lookup_addr.minsize(600, 300)
    l1 = Label(Lookup_addr, text="Address:", bg="black", fg="Grey",
               font=("comicsansms", 16, "bold"), relief=FLAT).place(x=60, y=60)
    addr = Entry(Lookup_addr, relief=FLAT, font=("comicsansms", 20, "bold"))
    addr.place(x=290, y=60)
    btn = Button(Lookup_addr, text="Search", font="BahnschriftLight 15", bg="gray17", fg="white",
                 activebackground="gray17", activeforeground="green", bd=0,
                 command=lambda: searchAdresse.searchAdresse(self, text, Lookup_addr,addr.get() ,settings.countrycode)).place(x=120,
                                                                                                                y=260)
    Lookup_addr.mainloop()


def Google_search(self, text, navself, topFrame):
    switch(navself, topFrame, btnState=True)
    # lookup.destroy()
    googl = Toplevel(self)
    googl.title("Google Lookup")
    googl.config(bg="grey17")
    googl.geometry("600x300+200+200")
    googl.maxsize(600, 300)
    googl.minsize(600, 300)
    l1 = Label(googl, text="Enter First Name, Last Name, City, Department, Sport, School...",
               bg="black", fg="Grey",font=("comicsansms", 16, "bold"), relief=FLAT).place(x=20, y=160)
    l1 = Label(googl, text="Research:", bg="black", fg="Grey",
               font=("comicsansms", 16, "bold"), relief=FLAT).place(x=60, y=60)
    search = Entry(googl, relief=FLAT, font=("comicsansms", 20, "bold"))
    search.place(x=290, y=60)
    btn = Button(googl, text="Search", font="BahnschriftLight 15", bg="gray17", fg="white",
                 activebackground="gray17", activeforeground="green", bd=0,
                 command=lambda: google.google(self, text, googl, search.get())).place(x=120,
                                                                                          y=260)
    googl.mainloop()


def Phone_lookup(self,text, navself, topFrame):
    switch(navself, topFrame, btnState=True)
    # lookup.destroy()
    phone_look = Toplevel(self)
    phone_look.title("Address Lookup")
    phone_look.config(bg="grey17")
    phone_look.geometry("600x300+200+200")
    phone_look.maxsize(600, 300)
    phone_look.minsize(600, 300)
    l1 = Label(phone_look, text="PHONE NUMBER:", bg="black", fg="Grey",
               font=("comicsansms", 16, "bold"), relief=FLAT).place(x=60, y=60)
    phno = Entry(phone_look, relief=FLAT, font=("comicsansms", 20, "bold"))
    phno.place(x=290, y=60)
    btn = Button(phone_look, text="Search", font="BahnschriftLight 15", bg="gray17", fg="white",
                 activebackground="gray17", activeforeground="green", bd=0,
                 command=lambda: searchNumber.searchNumber(self, text, phone_look, phno.get())).place(x=120,y=260)
    phone_look.mainloop()


def Facebook_GraphSearch(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "Facebook_GraphSearch")


def IP_lookup(self, text, navself, topFrame):
    switch(navself, topFrame, btnState=True)
    # lookup.destroy()
    Lookup_ipaddr = Toplevel(self)
    Lookup_ipaddr.title("IP-Address Lookup")
    Lookup_ipaddr.config(bg="grey17")
    Lookup_ipaddr.geometry("600x300+200+200")
    Lookup_ipaddr.maxsize(600, 300)
    Lookup_ipaddr.minsize(600, 300)
    l1 = Label(Lookup_ipaddr, text="IPAddress:", bg="black", fg="Grey",
               font=("comicsansms", 16, "bold"), relief=FLAT).place(x=60, y=60)
    ipaddr = Entry(Lookup_ipaddr, relief=FLAT, font=("comicsansms", 20, "bold"))
    ipaddr.place(x=290, y=60)
    btn = Button(Lookup_ipaddr, text="Search", font="BahnschriftLight 15", bg="gray17", fg="white",
                 activebackground="gray17", activeforeground="green", bd=0,
                 command=lambda: ipFinder.ipFinder(self, text, Lookup_ipaddr, ipaddr.get())).place(x=120,
                                                                                          y=260)
    Lookup_ipaddr.mainloop()


def twitter_info(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "twitter_info")


def SSID_locator(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "SSID_locator")


def instagram_info(self,text, navself, topFrame):
    switch(navself, topFrame, btnState=True)
    # lookup.destroy()
    instagram_info = Toplevel(self)
    instagram_info.title("Instagram Lookup")
    instagram_info.config(bg="grey17")
    instagram_info.geometry("700x350+200+200")
    instagram_info.maxsize(600, 300)
    instagram_info.minsize(600, 300)
    l = Label(instagram_info, text="USERNAME:", bg="black", fg="Grey",
              font=("comicsansms", 16, "bold"), relief=FLAT).place(x=60, y=60)
    instaprofile = Entry(instagram_info, relief=FLAT, font=("comicsansms", 20, "bold"))
    instaprofile.place(x=290, y=60)
    btn = Button(instagram_info, text="Search", font="BahnschriftLight 15", bg="gray17", fg="white",
                 activebackground="gray17", activeforeground="green", bd=0,
                 command=lambda: searchInstagram.searchInstagram(self,instagram_info,instaprofile.get(),text)).place(x=120, y=200)
    instagram_info.mainloop()

def Email_lookup(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info","Email_lookup")

def FR(options, navself):
    options.destroy()
    return messagebox.showinfo("info","FR")

def LU(options, navself):
    options.destroy()
    return messagebox.showinfo("info","LU")

def BE(options, navself):
    options.destroy()
    return messagebox.showinfo("info","BE")

def All(options, navself):
    options.destroy()
    return messagebox.showinfo("info","ALL")

def CH(options, navself):
    options.destroy()
    return messagebox.showinfo("info","CH")

