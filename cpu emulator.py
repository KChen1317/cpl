


def main():
    true=(2**64)-1
    max_address_mem=(2**64)-1
    pc=0
    reg={"r1":0,"r2":0,"r3":0,"r4":0,"r5":0,"r6":0,"r7":0,"r8":0,"r9":0}
    intr=0
    intr_handle=0
    sp_write=2**64-1
    instr_mem_write=2**64-1
    rand=get_rand()
    special={"intr":intr,"intr handle":intr_handle,"sp write":sp_write,"instr mem write":instr_mem_write,"rand":rand}
    instr_mem={}
    data_mem={}
    io_mem={}
    mem={"instr":instr_mem,"data":data_mem,"io":io_mem}
    single_instr()
    



def single_instr():
    global reg
    global pc
    global special
    global mem
    instr=get_instr(pc)
    data=get_data(pc)
    target_reg=get_target_reg(instr,"reg")
    instr_type=get_instr_type(instr,"instr")
    if instr_type=="INTR INVOP":    #eg the instr fetched is out of range
        intr=intr_conv(instr_type,"instr")  #only need to handle one of these
        pc=intr_handle
    else:   #no interupt, continue
        frame=instr_type[0:2]
        instr_type=instr_type[2:len(instr_type)]
        target_reg=rep_list_conv_str(target_reg)
        if frame=="A-":     #arithmetic instr
            a=1
        elif frame=="S-":   #binary shift
            a=1
        elif frame=="B-":   #bitwise operation
            a=1
        elif frame=="M-":   #mem operation
            a=1
        elif frame=="C-":   #condtionals
            a=1
        elif frame=="J-":   #jumps
            a=1
        elif frame=="N-":   #nop
            a=1
        elif frame=="I-":   #interupts and etc
            a=1



def intr_conv(intr):
    if intr=="INTR ILLMEM":
        return(1)
    elif intr=="INTR ILLOP":
        return(2)
    elif intr=="INTR INVOP":
        return(3)
    elif intr=="THROW": #does not exist on actual cpu
        return(4)       #we use this to id when to handle intr from Thr()



#operations
def Nadd(target_reg):
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=target_reg[2]
    d=a+b
    if d==max_address or d>max_address: #overflow handling
        d=d-max_address
    intr_status=reg_write(c,d)
    return(intr_status)



def Nsub(target_reg):
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=target_reg[2]
    d=a-b
    if d<0: #underflow handling
        d=d+max_address
    intr_status=reg_write(c,d)
    return(intr_status)



def Sadd(target_reg):
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=target_reg[2]
    bin_a=format(a,"064b")
    bin_b=format(a,"064b")
    frame_1=bin_a[0:1]
    frame_2=bin_b[0:1]
    if frame_1=="0":    #handle conversion of the 
        frame_1=bin_a[1:64]
        frame_1=int(frame_1,2)
        a=frame_1
    else:
        frame_1=bin_a[1:64]
        frame_1=int(frame_1,2)
        frame_1=frame_1*-1
        a=frame_1
    if frame_2=="0":
        frame_2=bin_a[1:64]
        frame_2=int(frame_2,2)
        a=frame_2
    else:
        frame_2=bin_a[1:64]
        frame_2=int(frame_2,2)
        frame_2=frame_2*-1
        a=frame_2
    d=a+b
    max_vaule=(2**63)-1
    min_vaule=max_vaule*-1
    if d==max_vaule or d>max_vaule: #overflow
        frame=format(d,"064b")
        frame=frame[0:63]
        frame="0"+frame
        d=int(frame,2)
    else:
        if d==min_vaule or d<min_vaule: #underflow
            frame=format(d,"064b")
            frame=frame[0:63]
            frame="1"+frame
            d=int(frame,2) 
    intr_status=reg_write(c,d)
    return(intr_status)



