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

Значение переменной может быть как строкой, так и числом. Если указываете строку, то записывайте значение в кавычках!

- Условие if/else и Сравнение переменной

Для определения if и последующего сравнения используйте следующие конструкции:

>When <название переменной> was like <значение переменной>

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

- Вывод на экран (print())

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

Блок else задается как:

> I tried something else.

Конец блока if/else определяется командой:

> That's what I did.

- Пример простой программы с условиями и выводом на экран

Dear Princess Celestia: Hello World!


Today I learned how to say Hello World!

Did you know that hello is "Hello world"?

When hello was like "Hello world"

I sang "Hello is hello world"

I tried something else.

I wrote "Hello is not hello world"

That's what I did.

I said "''hello''"

That’s all about how to say Hello World!


Your faithful student, Twilight Sparkle.


В python это будет выглядеть так:


if __name__ == '__main__':
    hello = "Hello world"
    if hello == "Hello world":
        print("Hello is hello world")
    else:
        print("Hello is not hello world")
    print("%s" % hello) 
