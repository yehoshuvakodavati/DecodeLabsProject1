from app.chatbot import Chatbot


def main():
    chatbot = Chatbot(max_turns=5)

    print("=" * 58)
    print("DecodeLabs — Custom AI Chatbot with Memory")
    print("Manual in-memory history | FIFO sliding window")
    print("=" * 58)
    print("Commands: /memory, /clear, /help, exit")
    print("Memory limit: 5 complete conversation turns\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        command = user_input.lower()

        if command in {"exit", "quit"}:
            print("Goodbye!")
            break
        if command == "/help":
            print("\nCommands:")
            print("  /memory  Show messages currently retained")
            print("  /clear   Clear this session's memory")
            print("  /help    Show commands")
            print("  exit     Quit the application\n")
            continue
        if command == "/memory":
            chatbot.show_memory()
            continue
        if command == "/clear":
            chatbot.clear_memory()
            print("Memory cleared.\n")
            continue
        if not user_input:
            print("Please enter a message. Empty input was not sent.\n")
            continue

        try:
            answer = chatbot.chat(user_input)
            print(f"\nAI: {answer}\n")
        except ValueError as exc:
            print(f"Input error: {exc}\n")
        except Exception as exc:
            print(f"Request failed: {exc}")
            print("Check your API key, model availability, network, and quota.\n")


if __name__ == "__main__":
    main()
