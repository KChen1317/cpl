def main():
    print("Lexer part 1 (Tokenizer no parse)")
    file_name=get_file_name()
    file=open(str(file_name)+".txtcpl")
    proceed(3,"Getting lines\ny or proceed","Getting lines\ny or proceed")
    lines=get_lines(file)
    print(lines)
    proceed(3,"Seperating lines\ny or proceed","Seperating lines\ny or proceed")
    seperated_lines=seperate_line(lines)
    print(seperated_lines)
    print("seperated lines amt:"+str(len(seperated_lines)))
    proceed(0,"exit\ny","exit\ny")
    exit(0)



def get_file_name():
    file_name_ready=False
    while file_name_ready==False:
        file_name=input("File name?\n--->")
        try:
            file=open(str(file_name)+".txtcpl")
            file.close()
            file_name_ready=True
        except FileNotFoundError:
            print("File "+str(file_name)+" does not exist.")
            print("Note that this program expects files that have the .txtcpl extension")
        except Exception:
            print("An unexpected error has occured.\nHow did this happen?")
            print("File name was "+str(file_name))
    return(file_name)



def proceed(loop_amt ="",loop_txt ="",start_txt =""):
    print(start_txt)
    i=0
    if loop_amt=="":
        loop_amt=0
    proceed=False
    while proceed==False:
        if i==loop_amt:
            i=0
            print(loop_txt)
            x=input("--->")
            if x=="Y":
                proceed=True
            elif x=="y":
                proceed=True
            elif x=="proceed":
                proceed=True
            elif x=="Yes":
                proceed=True
            elif x=="yes":
                proceed=True
        else:
            x=input("--->")
            if x=="Y":
                proceed=True
            elif x=="y":
                proceed=True
            elif x=="proceed":
                proceed=True
            elif x=="Yes":
                proceed=True
            elif x=="yes":
                proceed=True
            i=i+1    
    



def get_lines(file):       ###srips newlines off the data
    lines_with_newline=file.readlines()
    amt_of_lines=len(lines_with_newline)
    i=0
    line_max_index=amt_of_lines-1   ###warn what if the file has no lines?
    lines=[]
    while i!=amt_of_lines-1:
        line=lines_with_newline[i]
        line_len=len(line)
        x=line_len-1
        line=line[0:x]
        lines.append(line)
        i=i+1
    x=amt_of_lines-1
    lines.append(lines_with_newline[x])
    return(lines)



def seperate_line(lines):       ###need to figure out delimiters
    lines_amt=len(lines)
    i=0
    seperated_lines=[]
    prev_component=""
    multi_line_comment=False
    while i!=lines_amt:
        line=lines[i]
        line_len=len(line)
        if multi_line_comment==False:
            prev_part=""
        curr_pointer=0
        prev_pointer=0
        print("-line-")
        print(line)
        if line=="":
            if multi_line_comment==True:
                prev_part=prev_part+""
            else:
                seperated_lines.append("")
        else:
            while curr_pointer!=line_len:
                if multi_line_comment==True:
                    print("looking for end of comment")
                    frame=line[curr_pointer:curr_pointer+2]
                    print(frame)
                    if frame=="/#":
                        print("found end of comment")
                        comment=prev_part+line[2:line_len]
                        seperated_lines.append(comment)
                        multi_line_comment=False
                        curr_pointer=line_len
                    else:
                        print("continuing search")
                        prev_part=prev_part+line
                        curr_pointer=line_len
                else:
                    print("not in a multiline comment")
                    frame=line[curr_pointer:curr_pointer+2]
                    print(frame)
                    if frame=="/#":
                        print("start of multiline comment")
                        if prev_pointer==0:
                            prev_part=line
                            curr_pointer=line_len
                            multi_line_comment=True
                        else:
                            prev_part_of_line_1=line[prev_pointer:curr_pointer]
                            seperate_line.append(prev_part_of_line_1)
                            prev_part=line[curr_pointer:line_end]
                            print("dumped any front component")
                            multi_line_comment=True
                            curr_pointer=line_len
                    else:
                        frame=line[curr_pointer:curr_pointer+1]
                        if frame=="#":
                            #frame_type="rlc"
                            if prev_pointer==0:
                                if curr_pointer==0:
                                    seperated_lines.append(line)
                                    curr_pointer=line_len
                                else:
                                    seperated_lines.append(line[0:curr_pointer])
                                    seperated_lines.append(line[curr_pointer:line_len])
                                    curr_pointer=line_len
                            else:
                                seperated_lines.append(line[prev_pointer:curr_pointer])
                                print("dumped any front component")
                                seperated_lines.append(line[curr_pointer:line_len])
                                curr_pointer=line_len
                        elif frame==";":
                            #frame_type="break"
                            print("found end of line delimiter")
                            seperated_lines.append(line[prev_pointer:curr_pointer+1])
                            prev_pointer=curr_pointer+1
                            curr_pointer=curr_pointer+1
                        else:
                            curr_pointer=curr_pointer+1
        i=i+1
    return(seperated_lines)



if 1==1:
    main()
