import pyautogui
import time


messege = (input("Enter the messege :~~  "))
interval = int(input("Enter the time interval :~~  "))
count_messege = int(input("Enter the messege count :~~  "))
start_interval = int(input("Enter start inteval :~~ "))

process =  input("Do you want  to print count (y/n) :~~  ")

time.sleep(start_interval)

count = 0


if process == "y":
    while count <= count_messege:
       time.sleep(interval)
       pyautogui.typewrite(messege + " " + str(count) + " :) ")
       pyautogui.press("enter")
       count = count + 1

elif process == "n":
    while count <= count_messege:
       time.sleep(interval)
       pyautogui.typewrite(messege + " :) ")
       pyautogui.press("enter")
       count = count + 1
       
    
else :
    print("Wrong input T_T ")
    print("Try again :) ")
    exit(0)





    
    
