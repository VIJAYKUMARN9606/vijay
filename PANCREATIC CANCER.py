import tkinter as tk
import tkinter.messagebox
import pandas as pd
from tkinter import *

 
import mysql.connector as mysql


import tkinter.filedialog
from tkinter import ttk


from PIL import ImageTk,Image  

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from pandas import DataFrame
import matplotlib.pyplot as plt

class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.root.geometry("975x507+300+100");
       self.root.title(" Pancreatic Cancer Prediction System ")
       self.root.configure(bg="green")
       self.canvas = tk.Canvas(self.root, width =975, height = 507)  
       self.canvas.place(x=0,y=0);


       self.img1 = ImageTk.PhotoImage(Image.open("img1.jpg"))  



       b1 = tk.Button(self.root,image=self.img1,width=975,height=507,bg="green",fg="white",relief="raised",font=("Comic Sans Ms",14,"bold"),command=self.createNewWindow)
       b1.place(x=0,y=0) 
       
       self.root.mainloop()

   def createNewWindow(self):
       self.root.destroy()
       app=browwin();
       

   def exit(self):
       self.root.destroy()        



class browwin:
    def __init__(self):
        self.f=tk.Tk();
        self.f.geometry("985x624+100+100");
        self.f.configure(bg="#A6DFEE");
        self.f.title(" Pancreatic Cancer Prediction System ")
        self.f.configure(bg="green")
        self.canvas = tk.Canvas(self.f, width =985, height = 624)  
        self.canvas.place(x=0,y=0);
        

        self.img2 = ImageTk.PhotoImage(Image.open("img3.jpeg")) 
        l22 = tk.Label(self.f, image=self.img2,width=985,relief="ridge",fg="#323223",font=("Comic Sans Ms",14,"bold"))
        l22.place(x=0,y=0)



              
        b1=tk.Button(self.f,text="SELECT THE FILE",width=25,height=1,bg="aquamarine",font=("Comic Sans Ms",14,"bold"),command=self.Load)
        b1.place(x=310,y=210)
        
                      

        self.f.mainloop();
        
        
    def Load(self):
        self.fname=tkinter.filedialog.askopenfilename();
        tk.messagebox.showinfo("File Browse"," Selecting File="+self.fname);
        self.t1 = tk.Label(self.f,text="",width=35,height=2,relief="raised",bg="#092193",fg="white",font=("Comic sans ms",16,"bold"))
        self.t1.place(x=310,y=310)
        self.t1.configure(text=self.fname); 
        
        b2=tk.Button(self.f,text="Read or Load Data",width=16,height=1,bg="magenta",font=("Comic Sans Ms",14,"bold"),command=self.Dataset)
        b2.place(x=380,y=420)
        
        
    def Dataset(self): 
        tk.messagebox.showinfo("File Browse"," Data is loading ="+self.fname);
        data=pd.read_csv(self.fname);
       # print(data);
        self.loading();
        

    def loading(self):
        
       tkinter.messagebox.showinfo(" Pancreatic Cancer Prediction System "," Data Loading Functio is Called...");
       
       fname=self.fname
       print("File Name="+fname)
       if(fname==""):       
           tkinter.messagebox.showinfo(" Pancreatic Cancer Prediction System"," Please Enter File Name....");
       else:
           tkinter.messagebox.showinfo(" Pancreatic Cancer Prediction System "," Data set of File="+fname+" is Loading ...Please Wait...");
           self.dataload()
           
           
    def dataload(self):
           fname=self.fname
           data=pd.read_csv(fname)

           data.columns=[col.lower() for col in data];  # Makes all columns To Lower Case
           n=data.shape
           #print(" Total Record=")
           max=n[0]
           #print(max)
           
           
           con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
           s = con.cursor() 

           s.execute("delete from ds1");
           con.commit()

           for i in range(max):
               rec=data.iloc[i]
               f1=str(rec[0])
               f2=str(rec[1])
               f3=str(rec[2])
               f4=str(rec[3])
               f5=str(rec[4])
               f6=str(rec[5])
               f7=str(rec[6])
               f8=str(rec[7])
               f9=str(rec[8])
               f10=str(rec[9])
               f11=str(rec[10])
               f12=str(rec[11])
               f13=str(rec[12])
               f14=str(rec[13])
               f15=str(rec[14])
               f16=str(rec[15])
               f17=str(rec[16])
               f18=str(rec[17])
               
               
               #print(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18);
               sql="insert into ds1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
               s.execute(sql,(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18));
               con.commit()
         
           print(" All Data Transfered And Stored in Data Base....");    
           tkinter.messagebox.showinfo(" Cancer Prediction System "," All Cancer Patients Data Transfered And Stored in Data Base....");
           self.f.destroy()
           app=Load();

     
     
