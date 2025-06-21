# {{title}}

## 📋 Tổng quan
- **Source**: 
- **Date**: {{date}}
- **Status**: [In Progress/Completed/Archived]

## 🎯 Mục tiêu nghiên cứu
# Phân tích Repository: Cursor-Best-Practices

## 📋 Tổng quan
- **Repository**: Cursor-Best-Practices
- **Type**: git
- **Date**: 2025-06-21
- **Status**: Completed

## 🎯 Mục tiêu nghiên cứu
Phân tích kiến trúc và patterns của Cursor-Best-Practices để áp dụng vào dự án KDP-2025-Agent

## 📚 Nội dung chính

### 1. README Analysis
# MDC Rules Generator

> **Disclaimer:** This project is not officially associated with or endorsed by Cursor. It is a community-driven initiative to enhance the Cursor experience.

<a href="https://www.producthunt.com/posts/cursor-rules-cli?embed=true&utm_source=badge-featured&utm_medium=badge&utm_souce=badge-cursor&#0045;rules&#0045;cli" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=936513&theme=light&t=1741030422709" alt="Cursor&#0032;Rules&#0032;CLI - Auto&#0045;install&#0032;relevant&#0032;Cursor&#0032;rules&#0032;with&#0032;one&#0032;simple&#0032;command | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

This project generates Cursor MDC (Markdown Cursor) rule files from a structured JSON file containing library information. It uses Exa for semantic search and LLM (Gemini) for content generation.

