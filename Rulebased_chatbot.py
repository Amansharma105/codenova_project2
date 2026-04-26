print("----- Simple Chatbot -----")
print("Type bye to exit")

while True:

    user=input("You: ").lower()

    if user=="hello":
        print("Bot: Hi! Welcome.")

    elif user=="how are you":
        print("Bot: I am fine.")

    elif user=="python":
        print("Bot: Python is a programming language.")

    elif user=="course":
        print("Bot: Internship courses available.")

    elif user=="project":
        print("Bot: You can make chatbot or automation projects.")

    elif user=="bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
        