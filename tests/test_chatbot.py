from unittest.mock import patch
from app.chatbot import Chatbot


def test_chat_stores_user_and_model_messages():
    bot = Chatbot(max_turns=3)
    with patch("app.chatbot.generate_reply", return_value="Hello there"):
        answer = bot.chat("Hi")
    assert answer == "Hello there"
    history = bot.memory.get_history()
    assert len(history) == 2
    assert history[0].role == "user"
    assert history[1].role == "model"


def test_blank_input_does_not_call_model():
    bot = Chatbot()
    with patch("app.chatbot.generate_reply") as mocked:
        try:
            bot.chat("   ")
        except ValueError:
            pass
        else:
            assert False, "Expected ValueError"
        mocked.assert_not_called()
