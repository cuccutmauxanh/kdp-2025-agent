# {{title}}

## 📋 Tổng quan
- **Source**: 
- **Date**: {{date}}
- **Status**: [In Progress/Completed/Archived]

## 🎯 Mục tiêu nghiên cứu
# Phân tích Repository: Agent-Zero

## 📋 Tổng quan
- **Repository**: Agent-Zero
- **Type**: git
- **Date**: 2025-06-21
- **Status**: Completed

## 🎯 Mục tiêu nghiên cứu
Phân tích kiến trúc và patterns của Agent-Zero để áp dụng vào dự án KDP-2025-Agent

## 📚 Nội dung chính

### 1. README Analysis
<div align="center">

# `Agent Zero`


[![Agent Zero Website](https://img.shields.io/badge/Website-agent--zero.ai-0A192F?style=for-the-badge&logo=vercel&logoColor=white)](https://agent-zero.ai) [![Thanks to Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Thanks%20to%20Sponsors-FF69B4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/frdel) [![Follow on X](https://img.shields.io/badge/X-Follow-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/Agent0ai) [![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AgentZeroFW) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com...

### 2. Project Structure
```
  📄 README.md
  📄 agent.py
  📄 initialize.py
  📄 jsconfig.json
  📄 models.py
  📄 preload.py
  📄 prepare.py
  📄 requirements.txt
  📄 run_cli.py
  📄 run_tunnel.py
  📁 .github/
    📄 FUNDING.yml
  📁 docker/
    📁 base/
      📄 build.txt
      📁 fs/
        📁 etc/
          📁 searxng/
            📄 settings.yml
        📁 ins/
    📁 run/
      📄 build.txt
      📄 docker-compose.yml
      📁 fs/
        📁 etc/
          📁 nginx/
          📁 searxng/
            📄 settings.yml
          📁 supervisor/
            📁 conf.d/
        📁 exe/
          📄 node_eval.js
          📄 supervisor_event_listener.py
        📁 ins/
        📁 per/
          📁 root/
  📁 docs/
    📄 README.md
    📄 architecture.md
    📄 contribution.md
    📄 cuda_docker_setup.md
    📄 installation.md
    📄 mcp_setup.md
    📄 quickstart.md
    📄 troubleshooting.md
    📄 tunnel.md
    📄 usage.md
    📁 res/
      📁 a0-vector-graphics/
      📁 setup/
        📁 settings/
  📁 instruments/
    📁 custom/
    📁 default/
      📁 yt_download/
        📄 download_video.py
        📄 yt_download.md
  📁 knowledge/
    📁 custom/
      📁 main/
      📁 solutions/
    📁 default/
      📁 main/
        📁 about/
          📄 github_readme.md
          📄 installation.md
      📁 solutions/
  📁 lib/
    📁 browser/
      📄 click.js
      📄 extract_dom.js
      📄 init_override.js
  📁 logs/
  📁 memory/
  📁 prompts/
    📁 default/
      📄 agent.context.extras.md
      📄 agent.system.behaviour.md
      📄 agent.system.behaviour_default.md
      📄 agent.system.datetime.md
      📄 agent.system.instruments.md
      📄 agent.system.main.communication.md
      📄 agent.system.main.environment.md
      📄 agent.system.main.md
      📄 agent.system.main.role.md
      📄 agent.system.main.solving.md
    📁 hacker/
      📄 agent.system.main.environment.md
      📄 agent.system.main.role.md
    📁 research_agent/
      📄 agent.system.main.communication.md
      📄 agent.system.main.deep_research.md
      📄 agent.system.main.environment.md
      📄 agent.system.main.md
      📄 agent.system.main.role.md
  📁 python/
    📄 __init__.py
    📁 api/
      📄 chat_export.py
      📄 chat_load.py
      📄 chat_remove.py
      📄 chat_reset.py
      📄 ctx_window_get.py
      📄 delete_work_dir_file.py
      📄 download_work_dir_file.py
      📄 file_info.py
      📄 get_work_dir_files.py
      📄 health.py
    📁 extensions/
      📁 message_loop_end/
        📄 _10_organize_history.py
        📄 _90_save_chat.py
      📁 message_loop_prompts_after/
        📄 _50_recall_memories.py
        📄 _51_recall_solutions.py
        📄 _60_include_current_datetime.py
        📄 _91_recall_wait.py
      📁 message_loop_prompts_before/
        📄 _90_organize_history_wait.py
      📁 message_loop_start/
        📄 _10_iteration_no.py
      📁 monologue_end/
        📄 _50_memorize_fragments.py
        📄 _51_memorize_solutions.py
        📄 _90_waiting_for_input_msg.py
      📁 monologue_start/
        📄 _60_rename_chat.py
      📁 response_stream/
        📄 _10_log_from_stream.py
        📄 _20_live_response.py
      📁 system_prompt/
        📄 _10_system_prompt.py
        📄 _20_behaviour_prompt.py
    📁 helpers/
      📄 api.py
      📄 attachment_manager.py
      📄 browser.py
      📄 browser_use.py
      📄 call_llm.py
      📄 crypto.py
      📄 defer.py
      📄 dirty_json.py
      📄 docker.py
      📄 document_query.py
    📁 tools/
      📄 behaviour_adjustment.py
      📄 browser_agent.py
      📄 call_subordinate.py
      📄 code_execution_tool.py
      📄 document_query.py
      📄 input.py
      📄 knowledge_tool.py
      📄 memory_delete.py
      📄 memory_forget.py
      📄 memory_load.py
  📁 tmp/
  📁 webui/
    📄 index.js
    📁 components/
      📁 settings/
        📁 mcp/
          📁 client/
            📄 mcp-servers-store.js
          📁 server/
    📁 css/
    📁 js/
      📄 AlpineStore.js
      📄 alpine.min.js
      📄 api.js
      📄 components.js
      📄 file_browser.js
      📄 history.js
      📄 image_modal.js
      📄 initFw.js
      📄 messages.js
      📄 modal.js
    📁 public/
```

### 3. Key Files Analysis

#### 1. python\helpers\docker.py (4840 chars)
```py
import time
import docker
import atexit
from typing import Optional
from python.helpers.files import get_abs_path
from python.helpers.errors import format_error
from python.helpers.print_style import PrintStyle
from python.helpers.log import Log

class DockerContainerManager:
    def __init__(self, ...
```

#### 2. python\extensions\monologue_end\_51_memorize_solutions.py (4784 chars)
```py
import asyncio
from python.helpers.extension import Extension
from python.helpers.memory import Memory
from python.helpers.dirty_json import DirtyJson
from agent import LoopData
from python.helpers.log import LogItem


class MemorizeSolutions(Extension):

    REPLACE_THRESHOLD = 0.9

    async def e...
```

#### 3. python\helpers\localization.py (4784 chars)
```py
from datetime import datetime
import pytz  # type: ignore

from python.helpers.print_style import PrintStyle
from python.helpers.dotenv import get_dotenv_value, save_dotenv_value


class Localization:
    """
    Localization class for handling timezone conversions between UTC and local time.
    ""...
```

#### 4. python\helpers\strings.py (4576 chars)
```py
import re
import sys
import time

def sanitize_string(s: str, encoding: str = "utf-8") -> str:
    # Replace surrogates and invalid unicode with replacement character
    if not isinstance(s, str):
        s = str(s)
    return s.encode(encoding, 'replace').decode(encoding, 'replace')

def calculate...
```

#### 5. python\api\poll.py (4371 chars)
```py
import time
from datetime import datetime
from python.helpers.api import ApiHandler
from flask import Request, Response

from agent import AgentContext

from python.helpers import persist_chat
from python.helpers.task_scheduler import TaskScheduler
from python.helpers.localization import Localizatio...
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