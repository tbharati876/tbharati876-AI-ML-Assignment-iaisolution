from xagent_wrapper import XAgentWrapper
from tools import get_tools

class DialogueAgentWithTools:
    def __init__(self):
        self.agent = XAgentWrapper()
        self.tools = get_tools()

    def respond(self, query):
        return self.agent.run(query, tools=self.tools)
