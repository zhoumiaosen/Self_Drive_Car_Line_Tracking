import motor
import time
if __name__ =="__main__":
    
    x = input("Enter your x direction: ")
    y = input("Enter your y direction: ")
    
    print(x)
    print(y)
    
    
    if(int(x)>0 and int(y)>0):
        for i in range(abs(int(y))):
            motor.forward()
        motor.motorStop()
        time.sleep(2)
        motor.right(90)
        motor.motorStop()
        time.sleep(2)
        for a in range(abs(int(x))):
            motor.forward()
            
    if(int(x)>0 and int(y)<0):
        motor.right(90)
        motor.motorStop()
        time.sleep(2)
        for i in range(abs(int(x))):
            motor.forward()
        motor.motorStop()
        time.sleep(2)
        motor.right(90)
        motor.motorStop()
        time.sleep(2)
        for a in range(abs(int(y))):
            motor.forward()
            
    if(int(x)<0 and int(y)>0):
        for i in range(abs(int(y))):
            motor.forward()
        motor.motorStop()
        time.sleep(2)
        motor.left(90)
        motor.motorStop()
        time.sleep(2)
        for a in range(abs(int(x))):
            motor.forward()
            
    if(int(x)<0 and int(y)<0):
        motor.left(90)
        motor.motorStop()
        time.sleep(2)
        for i in range(abs(int(x))):
            motor.forward()
        motor.motorStop()
        time.sleep(2)
        motor.left(90)
        motor.motorStop()
        time.sleep(2)
        for a in range(abs(int(y))):
            motor.forward()
    
