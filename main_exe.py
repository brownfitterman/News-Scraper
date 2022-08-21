from tkinter import *
from news_scrape import main
window = Tk()
wiki_url=Variable()
City=Variable()
Tag=Variable()
window.title("News Scrapper")
window.geometry('350x200')
lbl = Label(window, text="Put wikipedia url", font=("Arial Bold", 10))
lbl.grid(column=0, row=1, padx=10,pady=10)
lb2 = Label(window, text="City name", font=("Arial Bold", 10))
lb2.grid(column=0, row=2, padx=10,pady=10)
lb3 = Label(window, text="Tag", font=("Arial Bold", 10))
lb3.grid(column=0, row=3, padx=10,pady=10)
entry1=Entry(window, textvariable=wiki_url).grid(column=1, row=1, padx=10,pady=10)
entry2=Entry(window, textvariable=City).grid(column=1, row=2, padx=10,pady=10)
entry3=Entry(window, textvariable=Tag).grid(column=1, row=3, padx=10,pady=10)
btn = Button(window, text="Start Scrapping", command=lambda:main(wiki_url.get(),City.get(),Tag.get()))
btn.grid(column=1, row=4)











window.mainloop()