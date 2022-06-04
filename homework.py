class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = format(duration, '.3f')
        self.distance = format(distance, '.3f')
        self.speed = format(speed, '.3f')
        self.calories = format(calories, '.3f')

    def get_message(self) -> str:
        message = (f"Тип тренировки: {self.training_type}; "
                   f"Длительность: {self.duration} ч.; "
                   f"Дистанция: {self.distance} км; "
                   f"Ср. скорость: {self.speed} км/ч; "
                   f"Потрачено ккал: {self.calories}.")
        return message


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.distance = self.get_distance()
        self.mean_speed = self.get_mean_speed()

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        self.distance = (self.action * self.LEN_STEP) / self.M_IN_KM
        return self.distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        self.mean_speed = self.distance / self.duration
        return self.mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        coeff_calorie_3 = 60
        spent_calories = ((coeff_calorie_1 * self.mean_speed - coeff_calorie_2)
                          * self.weight / self.M_IN_KM * self.duration
                          * coeff_calorie_3)
        self.spent_calories = spent_calories
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        coeff_calorie_3 = 60
        spent_calories = ((coeff_calorie_1 * self.weight
                          + (self.mean_speed ** 2 // self.height)
                          * coeff_calorie_2 * self.weight)
                          * self.duration * coeff_calorie_3)
        self.spent_calories = spent_calories
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int) -> None:
        self.length_pool = length_pool
        self.count_pool = count_pool
        super().__init__(action, duration, weight)

    def get_mean_speed(self) -> float:
        mean_speed = (self.length_pool * self.count_pool / self.M_IN_KM
                      / self.duration)
        self.mean_speed = mean_speed
        return mean_speed

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        spent_calories = ((self.mean_speed + coeff_calorie_1)
                          * coeff_calorie_2 * self.weight)
        self.spent_calories = spent_calories
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == "SWM":
        action = data[0]
        duration = data[1]
        weight = data[2]
        length_pool = data[3]
        count_pool = data[4]
        return Swimming(action=action,
                        duration=duration,
                        weight=weight,
                        length_pool=length_pool,
                        count_pool=count_pool)
    elif workout_type == "RUN":
        action = data[0]
        duration = data[1]
        weight = data[2]
        return Running(action=action,
                       duration=duration,
                       weight=weight)
    elif workout_type == "WLK":
        action = data[0]
        duration = data[1]
        weight = data[2]
        height = data[3]
        return SportsWalking(action=action,
                             duration=duration,
                             weight=weight,
                             height=height)
    else:
        return Training(15000, 1, 75)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    message = info.get_message()
    print(message)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