class Load:
       def __init__(self):
           self.load = tk.Tk()
           self.load.geometry("1200x600+100+100");

           self.load.configure(bg="#812336")
           self.load.title(" Pancreatic Cancer Prediction System ")
         


           con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
           s = con.cursor()
           
           sql="select * from ds1"
           s.execute(sql);
           rows=s.fetchall()
           total=s.rowcount
           #print("\n Total Data Records=\t"+str(total));

           self.canvas = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")
           self.canvas.place(x=20,y=100);
           self.canvas.pack();

           l1 = tk.Label(self.canvas,text=" Patients Data Set Details ",width=50,relief="raised",bg="red",fg="white",font=("Comic Sans Ms",14,"bold"))
           l1.place(x=300,y=20)
           
     
           self.tv=ttk.Treeview(self.load,column=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),show="headings",height="15")

           self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
           self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
           ttk.Style().configure("Treeview", background="#092193",foreground="white", fieldbackground="red",font=('Comic Sans Ms', 10,'bold'))
           self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
           self.tv.column('18', minwidth=150, stretch=False)

           self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
           self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
           self.tv.pack(expand=True, fill=tk.BOTH)
        
        
           self.tv.heading("#1",text="PID")
           self.tv.heading("#2",text="COUNTRY")
           self.tv.heading("#3",text="AGE")
           self.tv.heading("#4",text="	GENDER")
           self.tv.heading("#5",text="	SMOKING ")
           self.tv.heading("#6",text="OBESITY")
           self.tv.heading("#7",text="	DIABETES")
           self.tv.heading("#8",text="	CHORONIC PANCREAS")
           self.tv.heading("#9",text="	FAMILY HISTORY")
           self.tv.heading("#10",text=" HEREDITARY") 
           self.tv.heading("#11",text="JAUNDICE")
           self.tv.heading("#12",text="ABDOMINAL_PAIN")
           self.tv.heading("#13",text="BACK PAIN")
           self.tv.heading("#14",text="WEIGHT LOSS")
           self.tv.heading("#15",text="ALCOHOL")
           self.tv.heading("#16",text="DIET_PROCESS")
           self.tv.heading("#17",text="URBAN OR RURAL")
           self.tv.heading("#18",text="ECONOMIC")
    	
           for i in rows:
               self.tv.insert('','end',values=i)

           self.canvas1 = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")  
           self.canvas1.place(x=20,y=500);
           self.canvas1.pack();

           b1 = tk.Button(self.canvas1,text=" Analyse Data Set ",width=25,relief="raised",bg="blue",fg="white",font=("Times New roman",14,"bold"),command=self.dataload1)
           b1.place(x=500,y=14)

           self.load.mainloop()
     
       def dataload1(self):
           tkinter.messagebox.showinfo(" Pancreatic Cancer Prediction System "," The Process of Analyse and Prediction of Disease Begins");
           self.load.destroy();
           app=Analysis();
           
           