[![Star History Chart](https://api.star-history.com/svg?repos=sanjeed5/awesome-cursor-rules-mdc&type...

### 2. Project Structure
```
  📄 README.md
  📄 requirements.txt
  📄 rules.json
  📁 .cursor/
    📁 rules/
  📁 cursor-rules-cli/
    📄 PUBLISHING.md
    📄 README.md
    📄 RULES_JSON_README.md
    📄 rules.json
    📄 setup.py
    📁 src/
      📄 __init__.py
      📄 downloader.py
      📄 installer.py
      📄 main.py
      📄 matcher.py
      📄 scanner.py
      📄 utils.py
  📁 rules-mdc/
    📄 docker.md
    📄 vim.md
  📁 rules-v0-deprecated/
    📄 conversion_report.json
    📄 convert_to_mdc.py
    📄 test_conversion.py
    📁 android-jetpack-compose-cursorrules-prompt-file/
    📁 angular-novo-elements-cursorrules-prompt-file/
    📁 angular-typescript-cursorrules-prompt-file/
    📁 ascii-simulation-game-cursorrules-prompt-file/
    📁 astro-typescript-cursorrules-prompt-file/
    📁 chrome-extension-dev-js-typescript-cursorrules-pro/
    📁 code-guidelines-cursorrules-prompt-file/
    📁 convex-cursorrules-prompt-file/
    📁 cursor-ai-react-typescript-shadcn-ui-cursorrules-p/
    📁 cursorrules-cursor-ai-nextjs-14-tailwind-seo-setup/
    📁 cursorrules-cursor-ai-wordpress-draft-macos-prompt/
    📁 cursorrules-file-cursor-ai-python-fastapi-api/
    📁 deno-integration-techniques-cursorrules-prompt-fil/
    📁 dragonruby-best-practices-cursorrules-prompt-file/
    📁 elixir-engineer-guidelines-cursorrules-prompt-file/
    📁 elixir-phoenix-docker-setup-cursorrules-prompt-fil/
    📁 es-module-nodejs-guidelines-cursorrules-prompt-fil/
    📁 flutter-app-expert-cursorrules-prompt-file/
    📁 flutter-riverpod-cursorrules-prompt-file/
    📁 github-code-quality-cursorrules-prompt-file/
    📁 github-cursorrules-prompt-file-instructions/
    📁 go-backend-scalability-cursorrules-prompt-file/
    📁 go-servemux-rest-api-cursorrules-prompt-file/
    📁 graphical-apps-development-cursorrules-prompt-file/
    📁 html-tailwind-css-javascript-cursorrules-prompt-fi/
    📁 htmx-basic-cursorrules-prompt-file/
    📁 htmx-django-cursorrules-prompt-file/
    📁 htmx-flask-cursorrules-prompt-file/
    📁 htmx-go-basic-cursorrules-prompt-file/
    📁 htmx-go-fiber-cursorrules-prompt-file/
    📁 java-springboot-jpa-cursorrules-prompt-file/
    📁 javascript-astro-tailwind-css-cursorrules-prompt-f/
    📁 javascript-chrome-apis-cursorrules-prompt-file/
    📁 javascript-typescript-code-quality-cursorrules-pro/
    📁 knative-istio-typesense-gpu-cursorrules-prompt-fil/
    📁 kubernetes-mkdocs-documentation-cursorrules-prompt/
    📁 laravel-php-83-cursorrules-prompt-file/
    📁 laravel-tall-stack-best-practices-cursorrules-prom/
    📁 linux-nvidia-cuda-python-cursorrules-prompt-file/
    📁 next-type-llm/
    📁 nextjs-app-router-cursorrules-prompt-file/
    📁 nextjs-material-ui-tailwind-css-cursorrules-prompt/
    📁 nextjs-react-tailwind-cursorrules-prompt-file/
    📁 nextjs-react-typescript-cursorrules-prompt-file/
    📁 nextjs-seo-dev-cursorrules-prompt-file/
    📁 nextjs-supabase-shadcn-pwa-cursorrules-prompt-file/
    📁 nextjs-supabase-todo-app-cursorrules-prompt-file/
    📁 nextjs-tailwind-typescript-apps-cursorrules-prompt/
    📁 nextjs-typescript-app-cursorrules-prompt-file/
    📁 nextjs-typescript-cursorrules-prompt-file/
    📁 nextjs-typescript-tailwind-cursorrules-prompt-file/
    📁 nextjs-vercel-supabase-cursorrules-prompt-file/
    📁 nextjs-vercel-typescript-cursorrules-prompt-file/
    📁 nextjs15-react19-vercelai-tailwind-cursorrules-prompt-file/
    📁 nodejs-mongodb-cursorrules-prompt-file-tutorial/
    📁 nodejs-mongodb-jwt-express-react-cursorrules-promp/
    📁 optimize-dry-solid-principles-cursorrules-prompt-f/
    📁 optimize-rell-blockchain-code-cursorrules-prompt-f/
    📁 pandas-scikit-learn-guide-cursorrules-prompt-file/
    📁 plasticode-telegram-api-cursorrules-prompt-file/
    📁 py-fast-api/
    📁 pyqt6-eeg-processing-cursorrules-prompt-file/
    📁 python--typescript-guide-cursorrules-prompt-file/
    📁 python-312-fastapi-best-practices-cursorrules-prom/
    📁 python-containerization-cursorrules-prompt-file/
    📁 python-cursorrules-prompt-file-best-practices/
    📁 python-developer-cursorrules-prompt-file/
    📁 python-django-best-practices-cursorrules-prompt-fi/
    📁 python-fastapi-best-practices-cursorrules-prompt-f/
    📁 python-fastapi-cursorrules-prompt-file/
    📁 python-fastapi-scalable-api-cursorrules-prompt-fil/
    📁 python-flask-json-guide-cursorrules-prompt-file/
    📁 python-github-setup-cursorrules-prompt-file/
    📁 python-llm-ml-workflow-cursorrules-prompt-file/
    📁 python-projects-guide-cursorrules-prompt-file/
    📁 pytorch-scikit-learn-cursorrules-prompt-file/
    📁 qwik-basic-cursorrules-prompt-file/
    📁 qwik-tailwind-cursorrules-prompt-file/
    📁 react-chakra-ui-cursorrules-prompt-file/
    📁 react-components-creation-cursorrules-prompt-file/
    📁 react-graphql-apollo-client-cursorrules-prompt-file/
    📁 react-mobx-cursorrules-prompt-file/
    📁 react-native-expo-cursorrules-prompt-file/
    📁 react-native-expo-router-typescript-windows-cursorrules-prompt-file/
    📁 react-nextjs-ui-development-cursorrules-prompt-fil/
    📁 react-query-cursorrules-prompt-file/
    📁 react-redux-typescript-cursorrules-prompt-file/
    📁 react-styled-components-cursorrules-prompt-file/
    📁 react-typescript-nextjs-nodejs-cursorrules-prompt-/
    📁 react-typescript-symfony-cursorrules-prompt-file/
    📁 solidity-hardhat-cursorrules-prompt-file/
    📁 solidity-react-blockchain-apps-cursorrules-prompt-/
    📁 solidjs-basic-cursorrules-prompt-file/
    📁 solidjs-tailwind-cursorrules-prompt-file/
    📁 solidjs-typescript-cursorrules-prompt-file/
    📁 svelte-5-vs-svelte-4-cursorrules-prompt-file/
    📁 sveltekit-restful-api-tailwind-css-cursorrules-pro/
    📁 sveltekit-tailwindcss-typescript-cursorrules-promp/
    📁 sveltekit-typescript-guide-cursorrules-prompt-file/
    📁 swiftui-guidelines-cursorrules-prompt-file/
    📁 tailwind-css-nextjs-guide-cursorrules-prompt-file/
    📁 tailwind-react-firebase-cursorrules-prompt-file/
    📁 tailwind-shadcn-ui-integration-cursorrules-prompt-/
    📁 tauri-svelte-typescript-guide-cursorrules-prompt-f/
    📁 typescript-axios-cursorrules-prompt-file/
    📁 typescript-clasp-cursorrules-prompt-file/
    📁 typescript-code-convention-cursorrules-prompt-file/
    📁 typescript-expo-jest-detox-cursorrules-prompt-file/
    📁 typescript-llm-tech-stack-cursorrules-prompt-file/
    📁 typescript-nestjs-best-practices-cursorrules-promp/
    📁 typescript-nextjs-cursorrules-prompt-file/
    📁 typescript-nextjs-react-cursorrules-prompt-file/
    📁 typescript-nextjs-react-tailwind-supabase-cursorru/
    📁 typescript-nextjs-supabase-cursorrules-prompt-file/
    📁 typescript-nodejs-nextjs-ai-cursorrules-prompt-fil/
    📁 typescript-nodejs-nextjs-app-cursorrules-prompt-fi/
    📁 typescript-nodejs-nextjs-react-ui-css-cursorrules-/
    📁 typescript-nodejs-react-vite-cursorrules-prompt-fi/
    📁 typescript-react-cursorrules-prompt-file/
    📁 typescript-react-nextjs-cloudflare-cursorrules-pro/
    📁 typescript-react-nextui-supabase-cursorrules-promp/
    📁 typescript-shadcn-ui-nextjs-cursorrules-prompt-fil/
    📁 typescript-vite-tailwind-cursorrules-prompt-file/
    📁 typescript-vuejs-cursorrules-prompt-file/
    📁 typescript-zod-tailwind-nextjs-cursorrules-prompt-/
    📁 unity-cursor-ai-c-cursorrules-prompt-file/
    📁 vue-3-nuxt-3-development-cursorrules-prompt-file/
    📁 vue-3-nuxt-3-typescript-cursorrules-prompt-file/
    📁 vue3-composition-api-cursorrules-prompt-file/
    📁 web-app-optimization-cursorrules-prompt-file/
    📁 webassembly-z80-cellular-automata-cursorrules-prom/
    📁 wordpress-php-guzzle-gutenberg-cursorrules-prompt-/
  📁 src/
    📄 config.yaml
    📄 exa-example.py
    📄 generate_mdc_files.py
    📄 mdc-instructions.txt
    📄 mdc_generation_progress.json
    📄 plan.md
```

### 3. Key Files Analysis

#### 1. README.md (4907 chars)
```md
# MDC Rules Generator

> **Disclaimer:** This project is not officially associated with or endorsed by Cursor. It is a community-driven initiative to enhance the Cursor experience.

<a href="https://www.producthunt.com/posts/cursor-rules-cli?embed=true&utm_source=badge-featured&utm_medium=badge&utm_...
```

#### 2. rules-v0-deprecated\test_conversion.py (3912 chars)
```py
import os
from pathlib import Path
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_conversion_status(source_folder: str, output_folder: str) -> dict:
    """
    Analyze the conversion status by comparing sourc...
```

#### 3. cursor-rules-cli\README.md (3025 chars)
```md
# Cursor Rules CLI

> **Disclaimer:** This project is not officially associated with or endorsed by Cursor. It is a community-driven initiative to enhance the Cursor experience.

<a href="https://www.producthunt.com/posts/cursor-rules-cli?embed=true&utm_source=badge-featured&utm_medium=badge&utm_sou...
```

#### 4. src\exa-example.py (2982 chars)
```py
# Example file to give context to LLM on how to use Exa API

from exa_py import Exa
import os

exa = Exa(api_key=os.getenv("EXA_API_KEY"))

result = exa.answer("consumer AI startups that had breakthrough recently", text=True)
# text = false if we don't need to return webpage text for every citation ...
```

#### 5. cursor-rules-cli\setup.py (2457 chars)
```py
#!/usr/bin/env python
"""
Setup script for cursor-rules.
"""

from setuptools import setup, find_packages
import os
import shutil
from pathlib import Path

# Read version from __init__.py
with open(os.path.join("src", "__init__.py"), "r") as f:
    for line in f:
        if line.startswith("__versio...
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