class VPet:

    def __init__(self, initial_age: int):
        self.Age = initial_age

    def tick(self):
        self.Age += 1


if __name__ == "__main__":
    # This should do all the work
    import consolegui
