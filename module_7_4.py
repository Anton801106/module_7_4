# Домашнее задание по теме "Форматирование строк".

team1 = '"Мастера кода"'
team2 = '"Волшебники данных"'
team1_num = 5
team2_num = 6
score_1 = 42
score_2 = 42
team1_time = 1200
team2_time = 1500
team1_time_avg = team1_time / score_1
team2_time_avg = team2_time / score_2
tasks_total = score_1 + score_2
time_total = team1_time + team2_time
time_avg = time_total / tasks_total

# Использование %:
print('В команде "Мастера кода" участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %d!' % (team1_num, team2_num))

# Использование format():
print('Команда {title} решила задач: {postfix}!'.format(title='"Волшебники данных"', postfix=score_2))
print('{title} решили задачи за {team1_time} c. !'.format(title='"Волшебники данных"', team1_time=18015.2))

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

print(f'Команда {team1} решила задач: {score_1}!')
print(f'Команда {team1} решила {score_1} задачи за {team1_time} c., в среднем каждую задачу за {team1_time_avg} с.!')
print(f'Команда {team2} решила {score_2} задачи за {team2_time} c., в среднем каждую задачу за {team2_time_avg} с.!')


def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time or team1_time == team2_time:
        print(f'Победа команды {team1}!')
    elif score_2 > score_1 or score_1 == score_2 and team2_time < team1_time or team1_time == team2_time:
        print(f'Победа команды {team2}!')
    else:
        print('Ничья!')
        return result


result = challenge_result
print(challenge_result())

# Использование %:
#
# Переменные: количество участников первой команды (team1_num).
# Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
#
# Переменные: количество участников в обеих командах (team1_num, team2_num).
# Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"

# Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
# Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
#
# Переменные: время за которое команда 2 решила задачи (team1_time).
# Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"

# Использование f-строк:
# Переменные: количество решённых задач по командам: score_1, score_2
# Пример итоговой строки: "Команды решили 40 и 42 задач.”
#
# Переменные: исход соревнования (challenge_result).
# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
#
# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
# Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
