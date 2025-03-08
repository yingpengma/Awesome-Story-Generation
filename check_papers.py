import json
import re
from datetime import datetime
import sys

def extract_titles_from_md():
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        # 使用正则表达式匹配**与**之间的标题
        pattern = r'\`\ \*\*(.*?)\*\*\ \['
        titles = re.findall(pattern, content)
        # 过滤掉非论文标题（如标签等）
        paper_titles = [title for title in titles if not title.startswith('[') and len(title) > 10]
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
    
    # 加载当前的citations数据
    citations_data = load_citations()
    
    # 获取当前日期
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # 检查并添加新的论文条目
    for title in md_titles:
        if title not in citations_data['papers']:
            citations_data['papers'][title] = {
                'citations': 0,
                'last_updated': current_date
            }
            print(f'添加新论文：{title}')
    
    # 检查citations.json中的论文是否都在README.md中
    titles_not_found = []
    for title in list(citations_data['papers'].keys()):
        if title not in md_titles:
            titles_not_found.append(title)
            print(f'警告：在README.md中未找到论文：{title}')
    
    # 保存更新后的数据
    save_citations(citations_data)
    
    if titles_not_found:
        print('\n以下论文在README.md中未找到：')
        for title in titles_not_found:
            print(f'- {title}')
    else:
        print('\n同步完成！所有论文标题已验证。')

if __name__ == '__main__':
    main()