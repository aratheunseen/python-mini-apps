import json

with open('data.json', 'r') as file:
    content = file.read()

data = json.loads(content)
point = 0

for question in data:
    print(f"{question["question"]}")
    for option_id, option in enumerate(question["options"], 1):
        print(f"  {option_id}) {option}")

    user_choice = int(input(" Enter your answer: "))
    question["user_choice"] = user_choice
    if user_choice == question["correct_answer"]:
        point += 1

print(f"\nScore: {point} out of {len(data)}\n")

for question in data:
    print(f"{question["question"]}")
    print(f"  Your answer: {question["options"][question["user_choice"] - 1]}")
    print(f"  Correct answer: {question["options"][question["correct_answer"] - 1]}\n")