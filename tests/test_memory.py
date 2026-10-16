from app.memory import ConversationMemory


def test_add_user_and_model_messages():
    memory = ConversationMemory(max_turns=2)
    memory.add_user_message("hello")
    memory.add_model_message("hi")
    assert len(memory.get_history()) == 2
    assert memory.get_turn_count() == 1


def test_fifo_keeps_latest_turns():
    memory = ConversationMemory(max_turns=2)
    for i in range(1, 4):
        memory.add_user_message(f"user {i}")
        memory.add_model_message(f"model {i}")
        memory.prune_oldest_turn()

    history_text = [
        part.text
        for message in memory.get_history()
        for part in (message.parts or [])
    ]
    assert history_text == ["user 2", "model 2", "user 3", "model 3"]


def test_clear_memory():
    memory = ConversationMemory()
    memory.add_user_message("hello")
    memory.add_model_message("hi")
    memory.clear()
    assert memory.get_history() == []
    assert memory.get_turn_count() == 0


def test_empty_message_limit_is_rejected():
    try:
        ConversationMemory(max_turns=0)
    except ValueError:
        return
    assert False, "Expected ValueError"
