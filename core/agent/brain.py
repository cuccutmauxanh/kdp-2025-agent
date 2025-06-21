"""
AI Agent Brain - Core Intelligence Module
========================================

Đây là module trung tâm của AI agent, xử lý:
- Tư duy và ra quyết định
- Quản lý memory và knowledge
- Điều phối các tools
- Tích hợp với Obsidian Second Brain
"""

import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
import sys
import os

# Add tools directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from memory_query import MemoryQueryTool

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AgentBrain:
    """
    AI Agent Brain - Bộ não thông minh của agent
    
    Chức năng chính:
    1. Tư duy và ra quyết định
    2. Quản lý memory và knowledge
    3. Điều phối tools
    4. Tích hợp với Obsidian
    """
    
    def __init__(self, config_path: str = "config/agent_config.json"):
        """
        Khởi tạo Agent Brain
        
        Args:
            config_path: Đường dẫn đến file config
        """
        self.config = self._load_config(config_path)
        memory_path = self.config.get("memory", {}).get("path", "data/memory_bank")
        self.memory_bank = MemoryQueryTool(db_path=memory_path)
        self.obsidian_vault = None  # Sẽ tích hợp Obsidian
        self.tools = {}  # Dictionary các tools available
        self.conversation_history = []
        self.current_context = {}
        
        logger.info("🧠 Agent Brain đã được khởi tạo")
    
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration từ file JSON"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            logger.info(f"✅ Đã load config từ {config_path}")
            return config
        except FileNotFoundError:
            logger.warning(f"⚠️ Không tìm thấy config file {config_path}, sử dụng default")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Default configuration cho agent"""
        return {
            "agent_name": "KDP-2025-Agent",
            "version": "1.0.0",
            "memory": {
                "type": "chromadb",
                "path": "data/memory_bank"
            },
            "obsidian": {
                "vault_path": "vault",
                "auto_sync": True
            },
            "tools": {
                "enabled": ["obsidian_writer", "memory_query", "code_analyzer"]
            },
            "personality": {
                "style": "professional",
                "language": "vi",
                "tone": "helpful"
            }
        }
    
    def think(self, input_text: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Tư duy và ra quyết định dựa trên input
        
        Args:
            input_text: Input từ user
            context: Context bổ sung
            
        Returns:
            Dict chứa kết quả tư duy
        """
        logger.info(f"🧠 Brain đang tư duy về: {input_text[:50]}...")
        
        # Cập nhật context
        if context:
            self.current_context.update(context)
        
        # Phân tích input
        analysis = self._analyze_input(input_text)
        
        # Tìm kiếm knowledge liên quan
        relevant_knowledge = self._search_knowledge(analysis)
        
        # Ra quyết định
        decision = self._make_decision(analysis, relevant_knowledge)
        
        # Lưu vào conversation history
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "input": input_text,
            "analysis": analysis,
            "decision": decision
        })
        
        return {
            "analysis": analysis,
            "knowledge": relevant_knowledge,
            "decision": decision,
            "confidence": decision.get("confidence", 0.8)
        }
    
    def _analyze_input(self, input_text: str) -> Dict[str, Any]:
        """Phân tích input để hiểu ý định và context"""
        # TODO: Implement NLP analysis
        return {
            "intent": "general_query",
            "entities": [],
            "sentiment": "neutral",
            "complexity": "medium",
            "requires_tools": False
        }
    
    def _search_knowledge(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Tìm kiếm knowledge liên quan từ memory bank"""
        query_text = analysis.get("query") or analysis.get("intent") or ""
        if not query_text:
            return []
        results = self.memory_bank.query_knowledge(query_text, n_results=5)
        return results
    
    def _make_decision(self, analysis: Dict, knowledge: List[Dict]) -> Dict[str, Any]:
        """Ra quyết định dựa trên analysis và knowledge"""
        return {
            "action": "respond",
            "tools_needed": [],
            "response_type": "text",
            "confidence": 0.8
        }
    
    def execute_action(self, decision: Dict[str, Any], input_text: str) -> str:
        """
        Thực thi action dựa trên decision
        
        Args:
            decision: Kết quả từ think()
            input_text: Input gốc
            
        Returns:
            Response string
        """
        action = decision.get("action", "respond")
        
        if action == "respond":
            return self._generate_response(input_text, decision)
        elif action == "use_tool":
            return self._execute_tool(decision, input_text)
        else:
            return "Tôi chưa hiểu rõ yêu cầu của bạn."
    
    def _generate_response(self, input_text: str, decision: Dict) -> str:
        """Tạo response dựa trên input và decision, tổng hợp từ knowledge"""
        # Lấy knowledge từ decision hoặc từ self.memory_bank
        knowledge = decision.get("knowledge")
        if knowledge is None:
            knowledge = []
        if not knowledge:
            return "Tôi đã hiểu yêu cầu: {}. Hiện tại tôi chưa tìm thấy thông tin liên quan trong kho tri thức.".format(input_text)
        
        # Tổng hợp nội dung từ các document liên quan
        response_parts = []
        for i, doc in enumerate(knowledge):
            content = doc.get("content", "")
            source = doc.get("metadata", {}).get("source", "Unknown")
            # Lấy đoạn đầu tiên hoặc tóm tắt ngắn
            snippet = content.strip().split("\n")[0][:200]
            response_parts.append(f"[{i+1}] {snippet} (Nguồn: {source})")
        
        response = f"Tôi đã tìm thấy {len(knowledge)} thông tin liên quan:\n" + "\n".join(response_parts)
        response += "\n\nNếu bạn cần chi tiết hơn, hãy hỏi cụ thể hoặc yêu cầu trích dẫn đầy đủ."
        return response
    
    def _execute_tool(self, decision: Dict, input_text: str) -> str:
        """Thực thi tool cụ thể"""
        # TODO: Implement tool execution
        return "Tool execution placeholder"
    
    def learn(self, feedback: Dict[str, Any]) -> None:
        """
        Học từ feedback để cải thiện và ghi log vào Obsidian Vault
        
        Args:
            feedback: Feedback từ user hoặc system
        """
        logger.info("📚 Brain đang học từ feedback...")
        # TODO: Implement learning mechanism
        # Ghi log vào Obsidian Vault
        try:
            from tools.obsidian_writer import ObsidianWriter
            vault_path = self.config.get("obsidian", {}).get("vault_path", "vault")
            writer = ObsidianWriter(vault_path=vault_path)
            content = f"### Feedback học được\n{json.dumps(feedback, ensure_ascii=False, indent=2)}"
            writer.update_daily_log(content)
            logger.info("📝 Đã ghi log học tập vào Obsidian Vault!")
        except Exception as e:
            logger.warning(f"Không thể ghi log vào Obsidian Vault: {e}")
        pass
    
    def save_state(self, filepath: str = "data/brain_state.json") -> None:
        """Lưu trạng thái brain"""
        state = {
            "conversation_history": self.conversation_history,
            "current_context": self.current_context,
            "timestamp": datetime.now().isoformat()
        }
        
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        
        logger.info(f"💾 Đã lưu brain state vào {filepath}")
    
    def load_state(self, filepath: str = "data/brain_state.json") -> None:
        """Load trạng thái brain"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                state = json.load(f)
            
            self.conversation_history = state.get("conversation_history", [])
            self.current_context = state.get("current_context", {})
            logger.info(f"📂 Đã load brain state từ {filepath}")
        except FileNotFoundError:
            logger.warning(f"⚠️ Không tìm thấy brain state file {filepath}")


def main():
    """Test function cho Agent Brain"""
    brain = AgentBrain()
    
    # Test thinking
    result = brain.think("Xin chào, bạn có thể giúp tôi gì?")
    print("🧠 Brain thinking result:")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # Test action execution
    response = brain.execute_action(result, "Xin chào, bạn có thể giúp tôi gì?")
    print(f"\n💬 Response: {response}")
    
    # Save state
    brain.save_state()


if __name__ == "__main__":
    main() 