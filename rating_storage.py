ratings = []


def save_rating(rating):
    if type(rating) is int and 1 <= rating <= 5:
        ratings.append(rating)
        return "Сохранено"
    return "Ошибка"
