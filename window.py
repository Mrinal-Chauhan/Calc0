from tkinter import *
import time


window = Tk()
window.title('Calc0')
window.geometry("400x367")
window.configure(bg="#242530")
canvas = Canvas(
    window,
    bg="#242530",
    height=367,
    width=400,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file="imgs/background.png")
background = canvas.create_image(
    200.0, 183.5,
    image=background_img)

#Textbox
textbox = Label(
    window, 
    #text= 'ww',
    fg= '#FFFFFF',
    font=('Inter',22),
    background='#3A3F77', 
    height= 1, width= 17, anchor="e"
    )
textbox.pack()
textbox.place(x = 40, y = 41)




#Some Functions:
output = ''
equation = ''
counter_backspace = 0

def press(button):
    global output
    global equation
    global counter_backspace

    equation += str(button)

    if button == '/':
        output += '÷'
    elif button == '*':
        output += 'x'
    elif button == '**':
        output += '^'
    else:
        output += str(button)
        
    textbox.config(text=output)
    counter_backspace = 0

def backspace():
    global output
    global equation
    global counter_backspace

    if counter_backspace == 1:
        output,equation = '',''
        textbox.config(text=output)
        counter_backspace = 0
    else:
        output_backspace = output[:len(output)-1]
        output = output_backspace
        equation_backspace = equation[:len(equation)-1]
        equation=equation_backspace
        textbox.config(text=output)

def percentage():
    global equation
    global output
    equation += '/100'
    output += '%'
    textbox.config(text=output)

def equals_to():
    global equation
    global output
    global counter_backspace

    nums = ['1','2','3','4','5','6','7','8','9','0','.']
    try:
        if ('%' in output) == True:
            div = output.split('%')
            for i in range(len(div)):
                if i != 0:
                    if (div[i] in nums) == True:
                        result = 'Malformed Expression'
                        equation,output = '',''
                        textbox.config(text=result)
                        break
            
        result = str(eval(equation))
        equation,output = result,result

        if result == '13':
            text_animation(13)
            return()
        elif result == '2346':
            text_animation(2346)
            return()

        if len(result) > 17:
            if ('.' in str(result)) == False:
                result = result[0]+'.'+result[1:13]+'E'+str(len(result)-1)
                textbox.config(text=result)
                equation,output = result,result
                
            else:
                result = result[:17]
                textbox.config(text=result)
                equation,output = result,result
                

        if ('.' in result) == True:
            div2 = result.split('.')
            for i in div2[1]:
                if i != '0':
                    break
            else:
                result = int(float(result))
                equation,output = result,result
                

        textbox.config(text=result)
        counter_backspace = 1

    except ZeroDivisionError:
        result = 'Zero Division Error'
        equation,output = '',''
        textbox.config(text=result)
        counter_backspace = 1
    except SyntaxError:
        result = 'Malformed Expression'
        equation,output = '',''
        textbox.config(text=result)
        counter_backspace = 1



def text_animation(num):

    if num == 13:
        arg = 'Mrinal'
    elif num == 2346:
        arg = 'Shy ♡ True'

    global textbox
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','♡']
    string = arg.upper()
    length=len(string)
    var2_ta=0
    var1_ta=''

    textbox.config(text=num)
    window.update()
    time.sleep(1)

    for i in range (length):
        for x in alphabet:
            if string[var2_ta] == ' ':
                var1_ta += ' '
                textbox.config(text=var1_ta)
                window.update()
                time.sleep(0.1)
                break

            elif x != string[var2_ta]:
                c = var1_ta+x
                textbox.config(text=c)
                window.update()
                time.sleep(0.1)
                
            else:
                var1_ta += x
                textbox.config(text=var1_ta)
                window.update()
                time.sleep(0.1)
                break
        var2_ta+=1
    textbox.config(text=var1_ta)
    window.update()





img0 = PhotoImage(file="imgs/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=equals_to,
    relief="flat")

