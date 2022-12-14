# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/FlateCool/guess-number-task#какой-кейс-решаем)  
[2. Какой кейс решаем?](https://github.com/FlateCool/guess-number-task#какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/FlateCool/guess-number-task#краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/FlateCool/guess-number-task#этапы-работы-над-проектом)  
[5. Результат](https://github.com/FlateCool/guess-number-task#результаты)    
[6. Выводы](https://github.com/FlateCool/guess-number-task#выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/FlateCool/guess-number-task#оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
Программа генерирует 1000 случайных чисел, используя seed = 1 
и потом предает каждое из них в функцию угадывания, работающую по принципу дихотомии. Эта функция возвращает чило шагов половинного деления. Для полученных шагов (всего их будет 1000, как и исходных случайных чисел) находтися математическое среднее.

[Ссылка](https://drive.google.com/file/d/1v00Xg7F_TsU-pSe6_iSTcmI_xcX_35G_/view?usp=share_link) на файл с данными 
  
:arrow_up:[к оглавлению](https://github.com/FlateCool/guess-number-task#оглавление)


### Этапы работы над проектом  
Написать функцию find_guessed_number, находящую загаданное число методом дихотомии.

:arrow_up:[к оглавлению](https://github.com/FlateCool/guess-number-task#оглавление)


### Результаты:  
Среднее число попыток угывания загаданного числа: 5

:arrow_up:[к оглавлению](https://github.com/FlateCool/guess-number-task#оглавление)


### Выводы:  
Метод дихотомии (половинного деления) очень хорошо подходит для решения данной задачи

:arrow_up:[к оглавлению](https://github.com/FlateCool/guess-number-task#оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами