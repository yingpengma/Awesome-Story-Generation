import json
import requests
from datetime import datetime

def update_paper_citation(title, paper_data, file_path, retry_limit=3):
    """获取单篇论文的引用数，并立即更新JSON文件"""
    base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    old_citation = paper_data["papers"][title]["citations"]
    print(f"\n论文: '{title}'")
    
    for attempt in range(retry_limit):
        try:
            # 使用search接口查询论文
            params = {
                "query": title,
                "fields": "title,citationCount,url",
                "limit": 10  # 获取几个匹配结果以提高找到的概率
            }
            
            response = requests.get(base_url, params=params, headers=headers)
            
            # 特殊处理429错误，直接跳过不显示
            if response.status_code == 429:
                if attempt < retry_limit - 1:
                    print(f"  ⚠️ 第{attempt+1}次尝试: 跳过并重试...")
                    continue
                else:
                    print(f"  ❌ 已达到最大重试次数，跳过此论文")
                    return False, "已达到最大重试次数"
            
            response.raise_for_status()
            data = response.json()
            
            # 检查是否有搜索结果
            if not data.get("data") or len(data["data"]) == 0:
                if attempt < retry_limit - 1:
                    print(f"  ⚠️ 第{attempt+1}次尝试: API返回空结果，重试...")
                    continue
                else:
                    print(f"  ❌ 未找到: API返回空结果")
                    return False, "API返回空结果"
            
            # 尝试从结果中找到完全匹配的论文标题
            found = False
            for paper in data["data"]:
                if 'title' not in paper or 'citationCount' not in paper:
                    continue
                
                # 检查标题是否完全匹配（忽略大小写）
                if paper['title'].lower() == title.lower():
                    new_citation = paper['citationCount']
                    
                    # 显示引用变化
                    change = new_citation - old_citation
                    change_symbol = "+" if change > 0 else ""
                    
                    print(f"  ✅ 更新成功: {old_citation} → {new_citation} ({change_symbol}{change})")
                    if 'url' in paper and paper['url']:
                        print(f"  📄 论文链接: {paper['url']}")
                    
                    # 立即更新数据
                    paper_data["papers"][title]["citations"] = new_citation
                    current_time = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
                    paper_data["papers"][title]["last_updated"] = current_time
                    
                    # 立即保存到文件
                    with open(file_path, 'w', encoding='utf-8') as file:
                        json.dump(paper_data, file, indent=2, ensure_ascii=False)
                    print(f"  💾 数据已保存到文件")
                    
                    found = True
                    return True, new_citation
            
            if not found:
                if attempt < retry_limit - 1:
                    print(f"  ⚠️ 第{attempt+1}次尝试: 标题不完全匹配，重试...")
                    continue
                else:
                    print(f"  ❌ 未找到: 标题不完全匹配")
                    print(f"  📝 备注: 找到了{len(data['data'])}个结果，但没有标题完全匹配的")
                    return False, "标题不完全匹配"
                
        except requests.exceptions.HTTPError as e:
            if "429" in str(e):  # 不显示429错误
                if attempt < retry_limit - 1:
                    print(f"  ⚠️ 第{attempt+1}次尝试: 跳过并重试...")
                    continue
                else:
                    print(f"  ❌ 已达到最大重试次数，跳过此论文")
                    return False, "已达到最大重试次数"
            else:
                if attempt < retry_limit - 1:
                    print(f"  ⚠️ 第{attempt+1}次尝试: HTTP错误，重试...")
                    continue
                else:
                    print(f"  ❌ API请求错误")
                    return False, f"HTTP错误"
        except requests.exceptions.RequestException:
            if attempt < retry_limit - 1:
                print(f"  ⚠️ 第{attempt+1}次尝试: 请求异常，重试...")
                continue
            else:
                print(f"  ❌ API请求错误")
                return False, "请求异常"
    
    return False, "超过最大重试次数"

def update_citations_file(file_path):
    """更新citations.json文件中的引用数并详细记录整个过程"""
    # 读取现有的citations.json文件
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"读取文件错误: {e}")
        return
    
    # 对论文标题进行排序，只按更新日期升序（最久未更新的排在前面）
    paper_info = []
    for title, info in data["papers"].items():
        # 对于没有last_updated字段的论文，设置一个默认值
        last_updated = info.get("last_updated", "1970-01-01-00:00:00")
        paper_info.append({
            "title": title,
            "citations": info["citations"],
            "last_updated": last_updated
        })
    
    # 只按更新日期排序（最旧的在前，最新的在后）
    sorted_papers = sorted(paper_info, key=lambda x: x["last_updated"])
    
    # 提取排序后的标题列表
    paper_titles_ordered = [paper["title"] for paper in sorted_papers]
    
    # 输出排序信息
    print("\n" + "="*80)
    print("论文排序信息（按最后更新时间升序排列，最久未更新的排在前面）")
    print("="*80)
    for i, paper in enumerate(sorted_papers):
        print(f"{i+1}. '{paper['title']}' - 引用: {paper['citations']}, 最后更新: {paper['last_updated']}")
    
    # 将排序结果保存到原始文件
    print("\n" + "="*80)
    print("排序完成，保存排序后的数据到原始文件")
    print("="*80)
    
    # 创建一个新的有序字典，保留原始数据结构但按新顺序排列
    sorted_data = {"papers": {}}
    for title in paper_titles_ordered:
        sorted_data["papers"][title] = data["papers"][title]
    
    # 保存排序后的数据到原始文件
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(sorted_data, file, indent=2, ensure_ascii=False)
    print(f"排序后的数据已保存到: {file_path}")
    
    print(f"\n开始更新 {len(paper_titles_ordered)} 篇论文的引用数...")
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 逐个更新引用数并立即保存
    updated_papers = []
    skipped_papers = []
    
    for index, title in enumerate(paper_titles_ordered):
        print(f"\n处理论文 {index+1}/{len(paper_titles_ordered)}")
        success, result = update_paper_citation(title, sorted_data, file_path)
        
        if success:
            updated_papers.append({
                "title": title,
                "old": sorted_data["papers"][title]["citations"] - result,
                "new": sorted_data["papers"][title]["citations"],
                "change": f"+{result}" if result > 0 else str(result),
                "updated_time": sorted_data["papers"][title]["last_updated"]
            })
        else:
            skipped_papers.append({
                "title": title,
                "reason": result
            })
    
    # 创建详细报告
    print("\n" + "="*80)
    print("更新摘要报告")
    print("="*80)
    print(f"总论文数: {len(paper_titles_ordered)}")
    print(f"成功更新: {len(updated_papers)} ({(len(updated_papers)/len(paper_titles_ordered)*100):.1f}%)")
    print(f"更新失败: {len(skipped_papers)} ({(len(skipped_papers)/len(paper_titles_ordered)*100):.1f}%)")
    
    if updated_papers:
        print("\n" + "="*80)
        print("成功更新的论文")
        print("="*80)
        for paper in updated_papers:
            print(f"'{paper['title']}'")
            print(f"  引用变化: {paper['old']} → {paper['new']} ({paper['change']})")
            print(f"  更新时间: {paper['updated_time']}")
    
    if skipped_papers:
        print("\n" + "="*80)
        print("未能更新的论文")
        print("="*80)
        for paper in skipped_papers:
            print(f"'{paper['title']}'")
            print(f"  原因: {paper['reason']}")
    
    print("\n" + "="*80)
    print(f"更新完成! 文件已保存到: {file_path}")
    print(f"更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)

if __name__ == "__main__":
    # 指定citations.json文件的路径
    file_path = "citations.json"
    
    # 运行更新函数
    update_citations_file(file_path)