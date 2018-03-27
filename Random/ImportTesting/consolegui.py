from vpet import VPet

lePet = VPet(0)
print("Hello from " + __name__)
print("We have a " + str(type(lePet)) + " whose age is " + str(lePet.Age))
for i in range(int(input("Add how many years?\n>"))):
    lePet.tick()
print("Now the VPet is {} years old".format(lePet.Age))
