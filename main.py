
from dataclasses import dataclass

M_IN_KM = 1000

@dataclass
class Training():
    
    action: int = 1
    duration: float = 1
    weight: float = 1

    LEN_STEP = 0.65

    def get_distance(self) -> float:
        """Возвращает дистанцию (в километрах), которую преодолел пользователь за время тренировки."""
        return self.action * self.LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Возвращает значение средней скорости движения во время тренировки."""
        return self.get_distance() / self.duration 


    def get_spent_calories(self) -> float:
        """Возвращает количество килокалорий, израсходованных за время тренировки."""
        pass

    def show_training_info(self):
        """Передает информацию в класс InfoMessage."""
        return InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories()
        )

class Running(Training):
    """Тренировка - бег."""

    COEFF_CALORIE_1 = 18
    COEFF_CALORIE_2 = 20

    def get_spent_calories(self) -> float:
        """Возвращает количество килокалорий, израсходованных за время тренировки."""
        return (self.COEFF_CALORIE_1 * self.get_mean_speed() - self.COEFF_CALORIE_2) * self.weight / M_IN_KM * self.duration
    
@dataclass
class SportsWalking(Training):
    """Тренировка - спортивная ходьба."""
    
    height: int = 1

    COEFF_CALORIE_1 = 0.035
    COEFF_CALORIE_2 = 0.029

    def get_spent_calories(self) -> float:
        """Возвращает количество килокалорий, израсходованных за время тренировки."""
        return (self.COEFF_CALORIE_1 * self.height + (self.get_mean_speed()**2 // self.height) * self.COEFF_CALORIE_2 * self.height) * self.duration

@dataclass
class Swimming(Training):
    """Тренировка - плавание."""
    
    length_pool: float = 1
    count_pool: int = 1
    
    LEN_STEP_SWIMMING = 1.38

    COEFF_CALORIE_1 = 1.1
    COEFF_CALORIE_2 = 2

    def get_mean_speed(self) -> float:
        """Возвращает значение средней скорости движения во время тренировки."""
        return self.length_pool * self.count_pool / M_IN_KM / self.duration
    
    def get_spent_calories(self) -> float:
        """Возвращает количество килокалорий, израсходованных за время тренировки."""
        return (self.get_mean_speed() * self.COEFF_CALORIE_1) * self.COEFF_CALORIE_2 * self.weight
    
    def get_distance(self) -> float:
        """Возвращает дистанцию (в километрах), которую преодолел пользователь за время тренировки."""
        return self.action * self.LEN_STEP_SWIMMING / M_IN_KM

@dataclass
class InfoMessage():
    
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    RESPONSE = (
        'Тип тренировки: {training_type}; '
        'Длительность: {duration} ч.; '
        'Дистанция: {distance} км; ' 
        'Ср. скорость: {speed} км/ч; '
        'Потрачено ккал: {calories}.'
    )

    def get_info_message(self) ->str:
        """Возвращает информацию о тренировке."""
        return self.RESPONSE.format(
            training_type = self.training_type,
            duration = round(self.duration, 3),
            distance = round(self.distance, 3),
            speed = round(self.speed, 3),
            calories = round(self.calories, 3)
        )
    
def read_package(workout_type, data):
    """Возвращает класс тренировки с аргументами."""
    WORKOUT_DICT = {
    'RUN':Running,
    'WLK':SportsWalking,
    'SWM':Swimming,
    }
    return WORKOUT_DICT[workout_type](*data)

def main(training):
    info = training.show_training_info()
    print(info.get_info_message())

if __name__ == "__main__":

    packages = [        
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)