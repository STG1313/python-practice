def is_valid_rating(rating):
    return type(rating) is int and 1 <= rating <= 5
