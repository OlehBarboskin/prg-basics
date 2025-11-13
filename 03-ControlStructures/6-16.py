total_washing_time = 0

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

time = 0
washing_product = ""
rinse = True
spin = False

if program == "j":
    washing_product = "jacket"
    time += 40
elif program == "u":
    washing_product = "underwear"
    time += 70
elif program == "s":
    washing_product = "shoes"
    time += 20
else:
    print("Error")

if extra_rinse == "y":
    rinse = True
    time += 15
else:
    rinse = False
if extra_spin == "y":
    spin = True
    time += 9
else:
    spin = False


print(f"mode: {washing_product}, rinse: {rinse}, extra_spin: {spin}, time: {time}")