class Analysis:
   def __init__(self):

       self.ananly = tk.Tk()
       self.ananly.geometry("1000x600+300+100");
       self.ananly.title(" Pancreatic Cancer Disease Prediction System ")
       self.ananly.configure(bg="#912388")
                          
       self.canvas = tk.Canvas(self.ananly, width = 1000, height = 600)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("img2.png"))  
       l1 = tk.Label(self.ananly, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("Comic Sans Ms",14,"bold"))
       l1.place(x=0,y=00)

     
       b1 = tk.Button(self.ananly,text=" Extract Featured Attribute  ",width=30,bg="green",fg="white",relief="groove",font=("Comic Sans Ms",12,"bold"),command=self.feaetr)
       b1.place(x=250,y=210)
       

       b4 = tk.Button(self.ananly, text=" Exit ",width=30,bg="green",fg="white",relief="groove",font=("Comic Sans Ms",12,"bold"),command=self.exit)
       b4.place(x=250,y=290)

       self.ananly.mainloop()

   def feaetr(self):

            tkinter.messagebox.showinfo(" Pancreatic Cancer Prediction System"," Extraction of Required Data from Oveall Data Set Information...")

            con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
            s = con.cursor()
            
            s.execute("delete from ds2");


            sql="select pid,age,gen,smoker,obs,dia,chrpan,jaun,abdo_pain,backpain,weloss,alco,diet_food from ds1";
            s.execute(sql);
            rows=s.fetchall()

            con.commit()

            for rec in rows:

                f1=str(rec[0])
                f2=str(rec[1])
                f3=str(rec[2])
                f4=str(rec[3])
                f5=str(rec[4])
                f6=str(rec[5])
                f7=str(rec[6])
                f8=str(rec[7])
                f9=str(rec[8])
                f10=str(rec[9])
                f11=str(rec[10])
                f12=str(rec[11])
                f13=str(rec[12])

                
                
                print(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13);
                sql="insert into ds2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                s.execute(sql,(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13));
                con.commit()
            total=s.rowcount
            print("\n Total Data Records=\t"+str(total));

            self.canvas = tk.Canvas(self.ananly, width = 1200, height = 60,bg="#232342")
            self.canvas.place(x=20,y=100);
            self.canvas.pack();

            l1 = tk.Label(self.canvas,text=" Extracted Featured Attributes Details Of Pancreatic Cancer Patients ",width=50,relief="raised",bg="red",fg="white",font=("Times New roman",14,"bold"))
            l1.place(x=250,y=20)

            self.tv=ttk.Treeview(self.ananly,column=(1,2,3,4,5,6,7,8,9,10,11,12,13),show="headings",height="15")

            self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
            self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
            ttk.Style().configure("Treeview", background="green",foreground="white", fieldbackground="aquamarine",font=('Times New roman', 10,'bold'))
            self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
            self.tv.column('9', minwidth=50, stretch=False)

            self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
            self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
            self.tv.pack(expand=True, fill=tk.BOTH)
         
            self.tv.heading("#1",text="PID")

            self.tv.heading("#2",text="AGE")
            self.tv.heading("#3",text="	GENDER")
            self.tv.heading("#4",text="	SMOKING ")
            self.tv.heading("#5",text="OBESITY")
            self.tv.heading("#6",text="	DIABETES")
            self.tv.heading("#7",text="	CHORONIC PANCREAS")
            self.tv.heading("#8",text="JAUNDICE")
            self.tv.heading("#9",text="ABDOMINAL_PAIN")
            self.tv.heading("#10",text="BACK PAIN")
            self.tv.heading("#11",text="WEIGHT LOSS")
            self.tv.heading("#12",text="ALCOHOL")
            self.tv.heading("#13",text="DIET_PROCESS")

            for i in rows:
                self.tv.insert('','end',values=i)

            self.canvas1 = tk.Canvas(self.ananly, width = 1200, height = 60,bg="#232342")  
            self.canvas1.place(x=20,y=500);
            self.canvas1.pack();

            b1 = tk.Button(self.canvas1,text=" Predict Cancer Patients  ",width=40,relief="raised",bg="red",fg="white",font=("Times New roman",14,"bold"),command=self.loading)
            b1.place(x=450,y=14)

            self.ananly.mainloop()
      
   def loading(self):
            self.ananly.destroy()
            app=Prediction()
            
   def prediction(self):
           self.ananly.destroy()
           app=Load()

   def exit(self):
            self.ananly.destroy()


