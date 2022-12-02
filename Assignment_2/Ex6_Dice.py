import random

print("=========================================================")
print("   ***    Welcome to Dice Simmulator    ***")
print("=========================================================")

print("Roll the dice 🎲!")
dice_num = random.randint(1, 6)

if (dice_num == 6):
    print("🎲   ", dice_num)
    while(dice_num == 6):
        dice_num = random.randint(1, 6)
        print("     🎁 🎲   ",dice_num)

else:
    print("🎲   ",dice_num)