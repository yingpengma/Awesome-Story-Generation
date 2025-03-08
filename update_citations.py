import json
import re

def update_citations():
    try:
        with open('citations.json', 'r', encoding='utf-8') as f:
            citations_data = json.load(f)
    except Exception as e:
        raise Exception(f'读取citations.json失败: {str(e)}')

    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            md_content = f.read()
    except Exception as e:
        raise Exception(f'读取README.md失败: {str(e)}')

    # 遍历citations.json中的每个论文
    for paper_title, paper_info in citations_data['papers'].items():
        # 在markdown中查找完全匹配的论文标题
        matches = [m.start() for m in re.finditer(re.escape(paper_title), md_content)]
        
        # 检查匹配数量
        if len(matches) == 0:
            raise Exception(f'未找到论文标题的匹配: {paper_title}')
        elif len(matches) > 1:
            raise Exception(f'找到多个论文标题的匹配: {paper_title}')
        
        # 找到匹配位置后的citation badge
        match_pos = matches[0]
        badge_pattern = r'\[!\[\]\(https://img\.shields\.io/badge/citation-\d+-blue\)\]\(\)'
        badge_match = re.search(badge_pattern, md_content[match_pos:])
        
        if not badge_match:
            raise Exception(f'未找到论文的citation badge: {paper_title}')
        
        # 更新citation数量
        old_badge = badge_match.group(0)
        new_badge = f'[![](https://img.shields.io/badge/citation-{paper_info["citations"]}-blue)]()'        
        
        # 替换badge
        md_content = md_content.replace(old_badge, new_badge)
        print(f'成功更新论文 "{paper_title}" 的引用数为 {paper_info["citations"]}')
    
    # 保存更新后的README.md
    try:
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(md_content)
    except Exception as e:
        raise Exception(f'保存README.md失败: {str(e)}')

if __name__ == '__main__':
    try:
        update_citations()
    except Exception as e:
        print(f'错误: {str(e)}')