print("========================================")
print("       CUSTOMER FEEDBACK ANALYZER")
print("========================================")

feedback = input("Enter customer feedback: ")

positive_words = [
    "good", "great", "excellent", "amazing",
    "happy", "love", "best", "satisfied",
    "fast", "helpful", "wonderful"
]

negative_words = [
    "bad", "poor", "worst", "hate",
    "slow", "unhappy", "terrible", "awful",
    "disappointed", "problem", "late"
]

words = feedback.lower().split()

positive_count = 0
negative_count = 0

positive_found = []
negative_found = []

for word in words:
    word = word.strip(".,!?")

    if word in positive_words:
        positive_count += 1
        positive_found.append(word)

    if word in negative_words:
        negative_count += 1
        negative_found.append(word)

print("\n----------------------------------------")
print("Customer Feedback:")
print(feedback)

print("\nPositive Words:", positive_count)
print("Negative Words:", negative_count)

if positive_count > negative_count:
    print("\nResult: POSITIVE 😊")
elif negative_count > positive_count:
    print("\nResult: NEGATIVE 😞")
else:
    print("\nResult: NEUTRAL 😐")

if positive_found:
    print("\nPositive words found:", ", ".join(positive_found))

if negative_found:
    print("Negative words found:", ", ".join(negative_found))

print("----------------------------------------")