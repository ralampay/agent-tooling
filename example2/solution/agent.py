import os
from typing import Any

from strands import Agent
from strands.models.openai import OpenAIModel
from tools import get_default_order_id, get_order_status


class ToolLogCallbackHandler:
    def __init__(self) -> None:
        self.tool_count = 0

    def __call__(self, **kwargs: Any) -> None:
        tool_use = (
            kwargs.get("event", {})
            .get("contentBlockStart", {})
            .get("start", {})
            .get("toolUse")
        )
        if tool_use:
            self.tool_count += 1
            tool_name = tool_use.get("name", "unknown")
            print(f"Tool #{self.tool_count}: {tool_name}")


class OrderAgent:
    def __init__(self):
        self.model = OpenAIModel(model_id="gpt-4o-mini")
        if os.getenv("OPENAI_API_KEY"):
            self.model = OpenAIModel(
                client_args={"api_key": os.getenv("OPENAI_API_KEY")},
                model_id="gpt-4o-mini",
            )

        self.agent = Agent(
            model=self.model,
            tools=[get_default_order_id, get_order_status],
            system_prompt=(
                "You are a simple order status agent.\n"
                "If the user provides an order ID, call get_order_status.\n"
                "If no order ID is provided, call get_default_order_id first,\n"
                "then pass that result to get_order_status.\n"
                "Do not invent order IDs."
            ),
            callback_handler=ToolLogCallbackHandler(),
        )

    def run(self, user_input: str):
        return self.agent(user_input)