class Prediction:
   def __init__(self):
       self.prediction = tk.Tk()
       self.prediction.geometry("500x400+400+200")
       self.prediction.title(" Pancreatic Cancer Disease Prediction System ")

       self.canvas = tk.Canvas(self.prediction, width=500, height=400)
       self.canvas.place(x=100, y=150)

       self.img1 = ImageTk.PhotoImage(Image.open("img4.png"))
       b1 = tk.Button(self.prediction, image=self.img1, width=500, bg="cyan", fg="yellow", relief="raised",
                      font=("Times New roman", 12, "bold"), command=self.croppred)
       b1.place(x=0, y=0)

       self.prediction.mainloop()

   def croppred(self):
       tkinter.messagebox.showinfo(" Pancreatic Cancer Disease Prediction", " Disease Prediction Begins...")
       tkinter.messagebox.showinfo(" Pancreatic Cancer Disease Prediction ", " Prediction of Pancreatic Cancer Disease ...")

       con = mysql.connect(host="localhost", user="root", passwd="mj", database="pancre", use_pure="True", charset='utf8')
       s1 = con.cursor()

       s1.execute("delete from disease")

       sql = "select pid,age,gen,smoker,obs,dia,chrpan,jaun,abdo_pain,backpain,weloss,alco,diet_food from ds2"
       s1.execute(sql)
       rows = s1.fetchall()
       con.commit()

       for rec in rows:
           pid = str(rec[0])
           age = int(rec[1])
           gen = str(rec[2])
           smoker = int(rec[3])
           obseity = int(rec[4])
           dia = int(rec[5])
           chpa = int(rec[6])
           jaun = int(rec[7])
           abdpain = int(rec[8])
           bacpa = int(rec[9])
           weloss = int(rec[10])
           alcohol = int(rec[11])
           difo = str(rec[12])


           if(alcohol < 3):
               alcohol1 = "Low";
           elif(alcohol > 3 and alcohol < 6):
               alcohol1 = "Medium";
           else:
               alcohol1 = "High";

           if(smoker < 3):
               smoker1 = "Low";
           elif(smoker > 3 and smoker < 6):
               smoker1 = "Medium";
           else:
               smoker1 = "High";

           if(dia == 0):
               dia1 = "Low";
           elif(dia > 1 and dia < 3):
               dia1 = "Medium";
           else:
               dia1 = "High";

           if(weloss < 3):
               wloss1 = "Low";
           elif(weloss > 3 and weloss < 6):
               wloss1 = "Medium";
           else:
               wloss1 = "High";

           if(jaun < 2):
               jaun1 = "Low";
           elif(jaun > 2 and jaun < 5):
               jaun1 = "Medium";
           else:
               jaun1 = "High";

           if(abdpain < 3):
               abdpain1 = "Low";
           elif(abdpain > 3 and abdpain < 6):
               abdpain1 = "Medium";
           else:
               abdpain1 = "High";

           if(bacpa < 3):
               bacpa1 = "Low";
           elif(bacpa > 3 and bacpa < 6):
               bacpa1 = "Medium";
           else:
               bacpa1 = "High";

           if(obseity < 3):
               obseity1 = "Low";
           elif(obseity > 3 and obseity < 6):
               obseity1 = "Medium";
           else:
               obseity1 = "High";

           if(chpa < 3):
               chpa1 = "Low";
           elif(chpa > 3 and chpa < 6):
               chpa1 = "Medium";
           else:
               chpa1 = "High";

           if(difo == "Low"):
               difo1 = "Low";
           elif(difo == "Medium"):
               difo1 = "Medium";
           else:
               difo1 = "High";
               
               
           if (jaun1 == "Medium") and (smoker1 == "High") and (age > 20) and (wloss1 == "Medium") and (dia1 == "Low") and (difo1 == "High") and (obseity1 == "High") and (chpa1 == "High"):
               disease = "Cancer is At 1st Stage";
           elif (dia1 == "Medium") and (jaun1 == "Medium") and ((wloss1 == "Low") or (wloss1 == "Medium")) and (difo1 == "High") and (obseity1 == "Medium") and (chpa1 == "Medium"):
               disease = "Cancer is At 2nd Stage";
           elif ((dia1 == "Medium") or (dia1 == "High")) and ((jaun1 == "Medium") or (jaun1 == "High")) and (wloss1 == "High") and (difo1 == "High") and (obseity1 == "High") and (chpa1 == "High"):
               disease = "Cancer is At 3rd Stage";
           elif ((dia1 == "Medium") or (dia1 == "High")) and ((jaun1 == "Low") or (jaun1 == "Medium") or (jaun1 == "High")) and ((wloss1 == "Low") or (wloss1 == "High")) and ((difo1 == "Medium") or (difo1 == "High")) and ((obseity1 == "Medium") or (obseity1 == "High")) and ((chpa1 == "Medium") or (chpa1 == "High")):
               disease = "Cancer is At 3rd Stage";
           elif (jaun1 == "Medium") and ((smoker1 == "Medium") or (smoker1 == "High")) and (age > 30) and ((wloss1 == "Low") or (wloss1 == "Medium")) and (dia1 == "Low") and (bacpa1 == "Low") and ((difo1 == "Medium") or (difo1 == "High")) and ((obseity1 == "Medium") or (obseity1 == "High")) and ((chpa1 == "Medium") or (chpa1 == "High")):
               disease = "Cancer is At Beginning Stage";
           elif (jaun1 == "Low") and (smoker1 == "Low") and (age > 20) and ((wloss1 == "Low") or (wloss1 == "Medium") or (wloss1 == "High")) and (dia1 == "Low") and ((bacpa1 == "Low") or (bacpa1 == "Medium")) and ((difo1 == "Low") or (difo1 == "Medium")) and ((obseity1 == "Low") or (obseity1 == "Medium")) and ((chpa1 == "Low") or (chpa1 == "Medium")):
               disease = "Cancer is Not At Present State";
           else:
               disease = "No Cancer";



           sql1 = "INSERT INTO disease VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           s1.execute(sql1, (pid, age, gen, alcohol1, smoker1, dia1, wloss1, jaun1,abdpain1, bacpa1, obseity1, chpa1,difo1, disease ))
           con.commit()

       tkinter.messagebox.showinfo(" Pancreatic Cancer Disease Prediction ","Pancreatic Cancer Disease Prediction of a Patient Completed ....")
       self.prediction.destroy();
       app = Load2()

   def exit(self):
       self.prediction.destroy()
       app = Analysis()


