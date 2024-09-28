def main():
    n = int(input(" nhap vao so ho :"))

    for i in range(n):
        print(" ho thu " , i+1)
    
        while True:
            maho = input(" nhap vao ma ho:") + "\n"
            if(maho != ""):
                break
        while True:
            tenho = input(" nhap vao ten ho:") + "\n"
            if(tenho != ""):
                break  
        while True:
            dchi = input(" nhap vao dchia:") + "\n"
            if(dchi != ""):
                break
        while True:
            kw = int(input(" nhap vao so kw:")) 
            if(kw>=0):
                break  
            
        with open(" data.txt" , "a") as file:
            file.writelines([maho,tenho,dchi,str(kw)])
                   
main()


    
               

    