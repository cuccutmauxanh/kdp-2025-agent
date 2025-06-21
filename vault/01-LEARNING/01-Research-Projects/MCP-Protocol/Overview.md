# {{title}}

## 📋 Tổng quan
- **Source**: 
- **Date**: {{date}}
- **Status**: [In Progress/Completed/Archived]

## 🎯 Mục tiêu nghiên cứu
# Phân tích Repository: MCP-Protocol

## 📋 Tổng quan
- **Repository**: MCP-Protocol
- **Type**: git
- **Date**: 2025-06-21
- **Status**: Completed

## 🎯 Mục tiêu nghiên cứu
Phân tích kiến trúc và patterns của MCP-Protocol để áp dụng vào dự án KDP-2025-Agent

## 📚 Nội dung chính

### 1. README Analysis
# MCP Python SDK

<div align="center">

<strong>Python implementation of the Model Context Protocol (MCP)</strong>

[![PyPI][pypi-badge]][pypi-url]
[![MIT licensed][mit-badge]][mit-url]
[![Python Version][python-badge]][python-url]
[![Documentation][docs-badge]][docs-url]
[![Specification][spec-badge]][spec-url]
[![GitHub Discussions][discussions-badge]][discussions-url]

</div>

<!-- omit in toc -->
## Table of Contents

