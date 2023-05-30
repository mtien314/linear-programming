from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import pulp as p

root = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
add_folder_image = ImageTk.PhotoImage(Image.open("D:/Users/User/Downloads/icons8-start-48.png").
                                      resize((20,20),Image.ANTIALIAS))
add_image = ImageTk.PhotoImage(Image.open("D:/Users/User/Downloads/icons8-keyboard-32.png").resize((20,20),
                                                    Image.ANTIALIAS))

add_image2 = ImageTk.PhotoImage(Image.open("D:/Users/User/Downloads/icons8-bmo-48.png").resize((20,20),
                                                    Image.ANTIALIAS))
class App:
    def __init__(self):

        root.title("Linear Programming ")
        root.geometry("500x500")
        self.beginB = customtkinter.CTkButton(master = root,image=add_folder_image,
                                               text="Start", command=self.begin,
                        width = 190, height=40)
        self.beginB.pack()
        self.beginB.place(relx = 0.5, rely = 0.5,anchor = CENTER)
        self.prolem = ""

    def begin(self):
        root.title("Linear Programming")
        self.beginB.destroy()
        del self.beginB
        self.goB = customtkinter.CTkButton(root, image=add_folder_image,text='Min', 
                                           command=self.button1_clicked)
        self.goB.pack()
        self.goB.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.goB2 = customtkinter.CTkButton(root,image=add_folder_image,text='Max',
                                             command=self.button2_clicked)
        self.goB2.pack()
        self.goB2.place(relx = 0.5,rely = 0.4, anchor = CENTER)
    
    def button1_clicked(self):
        self.m = p.LpProblem("Minimize",p.LpMinimize)
        self.prolem = "Mimimize"
        return self.go_on()
    
    def button2_clicked(self):
        self.m = p.LpProblem("Maximize",p.LpMaximize)
        self.prolem = "Maximize"
        return self.go_on()

    def go_on(self):
        root.title("Linear Programming")
        self.goB.destroy()
        self.goB2.destroy()
        del self.goB
        del self.goB2

        self.goB3 = customtkinter.CTkButton(root,image=add_image,width=100,text='Generate',
                                            command=self.save_textBox)
        self.goB3.pack()
        self.goB3.place(relx = 0.9,rely = 0.1,anchor= SE)
        
        self.label = customtkinter.CTkLabel(root, text = "Total Variables:")
        self.label.pack()
        self.label.place(relx = 0.2,rely = 0.1, anchor = SE)
        self.textbox = customtkinter.CTkTextbox(root,height=2.4,width=50,border_width=2,
                                                border_color="Red")
        self.textbox.pack()
        self.textbox.place(relx = 0.32,rely = 0.1, anchor = SE)
        
        self.label2 = customtkinter.CTkLabel(root, text = "Total Contraints:")
        self.label2.pack()
        self.label2.place(relx = 0.55,rely= 0.1,anchor = SE)
        
        self.textbox2 = customtkinter.CTkTextbox(root,height=3,width=50,border_width=2,
                                                border_color="Red")
        self.textbox2.pack()
        self.textbox2.place(relx = 0.67,rely = 0.1, anchor = SE)
    
    def save_textBox(self):
        
        self.text = self.textbox.get(0.0,END)
        self.text2 = self.textbox2.get(0.0,END)

        self.n = int(self.text)
        self.n2 = int(self.text2)
        n = self.n
        n2 = self.n2

        self.textbox = []
        self.constraint = []
        self.char_constraint = []
        self.num_constraint = []

        if n>2:
            k = 0
        else:
            k = 0.2
        
        k2 = k

        self.label3 = customtkinter.CTkLabel(root, text = "Z = ")
        self.label3.pack()
        self.label3.place(relx = k+0.1,rely = 0.3, anchor = SE)
        
        for i in range(n):
            k+=0.2
            if i== self.n-1:
                label = customtkinter.CTkLabel(root,text =f"X{i+1}")
            else:
                label = customtkinter.CTkLabel(root,text =f"X{i+1}")
                label2 = customtkinter.CTkLabel(root , text = " + ")
                label2.pack()
                label2.place(relx = k+0.085,rely = 0.3,anchor = SE)

            label.pack()
            label.place(relx = k+0.05,rely = 0.3,anchor = SE)

            
            self.box = customtkinter.CTkEntry(root,width=50,border_color="Red")
            self.box.pack()
            self.box.place(relx = k,rely = 0.3,anchor = SE)
            
            self.textbox.append(self.box)
            
        #Create n constraint
        h = 0.4
       
        while n2!=0:
            k3 = k2-0.1
            for i in range(n):
                k3 +=0.2
                
                label = customtkinter.CTkLabel(root,text =f"X{i+1}")
                label.pack()
                label.place(relx = k3+0.05,rely = h,anchor = SE)

                if i==self.n-1:
                    
                    self.textbox_constraint1 = customtkinter.CTkEntry(root,width=50,border_color="Red",
                                                                      textvariable=customtkinter.StringVar())
                    self.textbox_constraint1.pack()
                    self.textbox_constraint1.place(relx = k3+0.2,rely = h,anchor = SE)
                    
                    self.textbox_constraint2 = customtkinter.CTkEntry(root,width=50,border_color="Red",
                                                                      textvariable=customtkinter.StringVar())
                    self.textbox_constraint2.pack()
                    self.textbox_constraint2.place(relx = k3+0.35,rely =h,anchor = SE )

                    self.char_constraint.append(self.textbox_constraint1)
                    self.num_constraint.append(self.textbox_constraint2)

                else:
                    label2 = customtkinter.CTkLabel(root , text = " + ")
                    label2.pack()
                    label2.place(relx = k3+0.085,rely =h,anchor = SE)

                self.textbox3 = customtkinter.CTkEntry(root,width=50,border_color="Red")
                self.textbox3.pack()
                self.textbox3.place(relx = k3,rely = h,anchor = SE)
                self.constraint.append(self.textbox3)

            n2 -=1
            h += 0.1

        self.goB4 = customtkinter.CTkButton(root,image=add_image,width=100,text='Solve',
                                            command=self.save_contraint)
        self.goB4.pack()
        self.goB4.place(relx = 0.9,rely = 0.3,anchor = SE)

    def save_contraint(self):
        
        self.goB4.destroy()
        del self.goB4

        self.goB5 = customtkinter.CTkButton(root,image=add_image2,width=100,text='Answer',
                                            command=self.solve_problem)
        self.goB5.pack()
        self.goB5.place(relx = 0.9,rely = 0.3,anchor = SE)

    def solve_problem(self):
        top = customtkinter.CTkToplevel(root)
        top.title("Linear Programming")
        top.geometry("500x500")
        self.x = [p.LpVariable(f'x_{i}') for i in range(1,self.n+1)]
        h =p.lpSum(int(box.get())*self.x[i] for i,box in enumerate(self.textbox))
        self.m += h
        
        constraint = []
        char_constraint = []
        num_constraint = []

        for i,num in enumerate(self.constraint):
            constraint.append(int(num.get()))
        
        for _,char in enumerate(self.char_constraint):
            char_constraint.append(char.get())

        for _, num in enumerate(self.num_constraint):
            num_constraint.append(int(num.get()))
        
        j = 0
        k = 0
        s = 0 
        for _ in range(self.n2):
            c = 0
            for i in range(self.n):             
                c +=constraint[j]*self.x[i]
                j+=1
                print(c)
            if char_constraint[k] == ">=":
                self.m += c >= num_constraint[s]
            elif char_constraint[k] == "<=":
                self.m += c <= num_constraint[s]
            else:
                self.m += c == num_constraint[s]
            s+=1
            k+=1

        print(self.m)
        self.status = self.m.solve()

        command_text = ""
        command_value = ""
        
        if self.status == p.LpStatusInfeasible:
            command_text = "Bài toán vô nghiệm\n" 
        
        elif self.status == p.LpStatusOptimal:
            optimal_value = p.value(self.m.objective)
            has_loose_contraint = False
            for contraint in self.m.constraints.values():
                if p.value(contraint)==contraint.constant:
                    has_loose_contraint = True
                    break

            has_depent_variable = False

            for var in self.m.variables():
                if p.value(var) !=0:
                    has_depent_variable = True
                break

            if has_depent_variable and has_loose_contraint == False:
                command_text = "Bài toán vô số nghiệm\n"
            else:
                command_text = "Nghiệm tối ưu:\n"
                for i, variable in enumerate(self.x):
                    command_value += f"x{i + 1} =" + str(p.value(variable))
                    command_value +='\n'
            command_value += "Giá trị tối ưu: Z =" + str(optimal_value)

        elif self.status == p.LpSolutionUnbounded:
            command_text = "Bài toán không giới nội\n"
            if self.prolem == "Maximize":
                command_value = "Z = Inf"
            else:
                command_value = "Z = -Inf"
        else:
            command_text = "Bài toán có trạng thái không xác định"
        
        self.label4 = customtkinter.CTkTextbox(top,width=300,height = 150)
        self.label4.insert(END,"ANSWER:\n")
        self.label4.insert(END,command_text)
        self.label4.insert(END,command_value)
        self.label4.pack()
        self.label4.place(relx = 0.65,rely = 0.5,anchor =SE)
App()
root.mainloop()