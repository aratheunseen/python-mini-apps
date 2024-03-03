from datetime import datetime
dt = datetime.now().strftime("%Y%m%d_%H%M%S")

mood = input("Rate your mood 1 to 5: ")
thoughts = input("Whats on your mind now?\n")

with open(f"{dt}_{mood}.txt","w") as file:
    file.writelines(thoughts)