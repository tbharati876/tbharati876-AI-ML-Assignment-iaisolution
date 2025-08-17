from dialogue_agent_with_tools import DialogueAgentWithTools

def test_agent():
    agent = DialogueAgentWithTools()
    query = "What's the weather like in Paris?"
    response = agent.respond(query)
    assert isinstance(response, str)
    print("Test passed. Response:", response)

if __name__ == "__main__":
    test_agent()
