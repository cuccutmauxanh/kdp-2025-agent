# {{title}}

## 📋 Tổng quan
- **Source**: 
- **Date**: {{date}}
- **Status**: [In Progress/Completed/Archived]

## 🎯 Mục tiêu nghiên cứu
# Phân tích Repository: Archon

## 📋 Tổng quan
- **Repository**: Archon
- **Type**: git
- **Date**: 2025-06-21
- **Status**: Completed

## 🎯 Mục tiêu nghiên cứu
Phân tích kiến trúc và patterns của Archon để áp dụng vào dự án KDP-2025-Agent

## 📚 Nội dung chính

### 1. README Analysis
# Archon - AI Agent Builder

<img src="public/Archon.png" alt="Archon Logo" />

<div align="center" style="margin-top: 20px;margin-bottom: 30px">

<h3>🚀 **CURRENT VERSION** 🚀</h3>

**[ V6 - Tool Library and MCP Integration ]**
*Prebuilt tools, examples, and MCP server integration*

</div>

> **🔄 IMPORTANT UPDATE (March 31st)**: Archon now includes a library of prebuilt tools, examples, and MCP server integrations. Archon can now incorporate these resources when building new agents, significantly enhancing capabilities and reducing hallucinations. Note that the examples/tool library for Archon is just starting out. Please feel free to contribute examples, MCP servers, and prebuilt tools!

Archon is the world's first **"Agenteer"**, an AI agent designed to autonomously build, refine, and optimize other AI agents. 

It serves both as a practical tool for developers and as an educational framework demonstrating the evolution of agentic systems.
Archon will be developed in iterations, start...

### 2. Project Structure
```
  📄 README.md
  📄 graph_service.py
  📄 requirements.txt
  📄 run_docker.py
  📄 streamlit_ui.py
  📁 .github/
    📄 dependabot.yml
    📁 ISSUE_TEMPLATE/
      📄 bug_report.md
      📄 config.yml
      📄 feature_request.md
    📁 workflows/
      📄 build.yml
  📁 .streamlit/
  📁 agent-resources/
    📁 examples/
      📄 pydantic_github_agent.py
      📄 pydantic_mcp_agent.py
      📄 pydantic_web_search_agent.py
    📁 mcps/
      📄 airtable.json
      📄 brave_search.json
      📄 chroma.json
      📄 file_system.json
      📄 firecrawl.json
      📄 git.json
      📄 github.json
      📄 google_drive.json
      📄 qdrant.json
      📄 redis.json
    📁 tools/
      📄 get_github_file.py
      📄 get_github_file_structure.py
      📄 get_github_repo_info.py
      📄 web_search.py
  📁 archon/
    📄 __init__.py
    📄 advisor_agent.py
    📄 agent_prompts.py
    📄 agent_tools.py
    📄 archon_graph.py
    📄 crawl_pydantic_ai_docs.py
    📄 langgraph.json
    📄 pydantic_ai_coder.py
    📁 refiner_agents/
      📄 agent_refiner_agent.py
      📄 prompt_refiner_agent.py
      📄 tools_refiner_agent.py
  📁 iterations/
    📁 v1-single-agent/
      📄 README.md
      📄 crawl_pydantic_ai_docs.py
      📄 pydantic_ai_coder.py
      📄 requirements.txt
      📄 streamlit_ui.py
    📁 v2-agentic-workflow/
      📄 README.md
      📄 archon_graph.py
      📄 crawl_pydantic_ai_docs.py
      📄 langgraph.json
      📄 pydantic_ai_coder.py
      📄 requirements.txt
      📄 streamlit_ui.py
    📁 v3-mcp-support/
      📄 README.md
      📄 graph_service.py
      📄 mcp-config.json
      📄 mcp_server.py
      📄 requirements.txt
      📄 setup_mcp.py
      📄 streamlit_ui.py
      📁 archon/
        📄 __init__.py
        📄 archon_graph.py
        📄 crawl_pydantic_ai_docs.py
        📄 langgraph.json
        📄 pydantic_ai_coder.py
      📁 utils/
        📄 utils.py
    📁 v4-streamlit-ui-overhaul/
      📄 README.md
      📄 future_enhancements.py
      📄 graph_service.py
      📄 mcp_server.py
      📄 requirements.txt
      📄 run_docker.py
      📄 streamlit_ui.py
      📁 .streamlit/
      📁 archon/
        📄 __init__.py
        📄 archon_graph.py
        📄 crawl_pydantic_ai_docs.py
        📄 langgraph.json
        📄 pydantic_ai_coder.py
      📁 mcp/
        📄 mcp_server.py
        📄 requirements.txt
      📁 public/
      📁 utils/
        📄 utils.py
    📁 v5-parallel-specialized-agents/
      📄 README.md
      📄 graph_service.py
      📄 requirements.txt
      📄 run_docker.py
      📄 streamlit_ui.py
      📁 archon/
        📄 __init__.py
        📄 agent_prompts.py
        📄 agent_tools.py
        📄 archon_graph.py
        📄 crawl_pydantic_ai_docs.py
        📄 langgraph.json
        📄 pydantic_ai_coder.py
        📁 refiner_agents/
          📄 agent_refiner_agent.py
          📄 prompt_refiner_agent.py
          📄 tools_refiner_agent.py
      📁 mcp/
        📄 mcp_server.py
        📄 requirements.txt
      📁 public/
      📁 streamlit_pages/
        📄 __init__.py
        📄 agent_service.py
        📄 chat.py
        📄 database.py
        📄 documentation.py
        📄 environment.py
        📄 future_enhancements.py
        📄 intro.py
        📄 mcp.py
        📄 styles.py
      📁 utils/
        📄 utils.py
    📁 v6-tool-library-integration/
      📄 README.md
      📄 graph_service.py
      📄 requirements.txt
      📄 run_docker.py
      📄 streamlit_ui.py
      📁 agent-resources/
        📁 examples/
          📄 pydantic_github_agent.py
          📄 pydantic_mcp_agent.py
          📄 pydantic_web_search_agent.py
        📁 mcps/
          📄 airtable.json
          📄 brave_search.json
          📄 chroma.json
          📄 file_system.json
          📄 firecrawl.json
          📄 git.json
          📄 github.json
          📄 google_drive.json
          📄 qdrant.json
          📄 redis.json
        📁 tools/
          📄 get_github_file.py
          📄 get_github_file_structure.py
          📄 get_github_repo_info.py
          📄 web_search.py
      📁 archon/
        📄 __init__.py
        📄 advisor_agent.py
        📄 agent_prompts.py
        📄 agent_tools.py
        📄 archon_graph.py
        📄 crawl_pydantic_ai_docs.py
        📄 langgraph.json
        📄 pydantic_ai_coder.py
        📁 refiner_agents/
          📄 agent_refiner_agent.py
          📄 prompt_refiner_agent.py
          📄 tools_refiner_agent.py
      📁 mcp/
        📄 mcp_server.py
        📄 requirements.txt
      📁 public/
      📁 streamlit_pages/
        📄 __init__.py
        📄 agent_service.py
        📄 chat.py
        📄 database.py
        📄 documentation.py
        📄 environment.py
        📄 future_enhancements.py
        📄 intro.py
        📄 mcp.py
        📄 styles.py
      📁 utils/
        📄 utils.py
  📁 mcp/
    📄 mcp_server.py
    📄 requirements.txt
  📁 public/
  📁 streamlit_pages/
    📄 __init__.py
    📄 agent_service.py
    📄 chat.py
    📄 database.py
    📄 documentation.py
    📄 environment.py
    📄 future_enhancements.py
    📄 intro.py
    📄 mcp.py
    📄 styles.py
  📁 utils/
    📄 utils.py
```