def Ssub(target_reg):
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=target_reg[2]
    bin_a=format(a,"064b")
    bin_b=format(a,"064b")
    frame_1=bin_a[0:1]
    frame_2=bin_b[0:1]
    if frame_1=="0":
        frame_1=bin_a[1:64]
        frame_1=int(frame_1,2)
        a=frame_1
    else:
        frame_1=bin_a[1:64]
        frame_1=int(frame_1,2)
        frame_1=frame_1*-1
        a=frame_1
    if frame_2=="0":
        frame_2=bin_a[1:64]
        frame_2=int(frame_2,2)
        a=frame_2
    else:
        frame_2=bin_a[1:64]
        frame_2=int(frame_2,2)
        frame_2=frame_2*-1
        a=frame_2
    d=a-b
    max_vaule=(2**63)-1
    min_vaule=max_vaule*-1
    if d==max_vaule or d>max_vaule: #overflow
        frame=format(d,"064b")
        frame=frame[0:63]
        frame="0"+frame
        d=int(frame,2)
    else:
        if d==min_vaule or d<min_vaule: #underflow
            frame=format(d,"064b")
            frame=frame[0:63]
            frame="1"+frame
            d=int(frame,2) 
    intr_status=reg_write(c,d)
    return(intr_status)



#shifts
#all throw intr
#log shift delets data
#arith shift does not
def LshiR():
    a=1


def AshiR():
    a=1


def LshiL():
    a=1



def AshiL():
    a=1


#bitwise operation
#all throw intr
def Not(target_reg):
    a=reg[target_reg[0]]
    b=target_reg[1]
    bin_max=max_address_mem
    a=~a
    a=bin_max+a
    intr_status=reg_write(b,a)
    return(intr_status)


def And(target_reg):
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=target_reg[2]
    d=a&b
    intr_status=reg_write(c,d)
    return(intr_status)



def Or(target_reg):
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=target_reg[2]
    d=a|b
    intr_status=reg_write(c,d)
    return(intr_status)


def Xor(target_reg):
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=target_reg[2]
    d=a^b
    intr_status=reg_write(c,d)
    return(intr_status)


#reg set
#all throw intr
def Set(target_reg,data):
    a=reg[target_reg[0]]
    data=data[0]
    intr_status=reg_write(a,data)
    return(intr_status)



def Clr(target_reg,data):
    a=reg[target_reg[0]]
    data=0
    intr_status=reg_write(a,data)
    return(intr_status)


#memory
#has intr throwing operations
def RR(target_reg):
    #throws intr
    a=reg[target_reg[0]]
    b=target_reg[1]
    intr_status=reg_write(b,a)
    return(intr_status)



def RM(target_reg): #write to mem
    #no intr
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=reg[target_reg[2]]
    data=a
    mem_type=b
    address=c
    if mem_type==0:
        intr_status=instr_mem_write(address,data)
    elif mem_type==1:
        intr_status=data_mem_write(address,data)
    elif mem_type==2:
        intr_status=io_mem_write(address,data)
    return(intr_status)
    


def MR(target_reg):
    #throws intr
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=target_reg[2]
    mem_type=a
    address=b
    targeted_reg=c
    if mem_type==0:
        data=instr_mem_get(address)
    elif mem_type==1:
        data=data_mem_get(address)
    elif mem_type==2:
        data=io_mem_get(address)
    intr_status=reg_write(targeted_reg,data)
    return(intr_status)



#conditional
#all throw intr
def CmpE(target_reg):
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=target_reg[2]
    if a==b:
        intr_status=reg_write(c,true)
    else:
        intr_status=reg_write(c,false)
    return(intr_status)



def CmpL(target_reg):
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=target_reg[2]
    if a<b:
        intr_status=reg_write(c,true)
    else:
        intr_status=reg_write(c,false)
    return(intr_status)
    


def CmpG(target_reg):
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    c=target_reg[2]
    if a>b:
        intr_status=reg_write(c,true)
    else:
        intr_status=reg_write(c,false)
    return(intr_status)



#jumps
#no operation throw intr
def IfT(target_reg):
    global pc
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    if a==true:
        pc=b
    else:
        pc=pc+4



def IfF(target_reg):
    global pc
    a=reg[target_reg[0]]
    b=reg[target_reg[1]]
    if a==false:
        pc=b
    else:
        pc=pc+4



def Jmp(target_reg):
    global pc
    a=reg[target_reg[0]]
    pc=a



#nop
#why would ths throw an exception?
def Nop(target_reg):
    a=1



#special instructions
#all throw intr
def SSet(target_reg):
    a=reg[target_reg[0]]
    b=target_reg[1]
    intr_status=reg_write(b,a)
    return(intr_status)


def Thr(target_reg):
    global special
    a=reg[target_reg[0]]
    special["intr"]=a
    return("THROW")
    

