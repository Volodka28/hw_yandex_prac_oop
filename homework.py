class InfoMessage:
    """
    Класс для создания сообщения о тренировке

    ...

    Атрибуты
    --------
    training_type: str
        тип тренировки
    duration: float
        продолжительность тренировки
    distance: float
        преодоленная дистанция
    speed: float
        средняя скорость
    calories: dloat
        сожженные калории

    Методы
    ------
    get_message():
        Возвращает сообщение о тренировке
    """

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        """Возвращает сообщение о тренировке"""

        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """
    Базовый класс тренировки

    ...

    Атрибуты
    --------
    LEN_STEP: float
        длина шага
    M_IN_KM: int
        коэффициент перевода метры в километры
    HOUR_TO_MINUTS: int
        перевод часов в минуты
    action: int
        количество шагов
    duration: float
        продолжительность тренировки
    weight: float
        вес спортсмена

    Методы
    ------
    get_distance()
        возвращает дистанцию в км
    get_mean_speed()
        возвращает среднюю скорость движения
    get_spent_calories()
        возвращает количество затраченных калорий
    show_training_info()
        возвращает информационное сообщение о выполненной тренировке
    """

    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    HOUR_TO_MINUTS = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """возвращает дистанцию в км."""

        return (self.action * self.LEN_STEP) / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """возвращает среднюю скорость движения."""

        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """возвращает количество затраченных калорий."""

        raise NotImplementedError

    def show_training_info(self) -> InfoMessage:
        """возвращает информационное сообщение о выполненной тренировке."""

        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """
    Класс Тренировка: Бег

    ...

    Атрибуты
    --------
    LEN_STEP: float
        длина шага
    M_IN_KM: int
        коэффициент перевода метры в километры
    COEFF_CALORIE_1: int
        коэффициент для расчёта калорий
    COEFF_CALORIE_2: int
        коэффициент для расчёта калорий
    HOUR_TO_MINUTS: int
        перевод часов в минуты
    action: int
        количество шагов
    duration: float
        продолжительность тренировки
    weight: float
        вес спортсмена

    Методы
    ------
    get_distance()
        возвращает дистанцию в км
    get_mean_speed()
        возвращает среднюю скорость движения
    get_spent_calories()
        возвращает количество затраченных калорий
    show_training_info()
        возвращает информационное сообщение о выполненной тренировке
    """

    COEFF_CALORIE_1 = 18
    COEFF_CALORIE_2 = 20

    def get_spent_calories(self) -> float:
        """Возвращает количество затраченных калорий."""

        return ((self.COEFF_CALORIE_1 * self.get_mean_speed()
                - self.COEFF_CALORIE_2)
                * self.weight / self.M_IN_KM * self.duration
                * self.HOUR_TO_MINUTS)


class SportsWalking(Training):
    """
    Класс Тренировка: Спортиваная ходьба

    ...

    Атрибуты
    --------
    LEN_STEP: float
        длина шага
    M_IN_KM: int
        коэффициент перевода метры в километры
    COEFF_CALORIE_1: int
        коэффициент для расчёта калорий
    COEFF_CALORIE_2: int
        коэффициент для расчёта калорий
    HOUR_TO_MINUTS: int
        перевод часов в минуты
    action: int
        количество шагов
    duration: float
        продолжительность тренировки
    weight: float
        вес спортсмена
    height: float
        рост спортсмена

    Методы
    ------
    get_distance()
        возвращает дистанцию в км
    get_mean_speed()
        возвращает среднюю скорость движения
    get_spent_calories()
        возвращает количество затраченных калорий
    show_training_info()
        возвращает информационное сообщение о выполненной тренировке
    """

    COEFF_CALORIE_1 = 0.035
    COEFF_CALORIE_2 = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """возвращает количество затраченных калорий."""

        return ((self.COEFF_CALORIE_1 * self.weight
                + (self.get_mean_speed() ** 2 // self.height)
                * self.COEFF_CALORIE_2 * self.weight)
                * self.duration * self.HOUR_TO_MINUTS)


class Swimming(Training):
    """
    Класс Тренировка: Спортиваная ходьба

    ...

    Атрибуты
    --------
    LEN_STEP: float
        длина шага
    M_IN_KM: int
        коэффициент перевода метры в километры
    COEFF_CALORIE_1: int
        коэффициент для расчёта калорий
    COEFF_CALORIE_2: int
        коэффициент для расчёта калорий
    action: int
        количество шагов
    duration: float
        продолжительность тренировки
    weight: float
        вес спортсмена
    length_pool: int
        длина бассейна в метрах
    count_pool: int
        сколько раз пользователь переплыл бассейн

    Методы
    ------
    get_distance()
        возвращает дистанцию в км
    get_mean_speed()
        возвращает среднюю скорость движения
    get_spent_calories()
        возвращает количество затраченных калорий
    show_training_info()
        возвращает информационное сообщение о выполненной тренировке
    """

    LEN_STEP = 1.38
    COEFF_CALORIE_1 = 1.1
    COEFF_CALORIE_2 = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """возвращает среднюю скорость движения."""

        return (self.length_pool * self.count_pool / self.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:
        """возвращает количество затраченных калорий."""

        return ((self.get_mean_speed() + self.COEFF_CALORIE_1)
                * self.COEFF_CALORIE_2 * self.weight)


def read_package(workout_type: str, data: list[int]) -> Training:
    """Прочитать данные полученные от датчиков."""

    dict_workout_type = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    return dict_workout_type[workout_type](*data)


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