### 3. Key Files Analysis

#### 1. archon\agent_tools.py (4968 chars)
```py
from typing import Dict, Any, List, Optional
from openai import AsyncOpenAI
from supabase import Client
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.utils import get_env_var

embedding_model = get_env_var('EMBEDDING_MODEL') or 'text-em...
```

#### 2. iterations\v6-tool-library-integration\archon\agent_tools.py (4968 chars)
```py
from typing import Dict, Any, List, Optional
from openai import AsyncOpenAI
from supabase import Client
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.utils import get_env_var

embedding_model = get_env_var('EMBEDDING_MODEL') or 'text-em...
```

#### 3. run_docker.py (4957 chars)
```py
#!/usr/bin/env python
"""
Simple script to build and run Archon Docker containers.
"""

import os
import subprocess
import platform
import time
from pathlib import Path

def run_command(command, cwd=None):
    """Run a command and print output in real-time."""
    print(f"Running: {' '.join(command)...
```

#### 4. iterations\v5-parallel-specialized-agents\run_docker.py (4957 chars)
```py
#!/usr/bin/env python
"""
Simple script to build and run Archon Docker containers.
"""

import os
import subprocess
import platform
import time
from pathlib import Path

def run_command(command, cwd=None):
    """Run a command and print output in real-time."""
    print(f"Running: {' '.join(command)...
```

#### 5. iterations\v6-tool-library-integration\run_docker.py (4957 chars)
```py
#!/usr/bin/env python
"""
Simple script to build and run Archon Docker containers.
"""

import os
import subprocess
import platform
import time
from pathlib import Path

def run_command(command, cwd=None):
    """Run a command and print output in real-time."""
    print(f"Running: {' '.join(command)...
```

## 💡 Key Insights
- [Cần phân tích thêm dựa trên nội dung]

## 🔗 Connections
- Related to: [[Agent Architecture]]
- Similar to: [[Tool Integration]]
- Builds on: [[Core Principles]]

## 📝 Implementation Ideas
- [Cần brainstorm thêm dựa trên patterns]

## ❓ Questions
- [Cần research thêm về implementation details]

## 📌 Tags
#research #learning #agent-architecture #{{name.lower().replace('-', '-')}}


## 📚 Nội dung chính
### 1. 
### 2. 
### 3. 

## 💡 Key Insights
- 

## 🔗 Connections
- Related to: 
- Similar to: 
- Builds on: 

## 📝 Implementation Ideas
- 

## ❓ Questions
- 

## 📌 Tags
#research #learning