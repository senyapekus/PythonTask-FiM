# FiM++
Версия beta

Авторы:
- Пшеничникова Ксения
- Кузьмина Лада

Ревью выполнил: Зверев Владимир

## Описание
Данное приложение является интерпретатором языка FiM++.

## Требования
- Python версии не ниже 3.9
- Установленная библиотека: tkinter

## Состав
- Файл для запуска: app.py

## Подробности реализации

## Документация от авторов

- Начало и окончание класса

Ваша программа, написанная на FiM, должна начинаться со строки

>Dear Princess Celestia: <название класса>!

Данная строка обозначает начало класса с названием <название класса>.

Необходимо также заявить об окончании класса следующим образом:

>That’s all about <название программы>!

- Функция "main"

"main" начинается со слов:

>Today I learned <название программы>!

Ваш код всегда должен заканчиваться на:

>Your faithful student, <ваше имя>.

- Присваивание переменной

Чтобы присвоить переменной значение следует использовать следующую конструкцию:

>Did you know that <название переменной> is <значение переменной>?

Значение переменной может быть как строкой, числом, так и булевой переменной. Если указываете строку, то записывайте значение в кавычках!

- Массивы

Задание массива происходит с помощью:

> Did you know that <название массива> has many names?

Дальше следует перечисление элементов массива, начиная с 1:

> <название массива> 1 is <значение>
> 
> <название массива> 2 is <значение>
> 
> <название массива> 3 is <значение>
> 
> и так далее..

Получение значения по индексу происходит с помощью команды:

> <название массива> <индекс>
> 
> I said <название массива> 2
> 
> ^ Выведет 2 элемент из массива
> 
> ИЛИ
> 
> I remember <название массива> name <индекс> as <переменная присваивания>
> 
> ^ <переменная присваивания> = <название массива>[<индекс>]

- Условие if/elif/else и Сравнение переменной

Для определения if и последующего сравнения используйте следующие конструкции:

> When <название переменной> was like <значение переменной>

Для определения elif используйте:

> However, <название переменной> was like <значение переменной>

Блок else задается как:

> I tried something else.

Конец блока if/elif/else определяется командой:

> That's what I did.

Как определить разные знаки сравнения:

> was like    =>    ==
> 
> was not like    =>    !=
> 
> had more than    =>    >
> 
> had less than    =>    <
> 
> had the same or more than    =>    >=
> 
> had the same or less than    =>    <=

- Вывод на экран (print()).

Для того, чтобы вывести что-то на экран командой print() используйте:

> I sang "что выводить"
> 
> I wrote "что выводить"
> 
> I said "что выводить"

Для подстановки ранее введенного значения в функцию print() используйте:

> I said "''название переменной''"

В python это будет выглядеть так:

> print("%s" % <название переменной>)

- Пример простой программы с условиями и выводом на экран

![image](https://user-images.githubusercontent.com/92165711/206901319-99e5b553-a31b-4731-a59b-ca31ba2c5655.png)

В python это будет выглядеть так:

![image](https://user-images.githubusercontent.com/92165711/206901292-b8376b57-4b00-4385-b108-32859076f0d7.png)

- Цикл for

Для того, чтобы определить начало цикла нужно написать:

> I did this <до какого числа будет запущен цикл> times!

Чтобы указать окончание цикла, пишем:

> That's what I did.

- Пример программы с циклом for

![image](https://user-images.githubusercontent.com/92165711/206901600-2daef1de-7028-4a54-a73e-89f604d85047.png)

Этот код на python:

![image](https://user-images.githubusercontent.com/92165711/206901624-d6c929d3-4b6f-4dea-8dd5-81fc7d0c7c3a.png)

- Цикл while

> Here's what I did while <переменная> <had more than|was like|had less than|had the same or more than|had the same or less than|was not like> <цифра>

Чтобы указать окончание цикла, пишем:

> That's what I did.

- Увеличение / уменьшение переменной (-= / +=)

> <название переменной> got/had <цифра> more/less 

- Умножение / деление переменной (*= | /=)

> I got <переменная> times <во сколько раз умножить>
> 
> I <переменная> divide <число1> by <число2>

- Пример программы с уменьшением переменной

![image](https://user-images.githubusercontent.com/92165711/206902552-e5fe74c8-96eb-41b9-a9e7-df239e8e0db8.png)

Тот же код на python:

![image](https://user-images.githubusercontent.com/92165711/206902568-9e95db1b-9648-47c4-9f5d-a235bce64d73.png)

- Пример создания функции с аргументами/без

Без аргументов:

> That's about <название функции>!

С аргументами:

> That's about <название функции> with <название аргументов через and>!

Блок функции также должен заканчиваться специальным словом:

> That's what I did.

- Пример программы с функциями:

![image](https://user-images.githubusercontent.com/92165711/207974360-41507073-7898-4ec0-8eac-18f32228e86e.png)

На python:

![image](https://user-images.githubusercontent.com/92165711/207974407-095df203-6763-4150-b576-97fec66cc6a4.png)

- Вызов функции

Без аргументов

> I learned about <название функции>

С аргументами

> I learned about <название функции> with <аргумент1> and <аргумент2>

Вызов функции и присваиваивание значения переменной

> I learned about <название функции> with <аргумент1> and <аргумент2> then I told <переменная>

> <переменная> = <название функции>(<арг1>, <арг2>)

- Явное приведение типов

> Did you know that <название переменной> is/likes (<тип приведения>) <значение переменной>?

В python строка "Did you know that hello is (int) 3?" будет выглядеть как:

> hello = int(3)

- Комментарии

> P.S. <ваш комментарий>


- Финальный пример программы на FiM

![image](https://user-images.githubusercontent.com/92165711/207975063-911b2925-8fca-4557-a5ac-79ce44e1db43.png)

Он же на Python

![image](https://user-images.githubusercontent.com/92165711/207975289-28e3ab57-1df1-405e-a2a1-f4ad8dc92b92.png)
