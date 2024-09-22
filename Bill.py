from tkinter import*
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #==========variables===========
        #=======spare parts==========
        self.clutch_plate=IntVar()
        self.Chaim_chain=IntVar()
        self.Big_roller=IntVar()
        self.small_roller=IntVar()
        self.clutch_lever=IntVar()
        self.clutch_cable=IntVar()

        #==========Engine oil==========
        self.Castrol_Active=IntVar()
        self.Bosch_oil=IntVar()
        self.Servo_4T=IntVar()
        self.MAK_Daimond=IntVar()
        self.Gear_oil=IntVar()
        self.Hero_4T=IntVar()

        #==========Battery=========
        self.Amron=IntVar()
        self.Exide=IntVar()
        self.Uplus=IntVar()
        self.Dynex=IntVar()
        self.SF_sonic=IntVar()
        self.Tesla=IntVar()

        #========Total Product Price & Tax Variables=======
        self.spare_parts_price=StringVar()
        self.Engine_oil_price=StringVar()
        self.Battery_price=StringVar()

        self.spare_parts_Tax=StringVar()
        self.Engine_oil_Tax=StringVar()
        self.Battery_Tax=StringVar()

        #==========Customer============
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_Number=StringVar()
        x=random.randint(1000,9999)
        self.bill_Number.set(str(x))

        self.search_bill=StringVar()



        #===========Customer Details Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10)

        cphn_lbl=Label(F1,text=" phone no.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=10)

        Bill_btn=Button(F1,text="search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=50,pady=10)

        #==============spare parts=============
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="spare parts",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=185,width=325,height=380)

        clutch_lbl=Label(F2,text="clutch plate",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        clutch_text=Entry(F2,width=10,textvariable=self.clutch_plate,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Chaim_chain_lbl=Label(F2,text="Chaim chain",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Chaim_chain_text=Entry(F2,width=10,textvariable=self.Chaim_chain,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Big_roller_lbl=Label(F2,text="Big roller",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Big_roller_text=Entry(F2,width=10,textvariable=self.Big_roller,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        small_roller_lbl=Label(F2,text="small roller",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        small_roller_text=Entry(F2,width=10,textvariable=self.small_roller,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        clutch_lever_lbl=Label(F2,text="clutch lever",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        clutch_lever_text=Entry(F2,width=10,textvariable=self.clutch_lever,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        clutch_cable_lbl=Label(F2,text="clutch cable",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        clutch_cable_text=Entry(F2,width=10,textvariable=self.clutch_cable,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #==============Engine oil=============
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Engine oil",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=185,width=325,height=380)

        Castrol_lbl=Label(F3,text="Castrol Active",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Castrol_text=Entry(F3,width=10,textvariable=self.Castrol_Active,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Bosch_chain_lbl=Label(F3,text="Bosch oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Bosch_chain_text=Entry(F3,width=10,textvariable=self.Bosch_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Servo_lbl=Label(F3,text="Servo 4T",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Servo_text=Entry(F3,width=10,textvariable=self.Servo_4T,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Mak_lbl=Label(F3,text="Mak Daimond",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Mak_text=Entry(F3,width=10,textvariable=self.MAK_Daimond,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Gear_lbl=Label(F3,text="Gear oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Gear_text=Entry(F3,width=10,textvariable=self.Gear_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Hero_lbl=Label(F3,text="Hero 4T",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Hero_text=Entry(F3,width=10,textvariable=self.Hero_4T,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


          #==============Battery=============
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Battery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=185,width=325,height=380)

        Amron_lbl=Label(F4,text="Amron",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Amron_text=Entry(F4,width=10,textvariable=self.Amron,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Exide_lbl=Label(F4,text="Exide",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Exide_text=Entry(F4,width=10,textvariable=self.Exide,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Uplus_lbl=Label(F4,text="Uplus",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Uplus_text=Entry(F4,width=10,textvariable=self.Uplus,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Dynex_lbl=Label(F4,text="Dynex",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Dynex_text=Entry(F4,width=10,textvariable=self.Dynex,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        SF_lbl=Label(F4,text="SF sonic",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        SF_text=Entry(F4,width=10,textvariable=self.SF_sonic,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Tesla_lbl=Label(F4,text="Tesla",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Tesla_text=Entry(F4,width=10,textvariable=self.Tesla,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #===========Bill Area======================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=185,width=500,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 20 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #==========ButtonFrame===============
        

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total spare parts price",bg=bg_color,fg="white",font=("times new roman",14, "bold")).grid(row=0,column=0,padx=20,pady=1,sticky="W")
        m1_text=Entry(F6,width=18,textvariable=self.spare_parts_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Engine oil price",bg=bg_color,fg="white",font=("times new roman",14, "bold")).grid(row=1,column=0,padx=20,pady=1,sticky="W")
        m2_text=Entry(F6,width=18,textvariable=self.Engine_oil_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Battery price",bg=bg_color,fg="white",font=("times new roman",14, "bold")).grid(row=2,column=0,padx=20,pady=1,sticky="W")
        m3_text=Entry(F6,width=18,textvariable=self.Battery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text=" spare parts Tax",bg=bg_color,fg="white",font=("times new roman",14, "bold")).grid(row=0,column=2,padx=20,pady=1,sticky="W")
        c1_text=Entry(F6,width=18,textvariable=self.spare_parts_Tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text=" Engine oil Tax",bg=bg_color,fg="white",font=("times new roman",14, "bold")).grid(row=1,column=2,padx=20,pady=1,sticky="W")
        c2_text=Entry(F6,width=18,textvariable=self.Engine_oil_Tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text=" Battery Tax",bg=bg_color,fg="white",font=("times new roman",14, "bold")).grid(row=2,column=2,padx=20,pady=1,sticky="W")
        c3_text=Entry(F6,width=18,textvariable=self.Battery_Tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=780,width=700,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=12,bd=5,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,width=12,bd=5,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=15,width=12,bd=5,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=15,width=12,bd=5,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.s_p_c_p_p=self.clutch_plate.get()*260
        self.s_p_C_c_p=self.Chaim_chain.get()*125
        self.s_p_B_r_p=self.Big_roller.get()*85
        self.s_p_s_r_p=self.small_roller.get()*70
        self.s_p_c_l_p=self.clutch_lever.get()*30
        self.s_p_c_c_p=self.clutch_cable.get()*100
        
        self.total_spare_parts_price=float(
                                       self.s_p_c_p_p+
                                       self.s_p_C_c_p+
                                       self.s_p_B_r_p+
                                       self.s_p_s_r_p+
                                       self.s_p_c_l_p+
                                       self.s_p_c_c_p
                                       )
        self.spare_parts_price.set("Rs. "+str(self.total_spare_parts_price))
        self.s_p_Tax=round((self.total_spare_parts_price*0.05),2) 
        self.spare_parts_Tax.set("Rs. "+str(self.s_p_Tax))

        self.E_o_C_A_p=self.Castrol_Active.get()*400
        self.E_o_B_o_p=self.Bosch_oil.get()*250
        self.E_o_S_4_p=self.Servo_4T.get()*270
        self.E_o_M_D_p=self.MAK_Daimond.get()*240
        self.E_o_G_o_p=self.Gear_oil.get()*200
        self.E_o_H_4_p=self.Hero_4T.get()*300

        self.total_Engine_oil_price=float(
                                       self.E_o_C_A_p+
                                       self.E_o_B_o_p+
                                       self.E_o_S_4_p+
                                       self.E_o_M_D_p+
                                       self.E_o_G_o_p+
                                       self.E_o_H_4_p
                                     
                                       )
        self.Engine_oil_price.set("Rs. "+str(self.total_Engine_oil_price))
        self.E_o_Tax=round((self.total_Engine_oil_price*0.1),2)
        self.Engine_oil_Tax.set("Rs. "+str(self.E_o_Tax))

        self.B_A_p=self.Amron.get()*950
        self.B_E_p=self.Exide.get()*1000
        self.B_U_p=self.Uplus.get()*850
        self.B_D_p=self.Dynex.get()*850
        self.B_S_s_p=self.SF_sonic.get()*900
        self.B_T_p=self.Tesla.get()*800

        self.total_Battery_price=float(
                                       self.B_A_p+
                                       self.B_E_p+
                                       self.B_U_p+
                                       self.B_D_p+
                                       self.B_S_s_p+
                                       self.B_T_p
                                       )
        self.Battery_price.set("Rs. "+str(self.total_Battery_price))
        self.B_p_Tax=round((self.total_Battery_price*0.05),2) 
        self.Battery_Tax.set("Rs. "+str(self.B_p_Tax))

        self.Total_bill=float(  self.total_spare_parts_price+
                                self.total_Engine_oil_price+
                                self.total_Battery_price+
                                self.s_p_Tax+
                                self.E_o_Tax+
                                self.B_p_Tax
                            )
                              

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome Rkcode Reatil\n")
        self.textarea.insert(END,f"\n Bill Number : {self.bill_Number.get()}")
        self.textarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number: {self.c_phone.get()}")
        self.textarea.insert(END,f"\n=========================================================")
        self.textarea.insert(END,f"\n Products\t\tQTY.\t\tPrice")
        self.textarea.insert(END,f"\n=========================================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("error","Customer details are must")
        elif self.spare_parts_price.get()=="Rs. 0.0" and self.Engine_oil_price.get()=="Rs. 0.0" and self.Battery_price.get()=="Rs. 0.0" :
            messagebox.showerror("error","no product purchased")     
        else:
            self.welcome_bill() 
            #============spare parts============
            if self.clutch_plate.get()!=0:
                self.textarea.insert(END,f"\n clutch plate\t\t{self.clutch_plate.get()}\t\t{self.s_p_c_p_p}")    
            if self.Chaim_chain.get()!=0:
                self.textarea.insert(END,f"\n Chaim chain\t\t{self.Chaim_chain.get()}\t\t{self.s_p_C_c_p}")    
            if self.Big_roller.get()!=0:
                self.textarea.insert(END,f"\n Big roller\t\t{self.Big_roller.get()}\t\t{self.s_p_B_r_p}")    
            if self.small_roller.get()!=0:
                self.textarea.insert(END,f"\n small roller\t\t{self.small_roller.get()}\t\t{self.s_p_s_r_p}")    
            if self.clutch_lever.get()!=0:
                self.textarea.insert(END,f"\n clutch lever\t\t{self.clutch_lever.get()}\t\t{self.s_p_c_l_p}")    
            if self.clutch_cable.get()!=0:
                self.textarea.insert(END,f"\n clutch cable\t\t{self.clutch_plate.get()}\t\t{self.s_p_c_c_p}")    

            #============Engine oil============
            if self.Castrol_Active.get()!=0:
                self.textarea.insert(END,f"\n Castrol Active\t\t{self.Castrol_Active.get()}\t\t{self.E_o_C_A_p}")    
            if self.Bosch_oil.get()!=0:
                self.textarea.insert(END,f"\n Bosch oil\t\t{self.Bosch_oil.get()}\t\t{self.E_o_B_o_p}")    
            if self.Servo_4T.get()!=0:
                self.textarea.insert(END,f"\n Servo 4T\t\t{self.Servo_4T.get()}\t\t{self.E_o_S_4_p}")    
            if self.MAK_Daimond.get()!=0:
                self.textarea.insert(END,f"\n Mak daimond\t\t{self.MAK_Daimond.get()}\t\t{self.E_o_M_D_p}")    
            if self.Gear_oil.get()!=0:
                self.textarea.insert(END,f"\n Gear oil\t\t{self.Gear_oil.get()}\t\t{self.E_o_G_o_p}")    
            if self.Hero_4T.get()!=0:
                self.textarea.insert(END,f"\n Hero 4T\t\t{self.Hero_4T.get()}\t\t{self.E_o_H_4_p}")    
                
            #============Battery============
            if self.Amron.get()!=0:
                self.textarea.insert(END,f"\n Amron\t\t{self.Amron.get()}\t\t{self.B_A_p}")    
            if self.Exide.get()!=0:
                self.textarea.insert(END,f"\n Exide\t\t{self.Exide.get()}\t\t{self.B_E_p}")    
            if self.Uplus.get()!=0:
                self.textarea.insert(END,f"\n Uplus\t\t{self.Uplus.get()}\t\t{self.B_U_p}")    
            if self.Dynex.get()!=0:
                self.textarea.insert(END,f"\n Dynex\t\t{self.Dynex.get()}\t\t{self.B_D_p}")    
            if self.SF_sonic.get()!=0:
                self.textarea.insert(END,f"\n SF sonic\t\t{self.SF_sonic.get()}\t\t{self.B_S_s_p}")    
            if self.Tesla.get()!=0:
                self.textarea.insert(END,f"\n Tesla\t\t{self.Tesla.get()}\t\t{self.B_T_p}")    

            self.textarea.insert(END,f"\n---------------------------------------------------------")
            if self.spare_parts_Tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n spare parts Tax\t\t\t\t{self.spare_parts_Tax.get()}")
            if self.Engine_oil_Tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Engine oil Tax\t\t\t\t{self.Engine_oil_Tax.get()}")
            if self.Battery_Tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Battery Tax\t\t\t\t{self.Battery_Tax.get()}")

            self.textarea.insert(END,f"\n Total bill : \t\t\t\t Rs.  {str(self.Total_bill)}")    
            self.textarea.insert(END,f"\n---------------------------------------------------------")
            self.save_bill()
        
    def save_bill(self):
        op=messagebox.askyesno("save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("intsab bills/"+str(self.bill_Number.get())+".text","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"Bill no. : {self.bill_Number.get()}.txt saved successfully")
        else:
            return    
        
    def find_bill(self):
        present="no"
        for i in os.listdir("intsab bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"intsab bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill no.")    

    def clear_data(self):  
        op=messagebox.askyesno("clear","Do you really want to clear?")
        if op>0:
  
                    #=======spare parts==========
            self.clutch_plate.set(0)
            self.Chaim_chain.set(0)
            self.Big_roller.set(0)
            self.small_roller.set(0)
            self.clutch_lever.set(0)
            self.clutch_cable.set(0)

            #==========Engine oil==========
            self.Castrol_Active.set(0)
            self.Bosch_oil.set(0)
            self.Servo_4T.set(0)
            self.MAK_Daimond.set(0)
            self.Gear_oil.set(0)
            self.Hero_4T.set(0)

            #==========Battery=========
            self.Amron.set(0)
            self.Exide.set(0)
            self.Uplus.set(0)
            self.Dynex.set(0)
            self.SF_sonic.set(0)
            self.Tesla.set(0)

            #========Total Product Price & Tax Variables=======
            self.spare_parts_price.set("")
            self.Engine_oil_price.set("")
            self.Battery_price.set("")

            self.spare_parts_Tax.set("")
            self.Engine_oil_Tax.set("")
            self.Battery_Tax.set("")

            #==========Customer============
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_Number.set("")
            x=random.randint(1000,9999)
            self.bill_Number.set(str(x))

            self.search_bill.set("intsab bills/")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
    
    

root=Tk()
obj = Bill_App(root)
root.mainloop()