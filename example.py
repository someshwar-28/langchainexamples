from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get Weather for any city. """
    return f"Its always sunny in{city}"

agent = create_agent(
    model = "claude-sonnet-4-5",
    tools = [get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
answer = agent.invoke({"messages": [{"role":"user", "content": "what is the weather in phx"}]})
print(answer)
