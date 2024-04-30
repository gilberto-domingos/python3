

'''
#Objects
person = {
    "name": "Programmer", 
    "age": 18,
    "weight": 70.2
}

print(person['name'])
print(person['age'])
print(person['weight'])


#while
scores = []

counter = 1

while counter <= 3:
    cod_student = input("Codigo": ")  
    score = float(input("nota :"))
    result = [cod_student, score]
    scores.append(result)

    counter = counter + 1

print("Quantidade de notas", len(scores))



#FOR
scores = []
for x in range(3):
    cod_student = input("Codigo: ")
    score = float(input("nota :"))
    result = [cod_student, score]
    scores.append(result)

print("Quantidade de notas", len(scores))
for n in scores:
    cod_student = n[0]
    score = n[1]
    print("Código" cod_student, "tirou a nota", score)
 


#add data list
empty_list = []
empty_list.append("olá")
empty_list.append("mundo")
print(empty_list)

# change value list
numbers_list = [1,2,3]
numbers_list[0] = 5
print("O primeiro numero da lista é :", numbers_list[0])

# inputs
name = input("type your name")
age = int(input("type your age"))
weigth = float(input("type your weight"))

print (type((name)))
print(age)
print(weigth)


#vars
var1, var2 = "junior", 18
print(var1,var2)

# coments
# os mais utilizado para web Django, FastAPI, Flask
# RPA -> Selenium, Robocorp, BotCity
# Mobile -> Kivy, BeeWare

django = "usar muito com python e request"
request = "usar request para extrair informações de outros sites"
p_test = "p test para testes automáticos"

media = 10 - 5
print(media)

var_name = "var com nomes longos"
print(var_name)

name = "Gilberto Domingos"
print(name)
'''