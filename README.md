# OOP_FitnessTracker
## Описание
Учебный проект в котором реализованы классы Running, SportsWalking и Swimming, унаследованные от класса Training.

Running - тренировка-бег,  
SportsWalking - тренировка-спортивная ходьба,
Swimming - тренировка-плавание.

Training принимает аргументы:

`action, тип int — количество совершённых действий (число шагов при ходьбе и беге либо гребков — при плавании);`
  
`duration, тип float — длительность тренировки;`
  
`weight, тип float — вес спортсмена.`
 
Running принимает аргументы Training

SportsWalking принимает аргументы:

`Аргументы Training;`

`height, тип float - рост человека`

Swimming принимает аргументы:

`Аргументы Training;`

`length_pool, тип float - длина бассейна в метрах;`

`count_pool, тип int -  сколько раз пользователь переплыл бассейн`

Программа возвращает информацию о тренировке в следующем виде:

`Тип тренировки: Swimming; Длительность: 1 ч.; Дистанция: 0.994 км; Ср. скорость: 1.0 км/ч; Потрачено ккал: 176.0.`

`Тип тренировки: Running; Длительность: 1 ч.; Дистанция: 9.75 км; Ср. скорость: 9.75 км/ч; Потрачено ккал: 11.662.`

`Тип тренировки: SportsWalking; Длительность: 1 ч.; Дистанция: 5.85 км; Ср. скорость: 5.85 км/ч; Потрачено ккал: 6.3.`

## Для запуска необходимо
- Python 3.7.6 и выше

## Как запустить
1. Клонируйте репозиторий  
`git clone https://github.com/Prple69/OOP_FitnessTracker.git`
2. Перейдите в папку репозитория  
`cd OOP_FitnessTracker`
3. Запустите файл `main.py`  
`python main.py`
