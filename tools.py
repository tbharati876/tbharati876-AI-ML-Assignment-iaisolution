def get_tools():
    return [
        {
            "name": "weather_tool",
            "description": "Provides weather information",
            "function": lambda location: f"The weather in {location} is sunny and 25°C."
        }
    ]
