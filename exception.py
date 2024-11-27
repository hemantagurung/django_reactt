try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divided by Zero")
except Exception as e:
    print(f"error:{e}")
finally:
    print("Executation Complete")





#self raising exception

def check_positive(num):
    if num<0:
        raise ValueError("Neg number not allowed")
    return True

check_positive(1)
check_positive(-5)


 