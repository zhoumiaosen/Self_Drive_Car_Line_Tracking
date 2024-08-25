import motor
import time
if __name__ =="__main__":
    x = input("Enter Your Right Degrees: ")
    print(x)
    motor.right(int(x))
    motor.motorStop()
       
