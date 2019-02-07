# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class People:
    def __init__(self, surname, name, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    def get_short_name(self):
        return self.surname + '.' + self.name[0] + '.' + self.patronymic[0]


class Student(People):
    def __init__(self, surname, name, patronymic, mother, father, class_room):
        People.__init__(self, surname, name, patronymic)
        self.mother = mother
        self.father = father
        self.class_room = class_room


class Teacher(People):
    def __init__(self, surname, name, patronymic, subject):
        People.__init__(self, surname, name, patronymic)
        self.subject = subject


class Class_rooms:
    def __init__(self, class_room, teacher):
        self.class_room = class_room
        self.teacher = teachers


teachers = [Teacher('Иванов', 'Иван', 'Иванович', 'Математика'),
            Teacher('Антонов', 'Антон', 'Антонович', 'Физкультура'),
            Teacher('Борисов', 'Борис', 'Борисович', 'Право'),
            Teacher('Александров', 'Александр', 'Александрович', 'Обществознание'),
            Teacher('Евгеньев', 'Евгений', 'Евгеньевич', 'Химия')]

classes = [Class_rooms('9 А', [teachers[0], teachers[1], teachers[2]]),
           Class_rooms('9 Б', [teachers[1], teachers[3], teachers[4]]),
           Class_rooms('9 В', [teachers[3], teachers[1], teachers[0]])]

parents = [People('Ляхин', 'Даниил', 'Остапович'),
           People('Ляхина', 'Геннадина', 'Геннадьевна'),
           People('Ошев', 'Константин', 'Алексеевич'),
           People('Ошева', 'Анастасия', 'Дмитриевна'),
           People('Шаталин', 'Андрей', 'Викторович'),
           People('Шаталина', 'Анна', 'Андреевна')]

students = [Student('Ляхина', 'Елизавета', 'Данииловна', parents[0], parents[1], classes[0]),
            Student('Ошев', 'Степан', 'Константинович', parents[2], parents[3], classes[1]),
            Student('Шаталина', 'Евгения', 'Андреевна', parents[4], parents[5], classes[2])]
print('Список классов в школе: ')

for c in classes:
    print(c.class_room)
for c in classes:
    print('Учителя, преподающие в {} классе:'.format(c.class_room))

    for teacher in teachers:
        print(teacher.get_full_name())

for c in classes:
    print("Ученики в классе {}:".format(c.class_room))

    for s in students:
        print(s.get_short_name())

for c in classes:
    print ("Родители учеников в классе {}:".format(c.class_room))

    for p in parents:
        print (p.get_full_name())
