import tkinter as tk

def evaluate(event):
    myString = entry.get()
    results = ""
    ##############################
    if (myString == 'Square'):
        for i in range(15):
            for j in range(15):
                results = results + '  *'
            results = results + '\n'
    
    if (myString == 'Triangle'):
        for i in range(15):
            for j in range(15):
                    if i==j:
                        results = results + ' 0'
                    elif j<i:
                        results = results + ' '
                    elif i+j==14:
                        results = results + ' 0'
                    else:
                        results = results + ' *'
                    



                    
            results = results + '\n'
        print(results)

    res.configure(text = "The output is: \n " + results)
            
 
            

w = tk.Tk()
tk.Label(w, text="Please Enter  format of the output (i.e. Square or Triangle):").pack()
entry = tk.Entry(w)
myString = entry.get()
print(myString)

entry.bind("<Return>", evaluate)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()