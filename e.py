import os
hi=input('1.write\n2.read\n')
if hi=="1":
    try:
        name=input("file name (without .txt):")
        name=name+".txt"
        line=1
        print("-------------")
        print("exit=ctrl+c")
        print("-------------")
        write=""
        while True:
            writecopy=input(f"line{line}:")
            write=write + writecopy + "\n"
            line=line+1
    except KeyboardInterrupt:
        with open(name,"w") as e:
            e.write(write)
    except:
        print("something is wrong")
if hi=="2":
    file_name=input("the .txt file should be next to the notepy\nfile name:")

    if not '.txt' in file_name:
        file_name=f"{file_name}.txt"

    file_file=os.path.abspath(file_name)
    if os.path.exists(file_file):

        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())

        except:
            print("error : no file found")

    else:
        print('error : no file found')
        
else:
    print('error')