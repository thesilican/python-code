import random
def transform(t):
    # r = random.randint(1,3)
    # return hex(t) if r == 1 else bin(t) if r == 2 else str(t)

    # return "{0:02x}".format(t)
    return "{0:02x}".format(t)

text = "00111001 00111000 00110001 00110001 00110001 00110001 00110000 00111001"
nums = [transform(ord(x)) for x in text]
# rows = 8

# for i in range(0, len(nums), rows):
#     print(",".join(nums[i:i+rows]))
print(", ".join(nums))