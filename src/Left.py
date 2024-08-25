import motor
import time
if __name__ =="__main__":
    x = input("Enter Your Left Degrees: ")
    print(x)
    motor.left(int(x))
    motor.motorStop()
       
