#Описание класса Student
class Student:
    def __init__(self):
        self.fio = ""
        self.cls = ""
    def __init__(self, fio):
        self.fio = fio
        self.cls = ""
    def __init__(self, fio, cls):
        self.fio = fio
        self.cls = cls
    def __str__(self):
        return "ФИО: "+ self.fio +" Класс: "+ self.cls
#Пустой список учащихся, который будет наполняться
studentList = []
#Форма для пользователя с инструкциями запросов
while True:
    print("+ - Добавить учащегося\nl - Вывести список учащихся\ns - Вывести отсортированный список учащихся\n")
    cmd = input()
#Обработка команд
    if cmd == "+":
       print("ФИО:")
       fio = input()
       print("Класс")
       cls = input()
       st = Student(fio, cls)
       studentList.append(st)
#Вывод списка без сортировки
    elif cmd == "l":
       print("------Список учащихся------")
       for student in studentList:
        print(student)
       print("------")
       #Вывод сортированного списка
    elif cmd == "s":
       sortedList = studentList
       sortedList.sort(key = lambda x: x.cls)
       print("------Список учащихся------")
       for student in sortedList:
        print(student)
       print("------")

