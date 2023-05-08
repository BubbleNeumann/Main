### (+) Задача 1
Написать программу, вычисляющую среднее, а также минимальное и максимальное значения вещественных чисел, переданных как параметры при запуске программы. Полученные три числа следует вывести на экран (консоль).
Рекомендуется писать программу, состоящую из одного класса, содержащего точку входа программы. Параметры при запуске могут указываться с ошибками.


### (+) Задача 2
Написать класс матриц, поддерживающий операцию транспонирования.
Должны быть описан один класс, который должен:
    • инкапсулировать в себе массив-матрицу;
    • иметь конструктор, параметрами которого являются размеры матрицы;
    • реализовывать получение размеров матрицы;
    • реализовывать получение и изменение отдельных элементов матрицы;
    • иметь статический метод транспонирования матриц, возвращающий транспонированную матрицу.


### Задача 3
Описать интерфейс функций, разрешающий выполнение трёх операций:
    • получение левой границы области определения;
    • получение правой границы области определения;
    • вычисление значения функции в заданной точке.
Написать базовый абстрактный класс для тригонометрических функций, реализующий методы получения границ области определения.
Написать два наследующих от него класса функций для Sin2(x) и Cos2(x).
Написать класс функции, являющейся суммой двух переданных в конструктор функций.
В методе main() создать объект для функции суммы Sin2(x) и Cos2(x), сохранить ссылку на него в поле интерфейсного типа. Вывести в консоль значения этой функции от 0 до 2π с шагом 0,1.


### (+) Задача 4
Написать программу, считающую и выводящую на экран количество вхождений заданного символа в заданный текстовый файл (символ и имя файла передаются как параметры при запуске программы).
Рекомендуется писать программу, состоящую из одного класса, содержащего точку входа программы. В случае ошибок чтения или отсутствия файла следует вывести сообщение об ошибке на русском языке.


### Задача 5
Написать программу, считывающую из заданного файла сериализованный массив вещественных чисел, сортирующую этот массив и записывающую результат в сериализованной форме в другой заданный файл (имена файлов передаются как параметры при запуске программы).
Рекомендуется писать программу, состоящую из одного класса, содержащего точку входа программы. В случае ошибок чтения или отсутствия файла следует вывести сообщение об ошибке на русском языке.


### Задача 6
Написать программу, генерирующую и записывающую в файл матрицу заданной размерности. Элементы матрицы следует брать из выборки случайной величины, равномерно распределенной на указанном интервале. Конечный файл должен быть бинарным и иметь следующий формат: целочисленное количество строк, целочисленное количество столбцов, далее перечислены вещественные элементы матрицы построчно.
Рекомендуется писать программу, состоящую из одного класса, содержащего точку входа программы. Размеры матрицы, крайние точки диапазона и имя выходного файла задаются как параметры при запуске программы.


### Задача 7
Написать класс компонента JavaBean, экземпляр которого описывает студента, обладающего следующими свойствами полного доступа: фамилия, имя, отчество, номер зачетки; а также индексированным свойством полного доступа, определяющим набор оценок студента за сессию.


### Задача 8
Написать программу, выводящую на экран форму (JFrame), содержащую единственную кнопку (“OK”), при нажатии на которую форма закрывается и программа прекращает работу.
Разрешается писать программу, состоящую из одного класса, содержащего точку входа программы.


### (+) Задача 9
Написать класс, содержащий единственный статический метод. Метод имеет единственный параметр типа Object, а возвращает ссылку на массив строк. В возвращаемом массиве должны содержаться имена методов объекта, ссылка на который передана как параметр.


### (+) Задача 10
Написать настраиваемый класс (generic class), экземпляр которого хранит ссылку на массив чисел (типа параметра), которую получает как аргумент конструктора. Также в классе должны присутствовать методы нахождения минимального и максимального значений, возвращающие тип double.


### Задача 11
Написать класс перечислимого типа, экземпляры которого описывают типы (форматы хранения) растровых изображений. У экземпляров должны быть доступны следующие методы:
•	получение расширения файла
•	получения информации о том, является ли данный формат форматом хранения с потерей качества, или без потери качества.


### Задача 12
Написать класс, инкапсулирующий массив вещественных чисел и методы доступа. Должны быть реализованы: конструктор (с указанием длины вектора), метод получения значения по номеру, метод установки значения по номеру, метод получения длины массива. Также класс должен быть сериализуемым и его экземпляры должны допускать использование в качестве аргументов в улучшенном цикле for (for-each).


### Задача 13
Написать программу, вычисляющую число π методом Монте-Карло с применением многопоточности (в расчёте на использование на многоядерном компьютере).
Метод main() получает два параметра: общее число генерируемых случайных точек и число запускаемых потоков.
Опишите класс потока, который получает в конструкторе количество генерируемых потоком случайных точек, а в теле потока выполняет следующие действия:
    • генерирует случайную точку, равномерно распределённую в области 
[0; 1]x[0; 1];
    • определяет, лежит ли эта точка внутри окружности единичного радиуса с центром в начале координат;
    • если лежит, то увеличивает значение счётчика точек на единицу.
После завершения вычисления поток должен поместить количество точек, попавших в окружность, в разделяемый объект, доступный основному потоку. Поток должен допускать корректное прерывание.
В методе main() следует создать и запустить указанное число потоков, по возможности равномерно распределив между ними количество генерируемых случайных точек.
После завершения работы всех потоков путём сложения следует получить общее количество точек, попавших в окружность, разделить его на число сгенерированных точек и умножить на 4. Полученный результат выведите в консоль.


### (+) Задача 14
Напишите класс, хранящий вещественное значение и позволяющий выполнять с ним следующие действия:
    • прибавлять к нему заданное число,
    • умножать его на заданное число,
    • устанавливать значение,
    • получать значение.
Класс должен быть реализован в соответствии с паттерном Singleton.


### Задача 15
Написать программу, выводящую на экран (в консоль) html-код страницы, путь к которой указывается как параметр программы при ее запуске.
Рекомендуется писать программу, состоящую из одного класса, содержащего точку входа программы. Разрешается выбрасывать исключения из метода main.