class Load2:
   def __init__(self):
       self.load = tk.Tk()
       self.load.geometry("1200x600+100+100");
       self.load.configure(bg="#812336")
       self.load.title(" Pancreatic Cancer Prediction System ")
     


       con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
       s = con.cursor()
       
       sql="select * from disease"
       s.execute(sql);
       rows=s.fetchall()
       total=s.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Pancreatic Cancer Disease Predicted Result Details ",width=50,relief="raised",bg="red",fg="white",font=("Times New roman",14,"bold"))
       l1.place(x=300,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3,4,5,6,7,8,9,10,11,12,13,14),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#213473",foreground="white", fieldbackground="red",font=('Times New roman', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('11', minwidth=150, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="PID")

       self.tv.heading("#2",text="AGE")
       self.tv.heading("#3",text="	GENDER")
       self.tv.heading("#4",text="	SMOKING ")
       self.tv.heading("#5",text="OBESITY")
       self.tv.heading("#6",text="	DIABETES")
       self.tv.heading("#7",text="	CHORONIC PANCREAS")
       self.tv.heading("#8",text="JAUNDICE")
       self.tv.heading("#9",text="ABDOMINAL_PAIN")
       self.tv.heading("#10",text="BACK PAIN")
       self.tv.heading("#11",text="WEIGHT LOSS")
       self.tv.heading("#12",text="ALCOHOL")
       self.tv.heading("#13",text="DIET_PROCESS")
       self.tv.heading("#14",text="Result")
 
      
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Analyse The Result ",width=25,relief="raised",bg="red",fg="white",font=("Times New roman",14,"bold"),command=self.dataload1)
       b1.place(x=500,y=14)
       
       import numpy as np
       import pandas as pd
       import matplotlib.pyplot as plt

       from sklearn.model_selection import train_test_split
       from sklearn.neighbors import KNeighborsClassifier
       from sklearn.metrics import confusion_matrix
       from sklearn.metrics import accuracy_score

       data=pd.read_csv("pancreatic.csv")
       n=data.shape;
       n=n[0];

       X=data.iloc[:,4:13]
       y=data.iloc[:,-1]

       X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=1234)

       print("\nthe training set\n")
       print(X_train)

       print("\nthe training set\n")
       print(y_train)
       print(y_train.shape)

       print("\nthe test set\n")
       print(X_test)
       print(X_test.shape)


       #print(X_train.value_counts())

       print(" KNN ALGORITHM ");

       knn=KNeighborsClassifier(n_neighbors=7,metric='euclidean')
       print(knn.fit(X_train,y_train))
       print(knn)

       y_predict1=knn.predict(X_test)
       print(y_predict1)

       cm=confusion_matrix(y_test,y_predict1)
       print(cm)
       knnacc=accuracy_score(y_test,y_predict1);
       print(knnacc)

       import seaborn as sns
       df_cm = pd.DataFrame(cm, columns=np.unique(y_test), index = np.unique(y_test))
       df_cm.index.name = 'Actual'
       df_cm.columns.name = 'Predicted'
       plt.figure(figsize = (10,7))
       sns.set(font_scale=1.4)#for label size
       sns.heatmap(df_cm, cmap="Blues", annot=True,annot_kws={"size": 16})


       X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=1234)

       print("\nthe training set\n")
       print(X_train)

       print("\nthe training set\n")
       print(y_train)
       print(y_train.shape)

       print("\nthe test set\n")
       print(X_test)
       print(X_test.shape)

       print(" DECISION TREE ALGORITHM ");

       from sklearn.tree import DecisionTreeClassifier
       classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
       classifier.fit(X_train, y_train)

       # Predicting the Test set results
       y_pred = classifier.predict(X_test)
       #print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

       # Making the Confusion Matrix
       from sklearn.metrics import confusion_matrix, accuracy_score
       cm = confusion_matrix(y_test, y_pred)
       print(cm)

       from sklearn.metrics import accuracy_score
       deacc=accuracy_score(y_test, y_pred)
       print("accuracy=",deacc)

       import seaborn as sns
       df_cm = pd.DataFrame(cm, columns=np.unique(y_test), index = np.unique(y_test))
       df_cm.index.name = 'Actual'
       df_cm.columns.name = 'Predicted'
       plt.figure(figsize = (10,7))
       sns.set(font_scale=1.4)#for label size
       sns.heatmap(df_cm, cmap="Blues", annot=True,annot_kws={"size": 16})


       print(" \n Accuracy Of KNN")
       print(knnacc*100);

       print(" \n Accuracy Of Decision Tree")
       print("accuracy=",deacc*100)

       x=["KNN","DECISION TREE"]
       y=[]
       y.append(knnacc*100)
       y.append(deacc*100)

       plt.figure(figsize=[6,6])
       plt.bar(x,y,width=0.24);
       plt.legend(['Testing Accuracy', 'Testing Accuracy'],fontsize=18)
       plt.title('Accuracy Curves',fontsize=16)
       plt.show()


 
       self.load.mainloop()
 
   def dataload1(self):
       tkinter.messagebox.showinfo(" Cancer Prediction System "," The Process of Analyse and Prediction of Disease Begins");
       self.load.destroy();
       app=classify();
       
