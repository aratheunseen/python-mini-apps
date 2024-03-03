prompt = "Throw the coin and enter head and tail here: "

head = tail = 0

while True:

    with open("coin-flip.txt", 'r') as file:
        flips = file.readlines()

    flip = input("Throw the coin and enter head and tail here: ").lower() + '\n'
    flips.append(flip)

    with open("coin-flip.txt", 'w') as file:
        file.writelines(flips)

    heads_count = flips.count("head\n")
    percentage = heads_count / len(flips) * 100

    print(f"Probability of Head: {percentage}%")
