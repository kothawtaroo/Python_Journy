from msvcrt import getch

print("This is Sample Python Calculator.")
print("Please Enter First Numer.")
x = int(input())
print("Please Enter Second Numer.")
y = int(input())
z = x+y
print(f"Your Numer is {z}.")
print("Press any key to continue...")
_ = getch()
exit()