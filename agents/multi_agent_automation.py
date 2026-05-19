# 示例多 Agent 系统基础框架
import asyncio
from typing import List, Dict
import random

async def call_agent(agent_name: str, task: str) -> str:
    await asyncio.sleep(random.uniform(0.5, 1.5))
    return f"[{agent_name} 完成任务]: {task}"

class Agent:
    def __init__(self, name: str):
        self.name = name
        self.task_queue: List[str] = []

    def assign_task(self, task: str):
        self.task_queue.append(task)
        print(f"{self.name} 收到任务: {task}")

    async def run(self):
        results = []
        while self.task_queue:
            task = self.task_queue.pop(0)
            result = await call_agent(self.name, task)
            print(result)
            results.append(result)
        return results

class MultiAgentSystem:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}

    def add_agent(self, agent: Agent):
        self.agents[agent.name] = agent

    def assign_task_to_agent(self, agent_name: str, task: str):
        if agent_name in self.agents:
            self.agents[agent_name].assign_task(task)
        else:
            print(f"Agent {agent_name} 不存在")

    async def run_all(self):
        tasks = [agent.run() for agent in self.agents.values()]
        results = await asyncio.gather(*tasks)
        return results

async def main():
    system = MultiAgentSystem()
    system.add_agent(Agent("Agent A"))
    system.add_agent(Agent("Agent B"))
    system.assign_task_to_agent("Agent A", "任务 1")
    system.assign_task_to_agent("Agent B", "任务 2")
    all_results = await system.run_all()
    print(all_results)

if __name__ == "__main__":
    asyncio.run(main())