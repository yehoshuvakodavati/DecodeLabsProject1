from app.llm import generate_reply
from app.memory import ConversationMemory


class Chatbot:
    def __init__(self, max_turns=5):
        self.memory = ConversationMemory(max_turns=max_turns)

    def chat(self, user_message):
        if not user_message or not user_message.strip():
            raise ValueError("Message cannot be empty.")

        # Prune before adding the new user message, keeping the request bounded.
        self.memory.prepare_for_new_turn()
        self.memory.add_user_message(user_message.strip())

        try:
            answer = generate_reply(self.memory.get_history())
        except Exception:
            # Avoid leaving an unmatched user message if the API call fails.
            if self.memory.history and self.memory.history[-1].role == "user":
                self.memory.history.pop()
            raise

        self.memory.add_model_message(answer)
        return answer

    def show_memory(self):
        self.memory.display()

    def clear_memory(self):
        self.memory.clear()
