from chatbot import ask_question

while True:

    question = input("Ask: ")

    if question.lower() == "exit":
        break

    answer = ask_question(question)

    print("\nBot:", answer)