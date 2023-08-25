import random


class Task:
    def __init__(self, name, point):
        self.name = name    # название домашнего дела
        self.point = point    # трудоемкость дела в баллах (определяется субъективно)

    def __repr__(self):
        return self.name


lite = []
hard = []


def create_task(name, point, times):
    # Создаем экземпляры дел и распределяем их по 2 спискам:
    # трудоемкие дела (сложность > 3 баллов) - в hard,
    # легкие дела (< 3 баллов) - в lite
    for i in range(0, times):
        task = Task(name, point)
        if task.point > 3:
            hard.append(task)
        else:
            lite.append(task)


create_task('полы', 21, 1),
create_task('пылесос', 18, 1),
create_task('готовка', 15, 5),
create_task('унитаз', 7, 1),
create_task('плита', 7, 1),
create_task('магазин', 6, 4)
create_task('туалетная комната', 4.5, 1),
create_task('ванная комната', 4.5, 1),
create_task('посуда hard', 4, 5),
create_task('посуда lite', 2.5, 20),
create_task('мусор', 1.5, 4),
create_task('стирка', 1.5, 2)


def main_func():
    # функция для создания пар словаря {домашнее дело: количество повторов за неделю}
    global lite
    global hard
    tasks = lite+hard
    max_points = round(sum([i.point for i in tasks]) / 2)    # величина для подсчета max количества баллов
    # участника исходя из созданных экземпляров класса Task
    total_list_he = []
    points_he = 0
    dictionary_he = {}
    dictionary_she = {}

    while points_he < max_points:
        try:
            any_hard_task = random.choice(hard)
            any_lite_task = random.choice(lite)
            p = any_hard_task.point + any_lite_task.point
            if any_hard_task.point > max_points - points_he:
                points_he -= (total_list_he[-1].point + total_list_he[-2].point)
                create_task(total_list_he[-1].name, total_list_he[-1].point, 1)
                create_task(total_list_he[-2].name, total_list_he[-2].point, 1)
                total_list_he.pop()
                total_list_he.pop()
                continue

            points_he += p
            total_list_he.append(any_hard_task)
            total_list_he.append(any_lite_task)
            hard.remove(any_hard_task)
            lite.remove(any_lite_task)

        except IndexError:
            break

    total_list_she = hard + lite
    points_she = sum([j.point for j in total_list_she])
    lst_he = [str(i.name) for i in total_list_he]
    lst_she = [str(i.name) for i in total_list_she]
    for i in lst_he:
        if i not in dictionary_he.keys():
            dictionary_he[i] = lst_he.count(i)

    for j in lst_she:
        if j not in dictionary_she.keys():
            dictionary_she[j] = lst_she.count(j)

    # print(points_he, dictionary_he, points_she, dictionary_she, sep='\n')
    # проверка корректности пар словарей (по необходимости)

    return [points_he, dictionary_he, points_she, dictionary_she]