#reg write handler
def reg_write(target_reg,data):
    global reg
    global pc
    global special
    frame=target_reg[0:1]
    if frame=="r":  #eg we are writing to a normal register
        reg[target_reg]=data
        return(0)
    else:   #special registers
        if target_reg=="pc":    #write to pc
            pc=data
            return(0)
        else:
            if special["sp write"]==0:
                if target_reg=="sp write" or target_reg=="intr":    #onlu alllowed special regs if sp write is locked
                    special[target_reg]=data
                    return(0)
                else:
                    return("INTR ILLOP")    #not allowed
            else:   #sp write is not locked so we can write to special regs
                special[target_reg]=data
                return(0)

    

#data extraction fuctions


def get_instr(pc):
    address=pc
    instr=instr_mem_get(address)
    return(instr)


def get_data(pc):
    address_base=pc
    d1=instr_mem_get(address_base+1)
    d2=instr_mem_get(address_base+2)
    d3=instr_mem_get(address_base+3)
    data_list=(d1,d2,d3)
    return(data_list)


def get_instr_type(instr,section):
    #can throw ecxception
    instr=instr_conv_str(instr)
    frame=instr[0:47]
    if frame!="0000000000000000000000000000000000000000000000": #no instruction with any bits in this range
        return("INTR INVOP")
    else:
        frame=instr[47:52]
        frame=bin(frame)
        frame=int(frame,2)
        if frame>25:
            return("INTR INVOP")
        else:
            instr_conv_table=("A-Nadd","A-Nsub","A-Sadd","A-Ssub","S-LshiR","S-AshiR","S-LishL","S-AshiL","B-Not","B-And","B-Or","B-Xor","M-RR","M-RM","M-MR","C-CMPE","C-CMPL","C-CMPG","J-IFT","J-IFF","J-JMP","N-NOP","I-SSET","I-THR")
            instr_type=instr_conv_table[frame]
            frame_1=int(bin(instr[52:56]),2)    #check reg vaules
            frame_2=int(bin(instr[56:60]),2)
            frame_3=int(bin(instr[60:64]),2)
            if frame_1>14 or frame_2>14 or frame_3>14:
                return("INTR INVOP")
            else:
                if section=="instr":    
                    return(instr_type)
                elif section=="reg":
                    reg=(frame_1,frame_2,frame_3)
                    return(reg)



def instr_conv_str(instr):
    bin_instr=format(instr,"064b")
    str_instr=str(bin_instr)
    return(str_instr)
    
    
def reg_list_conv_str(reg_list):
    i=0
    conv_list=("r1","r2","r3","r4","r5","r6","r7","r8","r9","pc","intr","intr handle","sp write","instr mem write","rand")
    reg_str_list=()
    while i!=2:
        frame=reg_list[i]
        reg_str_list.append(conv_list[frame])
    return(reg_str_list)
        




#mem read/write functions

def instr_mem_get(address):
    #never throws a exception
    #address should be bounded
    if address==max_address_mem or address>max_address_mem:
        address=address-max_address
    data=instr_mem.get(str(address),"None")
    if data=="None":
        data=0
    return(data)



def instr_mem_write(address,data):
    #can throw exception
    global instr_mem
    if instr_mem_write==0:
        return("INTR ILLOP")    #not allowed
    else:
        if data==0:
            address_data=instr_mem.get[str(address),"None"]
            if address_data=="None":
                return(0)
            else:
                instr_mem.pop(str(address))
                return(0)
        else:
            instr_mem[str(address)]=data
            return(0)


def data_mem_get():
    #never throws a exception
    #address should be bounded
    if address==max_address_mem or address>max_address_mem:
        address=address-max_address
    data=data_mem.get(str(address),"None")
    if data=="None":
        data=0
    return(data)



def data_emem_write():
    #does not throw exception
    global data_mem
    if data==0:
        address_data=data_mem.get[str(address),"None"]
        if address_data=="None":
            return(0)
        else:
            data_mem.pop(str(address))
            return(0)
    else:
        data_mem[str(address)]=data
        return(0)



def io_mem_get():
    #never throws a exception
    #address should be bounded
    if address==max_address_mem or address>max_address_mem:
        address=address-max_address
    data=io_mem.get(str(address),"None")
    if data=="None":
        data=0
    return(data)


def io_mem_write(address,data):
    #does not throw exception
    global io_mem
    if data==0:
        address_data=io_mem.get[str(address),"None"]
        if address_data=="None":
            return(0)
        else:
            data_mem.pop(str(address))
            return(0)
    else:
        io_mem[str(address)]=data
        return(data)


    

def a():
    a=1



if 1==1:
    main()
