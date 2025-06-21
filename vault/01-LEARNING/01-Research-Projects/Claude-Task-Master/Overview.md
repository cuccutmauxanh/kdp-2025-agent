# {{title}}

## 📋 Tổng quan
- **Source**: 
- **Date**: {{date}}
- **Status**: [In Progress/Completed/Archived]

## 🎯 Mục tiêu nghiên cứu
# Phân tích Repository: Claude-Task-Master

## 📋 Tổng quan
- **Repository**: Claude-Task-Master
- **Type**: git
- **Date**: 2025-06-21
- **Status**: Completed

## 🎯 Mục tiêu nghiên cứu
Phân tích kiến trúc và patterns của Claude-Task-Master để áp dụng vào dự án KDP-2025-Agent

## 📚 Nội dung chính

### 1. README Analysis
# Task Master [![GitHub stars](https://img.shields.io/github/stars/eyaltoledano/claude-task-master?style=social)](https://github.com/eyaltoledano/claude-task-master/stargazers)

[![CI](https://github.com/eyaltoledano/claude-task-master/actions/workflows/ci.yml/badge.svg)](https://github.com/eyaltoledano/claude-task-master/actions/workflows/ci.yml) [![npm version](https://badge.fury.io/js/task-master-ai.svg)](https://badge.fury.io/js/task-master-ai) [![Discord](https://dcbadge.limes.pink/api/server/https://discord.gg/taskmasterai?style=flat)](https://discord.gg/taskmasterai) [![License: MIT with Commons Clause](https://img.shields.io/badge/license-MIT%20with%20Commons%20Clause-blue.svg)](LICENSE)

[![NPM Downloads](https://img.shields.io/npm/d18m/task-master-ai?style=flat)](https://www.npmjs.com/package/task-master-ai) [![NPM Downloads](https://img.shields.io/npm/dm/task-master-ai?style=flat)](https://www.npmjs.com/package/task-master-ai) [![NPM Downloads](https://img.shields.io/npm/dw/...

### 2. Project Structure
```
  📄 CHANGELOG.md
  📄 CONTRIBUTING.md
  📄 README-task-master.md
  📄 README.md
  📄 biome.json
  📄 index.js
  📄 jest.config.js
  📄 llms-install.md
  📄 mcp-test.js
  📄 output.json
  📁 .changeset/
    📄 README.md
    📄 config.json
  📁 .cursor/
    📄 mcp.json
    📁 rules/
  📁 .github/
    📁 ISSUE_TEMPLATE/
      📄 bug_report.md
      📄 enhancements---feature-requests.md
      📄 feedback.md
    📁 workflows/
      📄 ci.yml
      📄 pre-release.yml
      📄 release.yml
      📄 update-models-md.yml
  📁 .taskmaster/
    📄 config.json
    📄 state.json
    📁 docs/
      📄 README.md
      📄 prd.txt
      📄 task-template-importing-prd.txt
      📁 research/
        📄 2025-06-14_how-can-i-improve-the-scope-up-and-scope-down-comm.md
        📄 2025-06-14_should-i-be-using-any-specific-libraries-for-this.md
        📄 2025-06-14_test-save-functionality.md
        📄 2025-06-14_test-the-fix-for-duplicate-saves-final-test.md
    📁 reports/
      📄 task-complexity-report.json
      📄 task-complexity-report_test-prd-tag.json
    📁 tasks/
      📄 task_001_test-tag.txt
      📄 tasks.json
    📁 templates/
      📄 example_prd.txt
  📁 assets/
    📄 AGENTS.md
    📄 config.json
    📄 example_prd.txt
    📄 scripts_README.md
    📁 roocode/
      📁 .roo/
        📁 rules-architect/
        📁 rules-ask/
        📁 rules-boomerang/
        📁 rules-code/
        📁 rules-debug/
        📁 rules-test/
  📁 bin/
    📄 task-master.js
  📁 context/
    📄 MCP_INTEGRATION.md
    📄 fastmcp-core.txt
    📄 fastmcp-docs.txt
    📄 mcp-js-sdk-docs.txt
    📄 mcp-protocol-repo.txt
    📄 mcp-protocol-schema-03262025.json
    📄 mcp-protocol-spec.txt
    📁 chats/
      📄 add-task-dependencies-1.md
      📄 max-min-tokens.txt.md
  📁 docs/
    📄 README.md
    📄 command-reference.md
    📄 configuration.md
    📄 examples.md
    📄 licensing.md
    📄 migration-guide.md
    📄 models.md
    📄 task-structure.md
    📄 tutorial.md
    📁 contributor-docs/
      📄 testing-roo-integration.md
    📁 scripts/
      📄 models-json-to-markdown.js
  📁 mcp-server/
    📄 server.js
    📁 src/
      📄 index.js
      📄 logger.js
      📁 core/
        📄 context-manager.js
        📄 task-master-core.js
        📁 __tests__/
          📄 context-manager.test.js
        📁 direct-functions/
          📄 add-dependency.js
          📄 add-subtask.js
          📄 add-tag.js
          📄 add-task.js
          📄 analyze-task-complexity.js
          📄 cache-stats.js
          📄 clear-subtasks.js
          📄 complexity-report.js
          📄 copy-tag.js
          📄 create-tag-from-branch.js
        📁 utils/
          📄 env-utils.js
          📄 path-utils.js
      📁 tools/
        📄 add-dependency.js
        📄 add-subtask.js
        📄 add-tag.js
        📄 add-task.js
        📄 analyze.js
        📄 clear-subtasks.js
        📄 complexity-report.js
        📄 copy-tag.js
        📄 delete-tag.js
        📄 expand-all.js
  📁 scripts/
    📄 dev.js
    📄 init.js
    📄 task-complexity-report.json
    📄 test-claude-errors.js
    📄 test-claude.js
    📁 modules/
      📄 ai-services-unified.js
      📄 commands.js
      📄 config-manager.js
      📄 dependency-manager.js
      📄 index.js
      📄 rule-transformer.js
      📄 supported-models.json
      📄 sync-readme.js
      📄 task-manager.js
      📄 ui.js
      📁 task-manager/
        📄 add-subtask.js
        📄 add-task.js
        📄 analyze-task-complexity.js
        📄 clear-subtasks.js
        📄 expand-all-tasks.js
        📄 expand-task.js
        📄 find-next-task.js
        📄 generate-task-files.js
        📄 is-task-dependent.js
        📄 list-tasks.js
      📁 utils/
        📄 contextGatherer.js
        📄 fuzzyTaskSearch.js
        📄 git-utils.js
  📁 src/
    📁 ai-providers/
      📄 anthropic.js
      📄 azure.js
      📄 base-provider.js
      📄 bedrock.js
      📄 google-vertex.js
      📄 google.js
      📄 index.js
      📄 ollama.js
      📄 openai.js
      📄 openrouter.js
    📁 constants/
      📄 paths.js
      📄 task-status.js
    📁 utils/
      📄 getVersion.js
      📄 logger-utils.js
      📄 path-utils.js
  📁 tests/
    📄 README.md
    📄 setup.js
    📁 e2e/
    📁 fixture/
      📄 test-tasks.json
    📁 fixtures/
      📄 sample-claude-response.js
      📄 sample-prd.txt
      📄 sample-tasks.js
    📁 integration/
      📄 roo-files-inclusion.test.js
      📄 roo-init-functionality.test.js
      📁 cli/
        📄 commands.test.js
      📁 mcp-server/
        📄 direct-functions.test.js
    📁 unit/
      📄 ai-services-unified.test.js
      📄 commands.test.js
      📄 config-manager.test.js
      📄 dependency-manager.test.js
      📄 init.test.js
      📄 kebab-case-validation.test.js
      📄 parse-prd.test.js
      📄 roo-integration.test.js
      📄 rule-transformer.test.js
      📄 task-finder.test.js
      📁 mcp/
        📁 tools/
          📄 add-task.test.js
          📄 analyze-complexity.test.js
          📄 get-tasks.test.js
          📄 initialize-project.test.js
      📁 scripts/
        📁 modules/
          📁 task-manager/
            📄 add-subtask.test.js
            📄 add-task.test.js
            📄 analyze-task-complexity.test.js
            📄 clear-subtasks.test.js
            📄 find-next-task.test.js
            📄 generate-task-files.test.js
            📄 list-tasks.test.js
            📄 parse-prd.test.js
            📄 remove-subtask.test.js
            📄 set-task-status.test.js
```

### 3. Key Files Analysis

#### 1. llms-install.md (4880 chars)
```md
# Taskmaster AI Installation Guide

This guide helps AI assistants install and configure Taskmaster for users in their development projects.

## What is Taskmaster?

Taskmaster is an AI-driven task management system designed for development workflows. It helps break down projects into manageable tas...
```

#### 2. scripts\modules\task-manager\add-subtask.js (4796 chars)
```js
import path from 'path';

import { log, readJSON, writeJSON } from '../utils.js';
import { isTaskDependentOn } from '../task-manager.js';
import generateTaskFiles from './generate-task-files.js';

/**
 * Add a subtask to a parent task
 * @param {string} tasksPath - Path to the tasks.json file
 * @pa...
```

#### 3. scripts\modules\task-manager\find-next-task.js (4597 chars)
```js
import { log } from '../utils.js';
import { addComplexityToTask } from '../utils.js';

/**
 * Return the next work item:
 *   •  Prefer an eligible SUBTASK that belongs to any parent task
 *      whose own status is `in-progress`.
 *   •  If no such subtask exists, fall back to the best top-level ta...
```

#### 4. tests\unit\scripts\modules\task-manager\update-single-task-status.test.js (4569 chars)
```js
/**
 * Tests for the updateSingleTaskStatus function
 */
import { jest } from '@jest/globals';

// Import test fixtures
import {
	isValidTaskStatus,
	TASK_STATUS_OPTIONS
} from '../../../../../src/constants/task-status.js';

// Sample tasks data for testing
const sampleTasks = {
	tasks: [
		{
			id:...
```

#### 5. mcp-server\src\core\direct-functions\initialize-project.js (4563 chars)
```js
import { initializeProject } from '../../../../scripts/init.js'; // Import core function and its logger if needed separately
import {
	enableSilentMode,
	disableSilentMode
	// isSilentMode // Not used directly here
} from '../../../../scripts/modules/utils.js';
import os from 'os'; // Import os modu...
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