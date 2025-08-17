from xagent import XAgent

class XAgentWrapper:
    def __init__(self, config=None):
        self.agent = XAgent(config=config)

    def run(self, query, tools=None):
        return self.agent.run(query, tools=tools)
