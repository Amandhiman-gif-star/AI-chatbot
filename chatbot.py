print("🤖 AI Chatbot Started!")
print("Type 'exit' or 'bye' to stop the chatbot\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["exit", "bye", "byee", "bye bye", "goodbye"]:
        print("Chatbot: Bye! 👋 Have a productive day 😊")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you today?")

    elif "your name" in user_input:
        print("Chatbot: I am a simple AI-based Chatbot.")

    elif "how are you" in user_input:
        print("Chatbot: I'm doing great! Ready to help you 😄")

    elif "today plan" in user_input or "make my today plan" in user_input:
        print("\n📅 Chatbot: Here is your Today Plan:")
        print("🕕 6:00 AM - Wake up & freshen up")
        print("🧘 6:30 AM - Light exercise / walk")
        print("📚 7:30 AM - Study / Skill learning")
        print("🍽️ 9:30 AM - Breakfast")
        print("💻 10:00 AM - Practice coding / projects")
        print("🍛 1:00 PM - Lunch break")
        print("😴 2:00 PM - Short rest")
        print("📖 4:00 PM - Revision / Reading")
        print("🏃 6:00 PM - Relax / Walk")
        print("🍽️ 8:00 PM - Dinner")
        print("📝 9:00 PM - Light study / planning")
        print("😴 10:30 PM - Sleep\n")

    else:
        print("Chatbot: Sorry, I didn't understand that.")
