"""
Repository Ingester
Script để clone và phân tích các repositories tham khảo
Tự động tạo research notes trong Obsidian Vault
"""

import os
import subprocess
import requests
from pathlib import Path
from bs4 import BeautifulSoup
import json
from datetime import datetime
import sys

# Add tools directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tools'))
from obsidian_writer import ObsidianWriter

class RepoIngester:
    """Tool để ingest và phân tích repositories"""
    
    def __init__(self):
        self.writer = ObsidianWriter()
        self.repos = {
            "MiniMax-M1": {
                "url": "https://github.com/MiniMax-AI/MiniMax-M1.git",
                "type": "git"
            },
            "Archon": {
                "url": "https://github.com/coleam00/Archon.git", 
                "type": "git"
            },
            "Claude-Task-Master": {
                "url": "https://github.com/eyaltoledano/claude-task-master.git",
                "type": "git"
            },
            "MCP-Protocol": {
                "url": "https://github.com/modelcontextprotocol/python-sdk.git",
                "type": "git"
            },
            "10x-Tool-Calls": {
                "url": "https://github.com/perrypixel/10x-Tool-Calls.git",
                "type": "git"
            },
            "Agent-Zero": {
                "url": "https://github.com/frdel/agent-zero.git",
                "type": "git"
            },
            "Cursor-Best-Practices": {
                "url": "https://github.com/sanjeed5/awesome-cursor-rules-mdc.git",
                "type": "git"
            },
            "Pydantic-Validation": {
                "url": "https://ai.pydantic.dev/",
                "type": "website"
            }
        }
        self.temp_dir = Path("temp_repos")
        self.temp_dir.mkdir(exist_ok=True)
    
    def clone_repo(self, name: str, url: str) -> str:
        """Clone repository về local"""
        repo_path = self.temp_dir / name
        
        if repo_path.exists():
            print(f"📁 Repo {name} đã tồn tại, skip clone")
            return str(repo_path)
        
        print(f"📥 Đang clone {name}...")
        try:
            subprocess.run(["git", "clone", url, str(repo_path)], check=True)
            print(f"✅ Đã clone thành công {name}")
            return str(repo_path)
        except subprocess.CalledProcessError as e:
            print(f"❌ Lỗi khi clone {name}: {e}")
            return None
    
    def extract_readme(self, repo_path: str) -> str:
        """Trích xuất nội dung README"""
        readme_files = ["README.md", "README.txt", "readme.md", "README.rst"]
        
        for readme in readme_files:
            readme_path = Path(repo_path) / readme
            if readme_path.exists():
                try:
                    with open(readme_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        print(f"📖 Đã đọc README: {readme}")
                        return content
                except UnicodeDecodeError:
                    try:
                        with open(readme_path, 'r', encoding='latin-1') as f:
                            content = f.read()
                            print(f"📖 Đã đọc README (latin-1): {readme}")
                            return content
                    except:
                        continue
        
        print(f"⚠️ Không tìm thấy README trong {repo_path}")
        return "Không tìm thấy README"
    
    def analyze_structure(self, repo_path: str) -> str:
        """Phân tích cấu trúc thư mục"""
        structure = []
        repo_path_obj = Path(repo_path)
        
        # Bỏ qua các thư mục không cần thiết
        ignore_dirs = {'.git', '__pycache__', 'node_modules', '.vscode', '.idea'}
        
        for root, dirs, files in os.walk(repo_path):
            # Lọc bỏ các thư mục không cần thiết
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            
            level = Path(root).relative_to(repo_path_obj).parts
            indent = '  ' * len(level)
            
            if level:
                structure.append(f"{indent}📁 {level[-1]}/")
            
            # Chỉ hiển thị một số file quan trọng
            important_files = [f for f in files if any(f.endswith(ext) for ext in 
                           ['.py', '.js', '.ts', '.md', '.yaml', '.yml', '.json', '.txt'])]
            
            for file in important_files[:10]:  # Giới hạn 10 files
                structure.append(f"{indent}  📄 {file}")
        
        return "\n".join(structure)
    
    def extract_key_files(self, repo_path: str) -> list:
        """Trích xuất nội dung các file quan trọng"""
        key_files = []
        important_extensions = ['.py', '.js', '.ts', '.md', '.yaml', '.yml', '.json']
        repo_path_obj = Path(repo_path)
        
        for root, dirs, files in os.walk(repo_path):
            # Bỏ qua thư mục .git
            if '.git' in dirs:
                dirs.remove('.git')
            
            for file in files:
                if any(file.endswith(ext) for ext in important_extensions):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if len(content) < 5000:  # Giới hạn kích thước
                                relative_path = file_path.relative_to(repo_path_obj)
                                key_files.append({
                                    'path': str(relative_path),
                                    'content': content[:1000],  # Giới hạn nội dung
                                    'size': len(content)
                                })
                    except UnicodeDecodeError:
                        try:
                            with open(file_path, 'r', encoding='latin-1') as f:
                                content = f.read()
                                if len(content) < 5000:
                                    relative_path = file_path.relative_to(repo_path_obj)
                                    key_files.append({
                                        'path': str(relative_path),
                                        'content': content[:1000],
                                        'size': len(content)
                                    })
                        except:
                            continue
                    except:
                        continue
        
        # Sắp xếp theo kích thước file (lớn nhất trước)
        key_files.sort(key=lambda x: x['size'], reverse=True)
        return key_files[:10]  # Chỉ lấy 10 files quan trọng nhất
    
    def scrape_website(self, url: str) -> str:
        """Scrape nội dung từ website"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Lấy title
            title = soup.find('title')
            title_text = title.get_text() if title else "No title"
            
            # Lấy nội dung chính
            main_content = ""
            
            # Tìm các thẻ có nội dung quan trọng
            for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'code', 'pre']):
                text = tag.get_text().strip()
                if text and len(text) > 10:
                    main_content += f"{text}\n\n"
            
            return f"# {title_text}\n\n{main_content[:2000]}..."
            
        except Exception as e:
            print(f"❌ Lỗi khi scrape {url}: {e}")
            return f"Không thể truy cập {url}: {e}"
    
    def generate_summary(self, name: str, readme: str, structure: str, key_files: list, repo_type: str = "git") -> str:
        """Tạo tóm tắt cho repository"""
        today = datetime.now().strftime('%Y-%m-%d')
        
        summary = f"""# Phân tích Repository: {name}

## 📋 Tổng quan
- **Repository**: {name}
- **Type**: {repo_type}
- **Date**: {today}
- **Status**: Completed

## 🎯 Mục tiêu nghiên cứu
Phân tích kiến trúc và patterns của {name} để áp dụng vào dự án KDP-2025-Agent

## 📚 Nội dung chính

### 1. README Analysis
{readme[:1000]}...

### 2. Project Structure
```
{structure}
```

### 3. Key Files Analysis
"""
        
        for i, file_info in enumerate(key_files[:5], 1):
            file_ext = Path(file_info['path']).suffix
            summary += f"""
#### {i}. {file_info['path']} ({file_info['size']} chars)
```{file_ext[1:] if file_ext else 'text'}
{file_info['content'][:300]}...
```
"""
        
        summary += """
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
"""
        
        return summary
    
    def ingest_repo(self, name: str) -> str:
        """Xử lý toàn bộ repository"""
        print(f"\n🔍 Bắt đầu ingest {name}...")
        
        repo_info = self.repos[name]
        repo_type = repo_info["type"]
        url = repo_info["url"]
        
        if repo_type == "git":
            # Clone repo
            repo_path = self.clone_repo(name, url)
            if not repo_path:
                return None
            
            # Trích xuất thông tin
            readme = self.extract_readme(repo_path)
            structure = self.analyze_structure(repo_path)
            key_files = self.extract_key_files(repo_path)
            
        elif repo_type == "website":
            # Scrape website
            readme = self.scrape_website(url)
            structure = "Website content"
            key_files = []
        
        # Tạo summary
        summary = self.generate_summary(name, readme, structure, key_files, repo_type)
        
        # Tạo note trong Obsidian
        note_path = f"01-LEARNING/01-Research-Projects/{name}/Overview.md"
        self.writer.create_note(note_path, summary, template="research-note")
        
        print(f"✅ Đã tạo note cho {name}: {note_path}")
        
        return note_path
    
    def ingest_all_repos(self):
        """Xử lý tất cả repositories"""
        print("🚀 Bắt đầu ingest tất cả repositories...")
        
        results = []
        for name in self.repos.keys():
            try:
                result = self.ingest_repo(name)
                results.append((name, result))
            except Exception as e:
                print(f"❌ Lỗi khi xử lý {name}: {e}")
                results.append((name, None))
        
        # Tạo summary report
        self._create_summary_report(results)
        
        print(f"\n🎉 Hoàn thành ingest {len(results)} repositories!")
        return results
    
    def _create_summary_report(self, results: list):
        """Tạo báo cáo tổng hợp"""
        today = datetime.now().strftime('%Y-%m-%d')
        
        report = f"""# Research Summary Report - {today}

## 📊 Tổng quan
- **Ngày nghiên cứu**: {today}
- **Tổng số repositories**: {len(results)}
- **Thành công**: {len([r for r in results if r[1]])}
- **Thất bại**: {len([r for r in results if not r[1]])}

## 📋 Chi tiết từng repository

"""
        
        for name, result in results:
            status = "✅ Thành công" if result else "❌ Thất bại"
            report += f"### {name}\n- **Status**: {status}\n- **Note**: {result or 'N/A'}\n\n"
        
        report += """
## 🎯 Next Steps
1. Review từng research note
2. Extract key patterns và insights
3. Apply vào KDP-2025-Agent design
4. Update knowledge base

## 📌 Tags
#research-summary #learning #kdp-2025
"""
        
        # Tạo summary note
        summary_path = f"01-LEARNING/03-Insights/Research-Summary-{today}.md"
        self.writer.create_note(summary_path, report)
        print(f"📊 Đã tạo summary report: {summary_path}")

# Test function
def test_repo_ingest():
    """Test RepoIngester với một repository"""
    ingester = RepoIngester()
    
    # Test với một repo nhỏ
    result = ingester.ingest_repo("Agent-Zero")
    print(f"Test result: {result}")

if __name__ == "__main__":
    # Test với một repo trước
    # test_repo_ingest()
    
    # Ingest toàn bộ 8 repositories
    ingester = RepoIngester()
    ingester.ingest_all_repos() 