class classify:
   def __init__(self):
       
       self.classify = tk.Tk()
       self.classify.geometry("813x410+300+100");
       self.classify.title(" Pancreatic Cancer Disease Prediction System ")
       self.classify.configure(bg="#912388")
                          
       self.canvas = tk.Canvas(self.classify, width = 813, height = 411)  
       self.canvas.place(x=0,y=0);

       self.img5 = ImageTk.PhotoImage(Image.open("img5.jpg"))  
       l2 = tk.Label(self.classify, image=self.img5,width=813,relief="groove",fg="#323223",font=("Times New roman",14,"bold"))
       l2.place(x=0,y=00)

       b1 = tk.Button(self.classify,text=" Cancer Disease Classify By Stages ",width=30,height=1,bg="white",fg="magenta",relief="groove",font=("Times New roman",15,"bold"),command=self.diseaseclass)
       b1.place(x=150,y=120)
       
       b2 = tk.Button(self.classify,text=" Age ",width=30,height=1,bg="white",fg="red",relief="groove",font=("Times New roman",15,"bold"),command=self.age)
       b2.place(x=150,y=210)

       b3 = tk.Button(self.classify,text=" Exit ",width=30,height=1,bg="white",fg="darkblue",relief="groove",font=("Times New roman",15,"bold"),command=self.exit)
       b3.place(x=150,y=300)

       self.classify.mainloop()

   def diseaseclass(self):
       tkinter.messagebox.showinfo(" Pancreatic Cancer Disease Data Analysis "," Pancreatic Cancer Disease Patient Data Analysis On Disease Stages ...")
       self.classify.destroy()
       app=DiseaseClass()
       
   def age(self):
       tkinter.messagebox.showinfo(" Pancreatic Cancer Disease Data Analysis "," Pancreatic Cancer Disease Patient Data Analysis On Age Group ...")
       self.classify.destroy()
       app=age()

   def exit(self):
       self.classify.destroy()
      

class age:
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
       self.load.configure(bg="#232342")
       self.load.title(" Pancreatic Cancer Disease  Data Analysis Based on Age Group  ")
     

       con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
       s = con.cursor()
       

       sql="select pid,age,res from disease";
       s.execute(sql);
       rows=s.fetchall()
       total=s.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Pancreatic Cancer Disease  Data Analysis Based on Age Group ",width=50,relief="raised",bg="darkred",fg="white",font=("Times New roman",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3),show="headings",height="10")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('Times New roman', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('3', minwidth=100, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Patient ID")
       self.tv.heading("#2",text="Age")
       self.tv.heading("#3",text="Result")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Classify Age Group ",width=45,relief="raised",bg="darkred",fg="white",font=("Times New roman",12,"bold"),command=self.graph)
       b2.place(x=260,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="aquamarine",fg="white",font=("Times New roman",12,"bold"),command=self.back)
       b3.place(x=30,y=12)


       self.load.mainloop()
      
   def graph(self):

       tkinter.messagebox.showinfo(" Pancreatic Cancer Disease Data Data Analysis "," Pancreatic Cancer Disease Data Processingn on Age Group Processing classification Begins ...")
       con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
       s = con.cursor()
 
       s.execute("delete from class");

       sql="select pid,age,res from disease"
       s.execute(sql);
       rows=s.fetchall()
       total=s.rowcount
       print("\n Total Data Records=\t"+str(total));

       for rec in rows:
           id=str(rec[0])
           age=int(rec[1])
           res=str(rec[2])
           
           if(age>10 and age<20):
               ageclass="Age(10-20) Class"
           elif(age>20 and age<30):
               ageclass="Age(20-30) Class"
           elif(age>30 and age<40):
               ageclass="Age(30-40) Class"
           elif(age>40 and age<50):
               ageclass="Age(40-50) Class"
           elif(age>50 and age<60):
               ageclass="Age(50-60) Class"
           else:
               ageclass="Age(>60) Class"
        
           sql="insert into class values(%s,%s)"
           s.execute(sql,(ageclass,res));
           con.commit()
           
           
       self.load.destroy()
       app=Age1()

            

   def back(self):
       self.load.destroy()
       app=classify

       
