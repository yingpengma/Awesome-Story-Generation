import json
import re
from datetime import datetime
import sys

def extract_titles_from_md():
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        # 更新匹配模式以适应不同格式的标题
        pattern = r'\*\*(.*?)\*\*\s*\['
        titles = re.findall(pattern, content)
        # 清理标题（去除多余的空格和特殊字符）
        paper_titles = [title.strip() for title in titles if not title.startswith('[') and len(title.strip()) > 10]
        return paper_titles
    except FileNotFoundError:
        print('错误：README.md文件不存在')
        sys.exit(1)
    except Exception as e:
        print(f'读取README.md时发生错误：{str(e)}')
        sys.exit(1)

def load_citations():
    try:
        with open('citations.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('错误：citations.json文件不存在')
        sys.exit(1)
    except json.JSONDecodeError:
        print('错误：citations.json格式不正确')
        sys.exit(1)
    except Exception as e:
        print(f'读取citations.json时发生错误：{str(e)}')
        sys.exit(1)

def save_citations(data):
    try:
        with open('citations.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f'保存citations.json时发生错误：{str(e)}')
        sys.exit(1)

def main():
    # 从README.md提取论文标题
    md_titles = extract_titles_from_md()
    print(f'在README.md中找到 {len(md_titles)} 篇论文')
    
    # 加载当前的citations数据
    citations_data = load_citations()
    print(f'在citations.json中现有 {len(citations_data["papers"])} 篇论文')
    
    # 获取当前日期
    current_date = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    
    # 创建新的citations数据，只包含md中存在的论文
    new_citations = {'papers': {}}
    
    # 同步处理
    for title in md_titles:
        if title in citations_data['papers']:
            # 保留已有论文的引用数据
            new_citations['papers'][title] = citations_data['papers'][title]
        else:
            # 添加新论文
            new_citations['papers'][title] = {
                'citations': 0,
                'last_updated': current_date
            }
            print(f'添加新论文：{title}')
    
    # 检查是否有论文被移除
    removed_papers = set(citations_data['papers'].keys()) - set(md_titles)
    if removed_papers:
        print('\n以下论文在README.md中已被移除：')
        for title in removed_papers:
            print(f'- {title}')
    
    # 保存更新后的数据
    save_citations(new_citations)
    
    print(f'\n同步完成！现在citations.json中共有 {len(new_citations["papers"])} 篇论文')

if __name__ == '__main__':
    main()