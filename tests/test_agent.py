import sys
import os
import json
import shutil
import pytest

# Thêm core/agent và tools vào sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core', 'agent'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tools'))

from brain import AgentBrain
from memory_query import MemoryQueryTool
from obsidian_writer import ObsidianWriter

def test_agent_think_and_knowledge():
    brain = AgentBrain()
    result = brain.think("AI agent development là gì?")
    assert "knowledge" in result
    assert isinstance(result["knowledge"], list)
    assert len(result["knowledge"]) > 0
    print("✅ Agent truy vấn knowledge thành công!")

def test_agent_generate_response():
    brain = AgentBrain()
    result = brain.think("Cursor là gì?")
    response = brain.execute_action(result["decision"], "Cursor là gì?")
    assert "Cursor" in response or "thông tin liên quan" in response
    print("✅ Agent sinh câu trả lời tự nhiên!")

def test_obsidian_writer_log():
    # Test ghi log vào daily log
    vault_path = "vault"
    writer = ObsidianWriter(vault_path=vault_path)
    content = "Test log entry for agent."
    path = writer.update_daily_log(content)
    assert os.path.exists(path)
    print(f"✅ Ghi log vào Obsidian Vault thành công: {path}")

def test_agent_learn_log():
    brain = AgentBrain()
    feedback = {"user": "test", "message": "Agent học tốt!"}
    brain.learn(feedback)
    # Kiểm tra file daily log hôm nay
    today = __import__('datetime').datetime.now().strftime('%Y-%m-%d')
    log_path = os.path.join("vault", "03-DEVELOPMENT", "01-Current-Sprint", f"Daily-Log-{today}.md")
    assert os.path.exists(log_path)
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "Feedback học được" in content
    print("✅ Agent ghi log học tập vào Obsidian Vault thành công!")

if __name__ == "__main__":
    test_agent_think_and_knowledge()
    test_agent_generate_response()
    test_obsidian_writer_log()
    test_agent_learn_log()
    print("\n🎉 Tất cả test đã chạy xong!") 