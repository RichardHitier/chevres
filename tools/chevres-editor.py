import csv
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

all_csv_rows = []
with open('/home/richard/public_html/chevres/datas/chevres_vincent_geocoded.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        all_csv_rows.append(row)

def save_csv():
    with open('/home/richard/public_html/chevres/sauve.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile,  delimiter=';')
        csv_writer.writerows( all_csv_rows)

photo_index = 0


def previous_photo(*args):
    global photo_index
    all_csv_rows[photo_index] = form2row()
    photo_index = photo_index - 1
    my_row = all_csv_rows[photo_index]
    row2form(my_row)


def next_photo(*args):
    global photo_index
    all_csv_rows[photo_index] = form2row()
    photo_index = photo_index + 1
    my_row = all_csv_rows[photo_index]
    row2form(my_row)


def form2row():
    my_row=[None]*9
    my_row[0]=imgpath.get()
    my_row[1]=name.get()
    my_row[5]=weight.get()
    my_row[6]=fat.get()
    my_row[2]=farm.get()
    my_row[3]=postal.get()
    my_row[4]=town.get()
    my_row[7]=lat.get()
    my_row[8]=lng.get()
    return( my_row)

def row2form(my_row):
    imgpath.set(my_row[0])
    name.set(my_row[1])
    weight.set(my_row[5])
    fat.set(my_row[6])
    farm.set(my_row[2])
    postal.set(my_row[3])
    town.set(my_row[4])
    lat.set(my_row[7])
    lng.set(my_row[8])
    my_image = ImageTk.PhotoImage(file="/home/richard/public_html/chevres/datas/{}".format(imgpath.get()))
    # image = ImageTk.PhotoImage(Image.open("/usr/share/tcltk/tk8.6/images/pwrdLogo100.gif"))
    # image = PhotoImage(file=)
    # imglabel['image'] = my_image
    # imglabel.set
    # imglabel.pack()
    imglabel.configure(image=my_image)
    imglabel.image = my_image

    print(type(image))


root = Tk()
root.title("Hollo")

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

image = ImageTk.PhotoImage(Image.open("/usr/share/tcltk/tk8.6/images/pwrdLogo100.gif"))
imglabel = ttk.Label(mainframe, image=image)
imglabel.grid(column=1, row=2, rowspan=8, sticky=E)

ttk.Label(mainframe, text="Img Path").grid(column=2, row=1, sticky=W)
imgpath = StringVar()
ttk.Label(mainframe, textvariable=imgpath).grid(column=3, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Nom").grid(column=2, row=2, sticky=W)
name = StringVar()
name_entry = ttk.Entry(mainframe, width=32, textvariable=name)
name_entry.grid(column=3, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Poids").grid(column=2, row=3, sticky=W)
weight = StringVar()
weight_entry = ttk.Entry(mainframe, width=32, textvariable=weight)
weight_entry.grid(column=3, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Mat. G.").grid(column=2, row=4, sticky=W)
fat = StringVar()
fat_entry = ttk.Entry(mainframe, width=32, textvariable=fat)
fat_entry.grid(column=3, row=4, sticky=(W, E))

ttk.Label(mainframe, text="Ferme").grid(column=2, row=5, sticky=W)
farm = StringVar()
farm_entry = ttk.Entry(mainframe, width=32, textvariable=farm)
farm_entry.grid(column=3, row=5, sticky=(W, E))

ttk.Label(mainframe, text="Code Postal").grid(column=2, row=6, sticky=W)
postal = StringVar()
postal_entry = ttk.Entry(mainframe, width=32, textvariable=postal)
postal_entry.grid(column=3, row=6, sticky=(W, E))

ttk.Label(mainframe, text="Ville").grid(column=2, row=7, sticky=W)
town = StringVar()
town_entry = ttk.Entry(mainframe, width=32, textvariable=town)
town_entry.grid(column=3, row=7, sticky=(W, E))

ttk.Label(mainframe, text="Lat").grid(column=2, row=8, sticky=W)
lat = StringVar()
lat_entry = ttk.Entry(mainframe, width=32, textvariable=lat)
lat_entry.grid(column=3, row=8, sticky=(W, E))

ttk.Label(mainframe, text="Lng").grid(column=2, row=9, sticky=W)
lng = StringVar()
lng_entry = ttk.Entry(mainframe, width=32, textvariable=lng)
lng_entry.grid(column=3, row=9, sticky=(W, E))

ttk.Button(mainframe, text="Prev", command=previous_photo).grid(column=2, row=10, sticky=E)
ttk.Button(mainframe, text="Next", command=next_photo).grid(column=3, row=10, sticky=E)
ttk.Button(mainframe, text="Save", command=save_csv).grid(column=3, row=11, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

name_entry.focus()
root.bind("<Return>", next_photo)


root.mainloop()
