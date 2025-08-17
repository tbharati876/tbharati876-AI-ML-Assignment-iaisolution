from dialogue_agent_with_tools import DialogueAgentWithTools

def main():
    agent = DialogueAgentWithTools()
    print("Welcome to the XAgent-powered CLI. Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        response = agent.respond(query)
        print("Agent:", response)

if __name__ == "__main__":
    main()
