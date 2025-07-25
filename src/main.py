from bedrock_agentcore import BedrockAgentCoreApp

from src.app.agents.strands import strands_agent_bedrock

app = BedrockAgentCoreApp()


@app.entrypoint
def my_agent(payload):
    user_inquiry = payload.get("user_input", "Hello, how can I help you?")
    result = strands_agent_bedrock(user_inquiry)
    return {"result": result.message}


app.run()