b0.place(
    x=258.0, y=289.0,
    width=126,
    height=63)

img1 = PhotoImage(file="imgs/img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press('/'),
    relief="flat")

b1.place(
    x=326.0, y=117.0,
    width=55,
    height=50)

img2 = PhotoImage(file="imgs/img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press('*'),
    relief="flat")

b2.place(
    x=269.0, y=106.0,
    width=55,
    height=61)

img3 = PhotoImage(file="imgs/img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command= lambda: press('+'),
    relief="flat")

b3.place(
    x=268.0, y=173.0,
    width=55,
    height=50)

img4 = PhotoImage(file="imgs/img4.png")
b4 = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press('-'),
    relief="flat")

b4.place(
    x=325.0, y=173.0,
    width=55,
    height=55)

img5 = PhotoImage(file="imgs/img5.png")
b5 = Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press('**'),
    relief="flat")

b5.place(
    x=326.0, y=237.0,
    width=55,
    height=50)

img6 = PhotoImage(file="imgs/img6.png")
b6 = Button(
    image=img6,
    borderwidth=0,
    highlightthickness=0,
    command=percentage,
    relief="flat")

b6.place(
    x=268.0, y=237.0,
    width=55,
    height=50)

img7 = PhotoImage(file="imgs/img7.png")
b7 = Button(
    image=img7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press(9),
    relief="flat")

b7.place(
    x=179.0, y=234.0,
    width=79,
    height=52)

img8 = PhotoImage(file="imgs/img8.png")
b8 = Button(
    image=img8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press(0),
    relief="flat")

b8.place(
    x=100.0, y=295.0,
    width=79,
    height=52)

img9 = PhotoImage(file="imgs/img9.png")
b9 = Button(
    image=img9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press(7),
    relief="flat")

b9.place(
    x=21.0, y=234.0,
    width=79,
    height=52)

img10 = PhotoImage(file="imgs/img10.png")
b10 = Button(
    image=img10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press(6),
    relief="flat")

b10.place(
    x=179.0, y=177.0,
    width=79,
    height=52)

img11 = PhotoImage(file="imgs/img11.png")
b11 = Button(
    image=img11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press(4),
    relief="flat")

b11.place(
    x=17.0, y=177.0,
    width=79,
    height=52)

img12 = PhotoImage(file="imgs/img12.png")
b12 = Button(
    image=img12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press(5),
    relief="flat")

b12.place(
    x=100.0, y=177.0,
    width=79,
    height=52)

img13 = PhotoImage(file="imgs/img13.png")
b13 = Button(
    image=img13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press('.'),
    relief="flat")

b13.place(
    x=21.0, y=294.0,
    width=79,
    height=52)

img14 = PhotoImage(file="imgs/img14.png")
b14 = Button(
    image=img14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press(8),
    relief="flat")

b14.place(
    x=98.0, y=237.0,
    width=79,
    height=52)

img15 = PhotoImage(file="imgs/img15.png")
b15 = Button(
    image=img15,
    borderwidth=0,
    highlightthickness=0,
    command=backspace,
    relief="flat")

b15.place(
    x=179.0, y=297.0,
    width=79,
    height=52)

img16 = PhotoImage(file="imgs/img16.png")
b16 = Button(
    image=img16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press(3),
    relief="flat")

b16.place(
    x=178.0, y=115.0,
    width=79,
    height=52)

img17 = PhotoImage(file="imgs/img17.png")
b17 = Button(
    image=img17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press(2),
    relief="flat")

b17.place(
    x=100.0, y=115.0,
    width=79,
    height=52)

img18 = PhotoImage(file="imgs/img18.png")
b18 = Button(
    image=img18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: press(1),
    relief="flat")

b18.place(
    x=14.0, y=115.0,
    width=79,
    height=52)



window.resizable(False, False)
window.mainloop()


#2346
