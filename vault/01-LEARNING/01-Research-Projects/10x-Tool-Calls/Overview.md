# {{title}}

## 📋 Tổng quan
- **Source**: 
- **Date**: {{date}}
- **Status**: [In Progress/Completed/Archived]

## 🎯 Mục tiêu nghiên cứu
# Phân tích Repository: 10x-Tool-Calls

## 📋 Tổng quan
- **Repository**: 10x-Tool-Calls
- **Type**: git
- **Date**: 2025-06-21
- **Status**: Completed

## 🎯 Mục tiêu nghiên cứu
Phân tích kiến trúc và patterns của 10x-Tool-Calls để áp dụng vào dự án KDP-2025-Agent

## 📚 Nội dung chính

### 1. README Analysis
# 🚀 10x-Tool-Calls

**10x-Tool-Calls** is a simple rules setup designed for the **Cursor IDE**, **Windsurf**, or any other agent-based coding assistant that supports tool calls. It helps you get the **maximum value out of your monthly tool call allowance** by running your tasks in a loop with user input—without restarting the chat every time.

Note : This only works with Agent Mode
---

## ✅ What It Does

- After the AI completes a task, it runs a small Python script that asks:
  
```

prompt:

````

- You type your next instruction (e.g., `"add comments"`, `"refactor this"`, etc.)
- The AI uses that input to continue working.
- This loop repeats until:
- You you manually stop, or
- The session hits your **tool call limit**.

---

## 💡 Why This Matters

Most AI coding tools (like Cursor) offer **500 monthly requests**, but each request can include **up to 25 tool calls**. Normally, even saying `"hi"` uses up a full request, wasting potential.

With **10x-Tool-Calls**:
- You start with ...

### 2. Project Structure
```
  📄 readme.md
  📁 Basic/
    📄 readme.md
    📄 rules.md
    📄 userinput.py
```

### 3. Key Files Analysis

#### 1. readme.md (2778 chars)
```md
# 🚀 10x-Tool-Calls

**10x-Tool-Calls** is a simple rules setup designed for the **Cursor IDE**, **Windsurf**, or any other agent-based coding assistant that supports tool calls. It helps you get the **maximum value out of your monthly tool call allowance** by running your tasks in a loop with user i...
```

#### 2. Basic\readme.md (759 chars)
```md
# 🔁 Interactive Task Loop with User Feedback

This tool enables an AI-driven workflow where tasks are performed interactively in response to user input. After each task, the user is prompted for the next instruction. The loop continues until the user stops it manually or the maximum number of tool c...
```

#### 3. Basic\rules.md (715 chars)
```md
---
description: 
globs: 
alwaysApply: true
---

### ✅ Task: Interactive Task Loop with User Feedback

1. **Check if `userinput.py` exists** in the root directory.

   * If it doesn't exist, create it with the following content:

     ```python
     # userinput.py
     user_input = input("prompt: ")...
```

#### 4. Basic\userinput.py (30 chars)
```py
user_input = input("prompt: ")...
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