class Age1():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
       self.load.configure(bg="#232342")
       self.load.title("Pancreatic  Cancer Disease  Data Analysis Based on Age Group  ")
     

       con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
       s = con.cursor()
       

       sql="select age,count(*) from class group by age";
       s.execute(sql);
       rows=s.fetchall()
       total=s.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Pancreatic Cancer Disease  Data Analysis Based on Age Group ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2),show="headings",height="5")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('2', minwidth=100, stretch=False)
       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Age")
       self.tv.heading("#2",text="No OF Patients")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Analyse using Graph  ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=60,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=500,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" Pancreatic Cancer Disease Data Analysis "," Pancreatic Cancer Disease Data Analysis Using Graphical Representation ...")
       con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
       s = con.cursor()
 
       s.execute("delete from graph");

       sql="select age,res,count(*) from class group by age,res order by age";
       s.execute(sql);
       rows=s.fetchall()

       for row in rows:
           age=str(row[0])
           res=str(row[1])
           cnt=int(row[2])
           sc=age+"-"+res;
           sql="insert into graph values(%s,%s)"
           s.execute(sql,(sc,cnt));
           con.commit()

       self.load.destroy()
       app=OverallAgeGraph88()
           


   def selected(self,a):
       print(" Item Clicke");
       self.data=self.tv.item(self.tv.selection())
       print(self.data)
       item=self.tv.selection()[0]
       print(item)
       self.age=str(self.tv.item(item)['values'][0])
       print(self.age)

       con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
       s = con.cursor()
 
       s.execute("delete from graph");

       sql="select age,res,count(*) from class where age='"+self.age+"' group by age,res order by age";
       s.execute(sql);
       rows=s.fetchall()

       for row in rows:
           age=str(row[0])
           res=str(row[1])
           cnt=int(row[2])
           sc=age+"-"+res;
           sql="insert into graph values(%s,%s)"
           s.execute(sql,(sc,cnt));
           con.commit()

       self.load.destroy()
       app=OverallAgeGraph88()
 

   def back(self):
       self.load.destroy()
       app=classify

class OverallAgeGraph88():
   def __init__(self):
       self.graph2= tk.Tk() 
       self.graph2.geometry("1600x1000+10+10")               
       self.graph2.title(" Graphical Representation of Data Analysis On Age Group Class");                      

       self.canvas = tk.Canvas(self.graph2, width = 1200, height = 60)
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Pancreatic Cancer Disease Data Analysis Based On Age Group Class ",width=70,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=100,y=20)

       b1 = tk.Button(self.canvas,text=" Back  ",width=27,relief="raised",bg="darkblue",fg="white",font=("cambria",13,"bold"),command=self.back)
       b1.place(x=890,y=20)

       con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
       s = con.cursor() 

       sql="select * from graph";
       s.execute(sql);
       rows=s.fetchall()

       df = pd.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'dc',1: 'cnt'}, inplace=True);

       dc=df['dc']
       dc=dc.values

       print(dc)

       for i in range(0, len(dc)): 
           dc[i] = str(dc[i])

       print("\n------------------\n")
       print(dc)
       print("\n------------------\n")


       cnt=df['cnt']
       cnt=cnt.values
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = float (cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

       xx1=cnt
       print(xx1)

       yy1=dc
       print(yy1)

       data2 = {'cnt': xx1,
                'dc': yy1
                }
 

       self.canvas1 = tk.Canvas(self.graph2, width = 600, height =800,bg="#918289")
       self.canvas1.place(x=30,y=70);

       figure3 = plt.Figure(figsize=(10,7), dpi=100)
       ax1 = figure3.add_subplot(221)

   
       df2 = DataFrame(data2,columns=['cnt','dc'])
       df2 = df2[['cnt','dc']].groupby('dc').sum()
       df2.plot(kind='bar', legend=True, ax=ax1,color="cyan",fontsize=10)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#312094")
       ax1.set_title('Disease Class Vs Total No Of Patients',fontsize=10, fontweight='bold')
       ax1.set_xlabel(' Disease Class ',fontsize=12, fontweight='bold')
       ax1.set_ylabel(' Total Number Of Patients ',fontsize=10, fontweight='bold')
        
       bar1 = FigureCanvasTkAgg(figure3, self.canvas1)
       bar1.get_tk_widget().place(x=0,y=0);





       self.canvas3 = tk.Canvas(self.graph2, width = 600, height =800,bg="#918289")
       self.canvas3.place(x=650,y=70);

   
       figure3 = plt.Figure(figsize=(13,9), dpi=70)
       ax1 = figure3.add_subplot(111)
      
       country_data =dc
       medal_data = cnt

       print(dc)

       colors = ["#2ca02c","red", "#ff7f0e",  "#d62728", "#8c564b","#982363"]
       explode = (0.1, 0, 0, 0, 0)  
       ax1.pie(medal_data, labels=country_data, explode=None, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=150)
       ax1.axis('equal')  
       pie2 = FigureCanvasTkAgg(figure3, self.canvas3)
       pie2.get_tk_widget().pack()


       self.graph2.mainloop();
       
   
   def back(self):
       self.graph2.destroy();
       app=classify()


       self.load.mainloop()        
       


class DiseaseClass():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x600+250+100");
       self.load.configure(bg="#232342")
       self.load.title(" Pancreatic Cancer Disease Data Analysis Based on Disease Class  ")
     

       con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
       s = con.cursor()
       

       sql="select res,count(*) from disease group by res order by age";
       s.execute(sql);
       rows=s.fetchall()
       total=s.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Pancreatic Cancer Disease Data Analysis Based on Disease Class ",width=70,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2),show="headings",height="10")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('2', minwidth=100, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Disease Class")
       self.tv.heading("#2",text=" Total Patient ")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Analyse using Graph  ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=60,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=550,y=12)


       self.load.mainloop()
      
   def graph(self):

       tkinter.messagebox.showinfo(" Pancreatic Cancer Disease Data Analysis "," Pancreatic Cancer Disease Data Analysis Using Graphical Representation ...")
       con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
       s = con.cursor()
 
       s.execute("delete from graph");

       sql="select res,count(*) from disease group by res order by age";
       s.execute(sql);
       rows=s.fetchall()

       for row in rows:
           res=str(row[0])
           cnt=int(row[1])
           sc=res;
           sql="insert into graph values(%s,%s)"
           s.execute(sql,(sc,cnt));
           con.commit()

       self.load.destroy()
       app=OverallLocGraph88()

   def back(self):
       self.load.destroy()
       app=classify()