- [MCP Python SDK](#mcp-python-sdk)
  - [Overview](#overview)
  - [Installation](#installation)
    - [Adding MCP to your python project](#adding-mcp-to-your-python-project)
    - [Running the standalone MCP development tools](#running-the-standalone-mcp-development-tools)
  - [Quickstart](#quickstart)
  - [What is MCP?](#what-is-mcp)
  - [Core Concepts](#core-concepts)
    - [Server](#server)
    - [Resources](#resources)
    - [Tools](#tools)
    - [Prompts](#prompts)
    - [Images](#images)
    - [Context](#context)
    - [Completions](#completions)
    - [Elicitat...

### 2. Project Structure
```
  📄 .pre-commit-config.yaml
  📄 CLAUDE.md
  📄 CODE_OF_CONDUCT.md
  📄 CONTRIBUTING.md
  📄 README.md
  📄 RELEASE.md
  📄 SECURITY.md
  📄 mkdocs.yml
  📁 .github/
    📁 ISSUE_TEMPLATE/
      📄 bug.yaml
      📄 config.yaml
      📄 feature-request.yaml
      📄 question.yaml
    📁 workflows/
      📄 main-checks.yml
      📄 publish-docs-manually.yml
      📄 publish-pypi.yml
      📄 pull-request-checks.yml
      📄 shared.yml
  📁 docs/
    📄 api.md
    📄 index.md
  📁 examples/
    📄 README.md
    📁 clients/
      📁 simple-auth-client/
        📄 README.md
        📁 mcp_simple_auth_client/
          📄 __init__.py
          📄 main.py
      📁 simple-chatbot/
        📁 mcp_simple_chatbot/
          📄 main.py
          📄 requirements.txt
          📄 servers_config.json
    📁 fastmcp/
      📄 complex_inputs.py
      📄 desktop.py
      📄 echo.py
      📄 memory.py
      📄 parameter_descriptions.py
      📄 readme-quickstart.py
      📄 screenshot.py
      📄 simple_echo.py
      📄 text_me.py
      📄 unicode_example.py
    📁 servers/
      📁 simple-auth/
        📄 README.md
        📁 mcp_simple_auth/
          📄 __init__.py
          📄 __main__.py
          📄 server.py
      📁 simple-prompt/
        📄 README.md
        📁 mcp_simple_prompt/
          📄 __init__.py
          📄 __main__.py
          📄 server.py
      📁 simple-resource/
        📄 README.md
        📁 mcp_simple_resource/
          📄 __init__.py
          📄 __main__.py
          📄 server.py
      📁 simple-streamablehttp-stateless/
        📄 README.md
        📁 mcp_simple_streamablehttp_stateless/
          📄 __init__.py
          📄 __main__.py
          📄 server.py
      📁 simple-streamablehttp/
        📄 README.md
        📁 mcp_simple_streamablehttp/
          📄 __init__.py
          📄 __main__.py
          📄 event_store.py
          📄 server.py
      📁 simple-tool/
        📄 README.md
        📁 mcp_simple_tool/
          📄 __init__.py
          📄 __main__.py
          📄 server.py
  📁 src/
    📁 mcp/
      📄 __init__.py
      📄 types.py
      📁 cli/
        📄 __init__.py
        📄 claude.py
        📄 cli.py
      📁 client/
        📄 __init__.py
        📄 __main__.py
        📄 auth.py
        📄 session.py
        📄 session_group.py
        📄 sse.py
        📄 streamable_http.py
        📄 websocket.py
        📁 stdio/
          📄 __init__.py
          📄 win32.py
      📁 server/
        📄 __init__.py
        📄 __main__.py
        📄 elicitation.py
        📄 models.py
        📄 session.py
        📄 sse.py
        📄 stdio.py
        📄 streamable_http.py
        📄 streamable_http_manager.py
        📄 streaming_asgi_transport.py
        📁 auth/
          📄 __init__.py
          📄 errors.py
          📄 json_response.py
          📄 provider.py
          📄 routes.py
          📄 settings.py
          📁 handlers/
            📄 __init__.py
            📄 authorize.py
            📄 metadata.py
            📄 register.py
            📄 revoke.py
            📄 token.py
          📁 middleware/
            📄 __init__.py
            📄 auth_context.py
            📄 bearer_auth.py
            📄 client_auth.py
        📁 fastmcp/
          📄 __init__.py
          📄 exceptions.py
          📄 server.py
          📁 prompts/
            📄 __init__.py
            📄 base.py
            📄 manager.py
            📄 prompt_manager.py
          📁 resources/
            📄 __init__.py
            📄 base.py
            📄 resource_manager.py
            📄 templates.py
            📄 types.py
          📁 tools/
            📄 __init__.py
            📄 base.py
            📄 tool_manager.py
          📁 utilities/
            📄 __init__.py
            📄 func_metadata.py
            📄 logging.py
            📄 types.py
        📁 lowlevel/
          📄 __init__.py
          📄 helper_types.py
          📄 server.py
      📁 shared/
        📄 __init__.py
        📄 _httpx_utils.py
        📄 auth.py
        📄 context.py
        📄 exceptions.py
        📄 memory.py
        📄 message.py
        📄 metadata_utils.py
        📄 progress.py
        📄 session.py
  📁 tests/
    📄 __init__.py
    📄 conftest.py
    📄 test_examples.py
    📄 test_types.py
    📁 client/
      📄 __init__.py
      📄 conftest.py
      📄 test_auth.py
      📄 test_config.py
      📄 test_list_methods_cursor.py
      📄 test_list_roots_callback.py
      📄 test_logging_callback.py
      📄 test_resource_cleanup.py
      📄 test_sampling_callback.py
      📄 test_session.py
    📁 issues/
      📄 test_100_tool_listing.py
      📄 test_129_resource_templates.py
      📄 test_141_resource_templates.py
      📄 test_152_resource_mime_type.py
      📄 test_176_progress_token.py
      📄 test_188_concurrency.py
      📄 test_192_request_id.py
      📄 test_342_base64_encoding.py
      📄 test_355_type_error.py
      📄 test_88_random_error.py
    📁 server/
      📄 __init__.py
      📄 test_completion_with_context.py
      📄 test_lifespan.py
      📄 test_lowlevel_tool_annotations.py
      📄 test_read_resource.py
      📄 test_session.py
      📄 test_sse_security.py
      📄 test_stdio.py
      📄 test_streamable_http_manager.py
      📄 test_streamable_http_security.py
      📁 auth/
        📄 test_error_handling.py
        📁 middleware/
          📄 test_auth_context.py
          📄 test_bearer_auth.py
      📁 fastmcp/
        📄 __init__.py
        📄 test_elicitation.py
        📄 test_func_metadata.py
        📄 test_integration.py
        📄 test_parameter_descriptions.py
        📄 test_server.py
        📄 test_title.py
        📄 test_tool_manager.py
        📁 auth/
          📄 __init__.py
          📄 test_auth_integration.py
        📁 prompts/
          📄 __init__.py
          📄 test_base.py
          📄 test_manager.py
        📁 resources/
          📄 __init__.py
          📄 test_file_resources.py
          📄 test_function_resources.py
          📄 test_resource_manager.py
          📄 test_resource_template.py
          📄 test_resources.py
        📁 servers/
          📄 __init__.py
          📄 test_file_server.py
    📁 shared/
      📄 test_httpx_utils.py
      📄 test_memory.py
      📄 test_progress_notifications.py
      📄 test_session.py
      📄 test_sse.py
      📄 test_streamable_http.py
      📄 test_ws.py
```

### 3. Key Files Analysis

#### 1. src\mcp\cli\claude.py (4949 chars)
```py
"""Claude app integration utilities."""

import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any

from mcp.server.fastmcp.utilities.logging import get_logger

logger = get_logger(__name__)

MCP_PACKAGE = "mcp[cli]"


def get_claude_config_path() -> Path | None:...
```

#### 2. tests\issues\test_152_resource_mime_type.py (4927 chars)
```py
import base64

import pytest
from pydantic import AnyUrl

from mcp import types
from mcp.server.fastmcp import FastMCP
from mcp.server.lowlevel import Server
from mcp.server.lowlevel.helper_types import ReadResourceContents
from mcp.shared.memory import (
    create_connected_server_and_client_sessi...
```

#### 3. tests\issues\test_141_resource_templates.py (4795 chars)
```py
import pytest
from pydantic import AnyUrl

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as client_session,
)
from mcp.types import (
    ListResourceTemplatesResult,
    TextResourceContents,
)


@pytest.mark.anyio
async def te...
```

#### 4. tests\client\conftest.py (4788 chars)
```py
from contextlib import asynccontextmanager
from unittest.mock import patch

import pytest

import mcp.shared.memory
from mcp.shared.message import SessionMessage
from mcp.types import (
    JSONRPCNotification,
    JSONRPCRequest,
)


class SpyMemoryObjectSendStream:
    def __init__(self, original_...
```

#### 5. src\mcp\server\transport_security.py (4657 chars)
```py
"""DNS rebinding protection for MCP server transports."""

import logging

from pydantic import BaseModel, Field
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger(__name__)


class TransportSecuritySettings(BaseModel):
    """Settings for MCP...
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