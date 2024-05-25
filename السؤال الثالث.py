import json

filename = input("Enter your name of the json file with question and answer: ")
grad=0
with open ("questions.json","r") as file:
    z=json.load(file)
    name = input("enter your name: ")
    for i in range (1,21):
        user_answer = input(f"{i} : {z[str(i)][0]} : ")
        if user_answer == z[str(i)][1]:
            grad+=1
print(f"the deserved grad is {grad}")      
try:
    with open('result.json','a' ,newline='') as file:   
        file.write(user_answer+ ":"+ str(grad)+ "/n")
except IOError:
    print("Error: could not write to result.json file.")        
              
            
