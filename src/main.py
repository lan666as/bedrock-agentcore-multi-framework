from bedrock_agentcore import BedrockAgentCoreApp

from src.app.agents.strands import strands_agent_bedrock

app = BedrockAgentCoreApp()


@app.entrypoint
def my_agent(request):
    return strands_agent_bedrock(request.get("prompt"))


app.run()
