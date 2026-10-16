from google.genai import types


class ConversationMemory:
    """In-memory chat history with FIFO pruning by complete turns."""

    def __init__(self, max_turns=5):
        if max_turns < 1:
            raise ValueError("max_turns must be at least 1.")
        self.max_turns = max_turns
        self.history = []

    def add_user_message(self, text):
        self.history.append(
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=text)],
            )
        )

    def add_model_message(self, text):
        self.history.append(
            types.Content(
                role="model",
                parts=[types.Part.from_text(text=text)],
            )
        )

    def prune_oldest_turn(self):
        # History is stored as user/model pairs.
        while len(self.history) > self.max_turns * 2:
            del self.history[:2]

    def prepare_for_new_turn(self):
        # Reserve room for the next user/model exchange.
        while len(self.history) >= self.max_turns * 2:
            del self.history[:2]

    def get_history(self):
        # Return a copy so callers can't accidentally mutate internal state.
        return list(self.history)

    def get_turn_count(self):
        return len(self.history) // 2

    def clear(self):
        self.history.clear()

    def display(self):
        if not self.history:
            print("\nMemory is empty.\n")
            return

        print("\n" + "=" * 58)
        print("CURRENT CONVERSATION MEMORY")
        print("=" * 58)
        for index, item in enumerate(self.history, start=1):
            role = (item.role or "unknown").upper()
            text = " ".join(part.text or "" for part in (item.parts or []))
            print(f"{index}. {role}: {text}")
        print("-" * 58)
        print(f"Turns stored: {self.get_turn_count()}/{self.max_turns}")
        print("=" * 58 + "\n")
