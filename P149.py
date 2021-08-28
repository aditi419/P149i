from tkinter import *
import random

root = Tk()
root.title('Random Word Generator')
root.geometry('400x400')

randomWord = Label(root)
randomWord.place(relx = 0.5,rely = 0.4,anchor = CENTER)

def randomNum():
    alpha_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    random_no1 = random.randint(1,26)
    random_no2 = random.randint(1,26) 
    random_no3 = random.randint(1,26)
    random_no4 = random.randint(1,26)
    random_no5 = random.randint(1,26)
    
    random_alpha1 = alpha_list[random_no1]
    random_alpha2 = alpha_list[random_no2]
    random_alpha3 = alpha_list[random_no3]
    random_alpha4 = alpha_list[random_no4]
    random_alpha5 = alpha_list[random_no5]
    
    alpha_list[random_no2,random_no3,random_no4,random_no5]
    
    randomWord['text'] = random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5
    
    btn = Button(root,text = 'Get Random Word',command = randomNum)
    btn.place(relx = 0.5,rely = 0.5,anchor = CENTER)
    
mainloop()
