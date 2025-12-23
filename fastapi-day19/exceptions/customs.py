class UserNotFoundError(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id

class ProductNotFoundError(Exception):
    def __init__(self, product_id: int):
        self.product_id = product_id        