class OverallLocGraph88():
   def __init__(self):
       self.graph2= tk.Tk() 

       self.graph2.geometry("1600x1000+10+10")               
       self.graph2.title(" Graphical Representation of Data Analysis On Disease Class");                      

       self.canvas = tk.Canvas(self.graph2, width = 1200, height = 60)
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Pancreatic Cancer Disease Data Analysis Based On Disease Stages ",width=50,relief="raised",bg="darkred",fg="white",font=("Times New roman",14,"bold"))
       l1.place(x=150,y=20)

       b1 = tk.Button(self.canvas,text=" Back  ",width=35,relief="raised",bg="darkblue",fg="white",font=("Times New roman",13,"bold"),command=self.back)
       b1.place(x=750,y=20)

       con = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="pancre",use_pure= "True",charset='utf8')
       s = con.cursor() 

       sql="select * from graph";
       s.execute(sql);
       rows=s.fetchall()

       df = pd.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'dc',1: 'cnt'}, inplace=True);

       dc=df['dc']
       dc=dc.values

       print(dc)

       for i in range(0, len(dc)): 
           dc[i] = str(dc[i])

       print("\n------------------\n")
       print(dc)
       print("\n------------------\n")


       cnt=df['cnt']
       cnt=cnt.values
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = float (cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

       xx1=cnt
       print(xx1)

       yy1=dc
       print(yy1)

       data2 = {'cnt': xx1,
                'dc': yy1
                }
 

       self.canvas1 = tk.Canvas(self.graph2, width = 600, height =700,bg="aquamarine")
       self.canvas1.place(x=30,y=70);

       figure3 = plt.Figure(figsize=(10,7), dpi=100)
       ax1 = figure3.add_subplot(221)

   
       df2 = DataFrame(data2,columns=['cnt','dc'])
       df2 = df2[['cnt','dc']].groupby('dc').sum()
       df2.plot(kind='bar', legend=False, ax=ax1,color="magenta",fontsize=12)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#312094")
       ax1.set_title('Disease Class Vs Total No Of Patients',fontsize=10, fontweight='bold',pad=20)
       ax1.set_xlabel(' Disease Class ',fontsize=10, fontweight='bold')
       ax1.set_ylabel(' Total Number Of Patients ',fontsize=10, fontweight='bold')
        
       bar1 = FigureCanvasTkAgg(figure3, self.canvas1)
       bar1.get_tk_widget().place(x=0,y=0);


       self.canvas3 = tk.Canvas(self.graph2, width = 600, height =700,bg="pink")
       self.canvas3.place(x=700,y=70);

   
       figure4 = plt.Figure(figsize=(8, 7), dpi=100)  # Bigger size for clarity
       ax2 = figure4.add_subplot(111)

       # Data
       labels = dc
       sizes = cnt

       # Custom colors for better distinction
       colors = ["#FF9999", "#66B3FF", "#99FF99", "#FFCC99", "#C2C2F0", "#FFB3E6"]

       # Explode all slices slightly to avoid crowding
       explode = [0.08] * len(sizes)

       # Plot pie chart
       wedges, texts, autotexts = ax2.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',startangle=140,explode=explode,shadow=True,textprops={'fontsize': 10, 'color': 'black'})

       # Make title bold and readable
       ax2.set_title('Percentage of Disease Stages', fontsize=14, fontweight='bold',pad=20)

       # Equal aspect ratio ensures pie is a circle
       ax2.axis('equal')

       # Add chart to canvas
       pie2 = FigureCanvasTkAgg(figure4, self.canvas3)
       pie2.get_tk_widget().pack()



       self.graph2.mainloop() 
   
   def back(self):
       self.graph2.destroy();
       app=classify()



app =Test()


