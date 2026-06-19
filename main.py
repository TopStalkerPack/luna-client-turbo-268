from dataclasses import dataclass
from typing import List
import requests
import json

@dataclass
class LunaMessage:
    id: int
    content: str

    def to_dict(self):
        return {'id': self.id, 'content': self.content}

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class LunaClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_messages(self) -> List[LunaMessage]:
        response = requests.get(f'{self.base_url}/messages')
        return [LunaMessage.from_dict(msg) for msg in response.json()]

    def send_message(self, message: LunaMessage):
        response = requests.post(f'{self.base_url}/messages', json=message.to_dict())
        if response.status_code != 200:
            raise Exception('Failed to send message')

def main():
    client = LunaClient('https://example.com/api')
    messages = client.get_messages()
    for msg in messages:
        print(f'Message {msg.id}: {msg.content}')
    new_msg = LunaMessage(1, 'Hello from luna-client-0000-c724')
    client.send_message(new_msg)

if __name__ == '__main__':
    main()