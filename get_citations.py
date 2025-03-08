import json
import requests
import time
from datetime import datetime

def batch_get_citations(paper_titles, original_data, batch_size=10):
    """批量获取多篇论文的引用数，使用正确的API格式"""
    base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # 存储结果的字典
    results = {}
    not_found_info = {}  # 存储未找到论文的详细原因
    
    # 将论文标题分批处理
    batches = [paper_titles[i:i+batch_size] for i in range(0, len(paper_titles), batch_size)]
    
    print("\n" + "="*80)
    print("开始批量查询过程")
    print("="*80)
    
    for batch_index, batch in enumerate(batches):
        print(f"\n批次 {batch_index+1}/{len(batches)} - 处理 {len(batch)} 篇论文:")
        
        # 逐个处理每篇论文而不是使用batch接口
        for i, title in enumerate(batch):
            print(f"\n论文 {batch_index*batch_size + i + 1}: '{title}'")
            old_citation = original_data["papers"][title]["citations"]
            
            try:
                # 使用search接口查询论文
                params = {
                    "query": title,
                    "fields": "title,citationCount,url",
                    "limit": 5  # 获取几个匹配结果以提高找到的概率
                }
                
                response = requests.get(base_url, params=params, headers=headers)
                response.raise_for_status()
                data = response.json()
                
                # 检查是否有搜索结果
                if not data.get("data") or len(data["data"]) == 0:
                    reason = "API返回空结果"
                    not_found_info[title] = reason
                    print(f"  ❌ 未找到: {reason}")
                    continue
                
                # 尝试从结果中找到完全匹配的论文标题
                found = False
                for paper in data["data"]:
                    if 'title' not in paper or 'citationCount' not in paper:
                        continue
                    
                    # 检查标题是否完全匹配（忽略大小写）
                    if paper['title'].lower() == title.lower():
                        new_citation = paper['citationCount']
                        results[title] = new_citation
                        
                        # 显示引用变化
                        change = new_citation - old_citation
                        change_symbol = "+" if change > 0 else ""
                        
                        print(f"  ✅ 更新成功: {old_citation} → {new_citation} ({change_symbol}{change})")
                        if 'url' in paper and paper['url']:
                            print(f"  📄 论文链接: {paper['url']}")
                        found = True
                        break
                
                if not found:
                    reason = f"标题不完全匹配: API返回的标题与查询不匹配"
                    not_found_info[title] = reason
                    print(f"  ❌ 未找到: {reason}")
                    print(f"  📝 备注: 找到了{len(data['data'])}个结果，但没有标题完全匹配的")
                
                # 添加延迟以避免API速率限制
                # time.sleep(1)
                
            except requests.exceptions.RequestException as e:
                error_msg = f"API请求错误: {str(e)}"
                print(f"  ❌ {error_msg}")
                not_found_info[title] = error_msg
                # time.sleep(3)  # 出错后等待更长时间
            
        # 每批次之间添加额外延迟
        if batch_index < len(batches) - 1:
            print(f"\n等待5秒以避免API限制...")
            # time.sleep(5)
    
    return results, not_found_info

def update_citations_file(file_path):
    """更新citations.json文件中的引用数并详细记录整个过程"""
    # 读取现有的citations.json文件
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"读取文件错误: {e}")
        return
    
    # 对论文标题进行排序，先按引用量升序，相同引用量按更新日期升序
    paper_info = []
    for title, info in data["papers"].items():
        # 对于没有last_updated字段的论文，设置一个默认值
        last_updated = info.get("last_updated", "1970-01-01-00:00:00")
        paper_info.append({
            "title": title,
            "citations": info["citations"],
            "last_updated": last_updated
        })
    
    # 按引用量和更新日期排序
    sorted_papers = sorted(paper_info, key=lambda x: (x["citations"], x["last_updated"]))
    
    # 提取排序后的标题列表
    paper_titles_ordered = [paper["title"] for paper in sorted_papers]
    
    # 输出排序信息
    print("\n" + "="*80)
    print("论文排序信息（按引用量升序，相同引用量按更新日期升序）")
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
    
    # 批量获取引用数
    citation_results, not_found_info = batch_get_citations(paper_titles_ordered, sorted_data)
    
    # 更新数据并创建报告
    update_count = 0
    updated_papers = []
    skipped_papers = []
    
    for title in paper_titles_ordered:
        if title in citation_results:
            old_citation = sorted_data["papers"][title]["citations"]
            new_citation = citation_results[title]
            
            # 只在找到了新引用时才更新数据和时间戳
            sorted_data["papers"][title]["citations"] = new_citation
            
            # 使用更精确的时间格式 YYYY-MM-DD-HH:MM:SS
            current_time = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            sorted_data["papers"][title]["last_updated"] = current_time
            
            update_count += 1
            
            # 记录更新信息
            change = new_citation - old_citation
            change_str = f"+{change}" if change > 0 else str(change)
            updated_papers.append({
                "title": title, 
                "old": old_citation, 
                "new": new_citation, 
                "change": change_str,
                "updated_time": current_time
            })
        else:
            # 记录未更新信息，但不修改原数据
            skipped_papers.append({
                "title": title,
                "reason": not_found_info.get(title, "未知原因")
            })
    
    # 再次保存更新后的数据
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(sorted_data, file, indent=2, ensure_ascii=False)
    
    # 创建详细报告
    print("\n" + "="*80)
    print("更新摘要报告")
    print("="*80)
    print(f"总论文数: {len(paper_titles_ordered)}")
    print(f"成功更新: {update_count} ({(update_count/len(paper_titles_ordered)*100):.1f}%)")
    print(f"更新失败: {len(paper_titles_ordered) - update_count} ({((len(paper_titles_ordered) - update_count)/len(paper_titles_ordered)*100):.1f}%)")
    
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