# v1.0 - My First Intelligent Contract by Rokon
# { "Depends": "py-genlayer:latest" }

from genlayer import *
import json
import time

class MyFirstIntelligentContract(gl.Contract):
    topics: TreeMap[str, str]
    xp: TreeMap[Address, u256]

    def __init__(self):
        self.topics = TreeMap()
        self.xp = TreeMap()

    @gl.public.write
    def create_topic(self) -> str:
        """AI generates a new fun topic"""
        topic_id = "topic_" + str(int(time.time()))

        def get_ai_topic():
            prompt = "Return only this exact JSON: {\"topic\": \"one short fun topic about AI or blockchain\"}"
            result = gl.nondet.exec_prompt(prompt)
            data = json.loads(result)
            return data["topic"]

        topic = gl.eq_principle.strict_eq(get_ai_topic)
        self.topics[topic_id] = topic
        return topic_id

    @gl.public.write
    def add_xp(self, amount: u256):
        sender = gl.message.sender_address
        if sender not in self.xp:
            self.xp[sender] = 0
        self.xp[sender] += amount

    @gl.public.view
    def get_topic(self, topic_id: str) -> str:
        return self.topics.get(topic_id, "Not found")

    @gl.public.view
    def get_my_xp(self) -> u256:
        sender = gl.message.sender_address
        return self.xp.get(sender, 0)
