class Number :
    i = 0 
if __name__ == "__main__":
    n1 = Number()
    n2 = Number()
    n1.i = 2 
    n2.i = 5 
    n1.i = n2.i 
    n2.i = 10 
    print(f"giá trị n1.i : {n1.i}")
    print(f"giá trị n2.i : {n2.i}")



