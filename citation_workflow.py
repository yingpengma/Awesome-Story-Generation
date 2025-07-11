#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
论文引用数管理工具 - 完整工作流
整合了论文同步、引用数获取和README更新的完整流程
"""

import json
import re
import requests
from datetime import datetime
import sys
import time

class CitationWorkflow:
    def __init__(self):
        self.readme_file = 'README.md'
        self.citations_file = 'citations.json'
        self.api_delay = 1  # API请求间隔（秒），固定1秒
        self.skip_recent_hours = 24  # 跳过24小时内更新过的论文
        
    def print_header(self, title, width=80):
        """打印格式化的标题"""
        print("-"*width)
        print(f"{title:^{width}}")
        print("-"*width)
    
    def print_step(self, step_num, total_steps, description):
        """打印步骤信息"""
        print(f"\n[步骤 {step_num}/{total_steps}] {description}")
    
    def extract_authors_from_readme(self, title):
        """从README.md中提取指定论文的作者信息"""
        try:
            with open(self.readme_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找论文标题的位置
            title_pattern = r'\*\*' + re.escape(title) + r'\*\*'
            match = re.search(title_pattern, content)
            if not match:
                return "未找到论文标题"
            
            # 从标题位置向后查找作者信息
            start_pos = match.end()
            line_content = content[start_pos:start_pos+500].split('\n')[0]  # 只在同一行查找
            
            # README格式: **标题** [[paper]](链接) [作者信息] [可选注释] [![citation badge
            # 需要跳过 [[paper]](链接) 部分，找到第一个不是[[开头的[内容]
            
            # 正则表达式：跳过所有[[...]](...) 格式的链接，找到第一个单独的[作者信息]
            # 格式：[[paper]](链接) 或 [[paper]](链接) [[code]](链接) 后面的 [作者信息]
            author_pattern = r'(?:\[\[[^\]]+\]\]\([^)]*\)\s*)+\[([^\]]+)\]'
            author_match = re.search(author_pattern, line_content)
            
            if author_match:
                authors = author_match.group(1).strip()
                # 确保这是作者信息而不是其他内容（如badge或注释）
                if (not authors.startswith('!')  # 不是badge
                    and 'http' not in authors.lower()  # 不是链接
                    and len(authors) > 3):  # 有实际内容
                    return authors
            
            return "未找到作者信息"
            
        except Exception as e:
            return f"提取失败: {str(e)}"
    
    def extract_titles_from_md(self):
        """从README.md中提取论文标题"""
        try:
            with open(self.readme_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 更新匹配模式以适应不同格式的标题
            pattern = r'\*\*(.*?)\*\*\s*\['
            titles = re.findall(pattern, content)
            
            # 清理标题（去除多余的空格和特殊字符）
            paper_titles = [title.strip() for title in titles if not title.startswith('[') and len(title.strip()) > 10]
            
            print(f"✅ 成功从 {self.readme_file} 中提取了 {len(paper_titles)} 篇论文")
            return paper_titles
            
        except FileNotFoundError:
            print(f'❌ 错误：{self.readme_file} 文件不存在')
            sys.exit(1)
        except Exception as e:
            print(f'❌ 读取 {self.readme_file} 时发生错误：{str(e)}')
            sys.exit(1)
    
    def load_citations(self):
        """加载citations.json文件"""
        try:
            with open(self.citations_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"✅ 成功加载 {self.citations_file}，现有 {len(data['papers'])} 篇论文")
            return data
        except FileNotFoundError:
            print(f'⚠️  {self.citations_file} 文件不存在，将创建新文件')
            return {'papers': {}}
        except json.JSONDecodeError:
            print(f'❌ 错误：{self.citations_file} 格式不正确')
            sys.exit(1)
        except Exception as e:
            print(f'❌ 读取 {self.citations_file} 时发生错误：{str(e)}')
            sys.exit(1)
    
    def save_citations(self, data):
        """保存citations数据到文件"""
        try:
            with open(self.citations_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f'❌ 保存 {self.citations_file} 时发生错误：{str(e)}')
            sys.exit(1)
    
    def sync_papers(self):
        """步骤1：同步README.md和citations.json中的论文列表"""
        self.print_step(1, 3, "同步论文列表")
        
        # 从README.md提取论文标题
        md_titles = self.extract_titles_from_md()
        
        # 加载当前的citations数据
        citations_data = self.load_citations()
        
        # 获取当前日期
        current_date = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        
        # 创建新的citations数据，只包含md中存在的论文
        new_citations = {'papers': {}}
        added_count = 0
        
        print("\n📋 开始同步论文列表...")
        
        # 同步处理
        for title in md_titles:
            if title in citations_data.get('papers', {}):
                # 保留已有论文的引用数据
                new_citations['papers'][title] = citations_data['papers'][title]
            else:
                # 添加新论文
                new_citations['papers'][title] = {
                    'title': title,  # 添加标题字段
                    'citations': 0,
                    'last_updated': '1970-01-01-00:00:00'  # 设置很久以前的时间，确保新论文会被立即更新
                }
                print(f"➕ 添加新论文：{title}")
                added_count += 1
        
        # 检查是否有论文在README.md中不存在（只从数据中移除，不修改README文件）
        old_papers = set(citations_data.get('papers', {}).keys())
        removed_papers = old_papers - set(md_titles)
        if removed_papers:
            print(f"\n📋 以下 {len(removed_papers)} 篇论文在README.md中不存在，将从数据中移除（不修改README文件）：")
            for title in removed_papers:
                print(f"   - {title}")
        
        # 保存更新后的数据
        self.save_citations(new_citations)
        
        print(f"\n✅ 论文列表同步完成！")
        print(f"   📊 当前总计：{len(new_citations['papers'])} 篇论文")
        print(f"   ➕ 新增：{added_count} 篇")
        print(f"   📋 数据清理：{len(removed_papers)} 篇")
        
        return new_citations
    
    def is_recently_updated(self, last_updated_str):
        """检查论文是否在最近24小时内更新过"""
        try:
            from datetime import timedelta
            
            # 解析最后更新时间
            last_updated = datetime.strptime(last_updated_str, '%Y-%m-%d-%H:%M:%S')
            
            # 计算时间差
            time_diff = datetime.now() - last_updated
            
            # 如果小于设定的跳过时间，返回True
            return time_diff < timedelta(hours=self.skip_recent_hours)
            
        except (ValueError, TypeError):
            # 如果时间格式解析失败，认为需要更新
            return False
    
    def update_paper_citation(self, title, paper_data, retry_limit=3):
        """获取单篇论文的引用数，并立即更新JSON文件"""
        base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        old_citation = paper_data["papers"][title]["citations"]
        search_title = paper_data["papers"][title]["title"]  # 使用标题字段搜索
        print(f"\n📖 论文: '{title}'")
        if search_title != title:
            print(f"🔍 通过标题搜索: '{search_title}'")
        
        for attempt in range(retry_limit):
            try:
                # 使用search接口查询论文
                params = {
                    "query": search_title,  # 使用标题搜索
                    "fields": "title,citationCount,url,authors",  # 添加作者信息
                    "limit": 10  # 获取几个匹配结果以提高找到的概率
                }
                
                response = requests.get(base_url, params=params, headers=headers)
                
                # 特殊处理429错误，直接跳过不显示
                if response.status_code == 429:
                    if attempt < retry_limit - 1:
                        print(f"   ⚠️ 第{attempt+1}次尝试: 请求频率限制，1秒后重试...")
                        time.sleep(self.api_delay)  # 固定1秒等待时间
                        continue
                    else:
                        print(f"   ❌ 已达到最大重试次数，跳过此论文")
                        return False, "已达到最大重试次数"
                
                response.raise_for_status()
                data = response.json()
                
                # 检查是否有搜索结果
                if not data.get("data") or len(data["data"]) == 0:
                    if attempt < retry_limit - 1:
                        print(f"   ⚠️ 第{attempt+1}次尝试: API返回空结果，重试...")
                        time.sleep(self.api_delay)
                        continue
                    else:
                        print(f"   ❌ 未找到: API返回空结果")
                        return False, "API返回空结果"
                
                # 尝试从结果中找到完全匹配的论文标题
                found = False
                for paper in data["data"]:
                    if 'title' not in paper or 'citationCount' not in paper:
                        continue
                    
                    # 检查标题是否完全匹配（忽略大小写）
                    if paper['title'].lower() == search_title.lower():
                        new_citation = paper['citationCount']
                        
                        # 显示引用变化
                        change = new_citation - old_citation
                        if change > 0:
                            change_symbol = f"📈 +{change}"
                        elif change < 0:
                            change_symbol = f"📉 {change}"
                        else:
                            change_symbol = "📊 无变化"
                        
                        print(f"   ✅ 更新成功: {old_citation} → {new_citation} ({change_symbol})")
                        if 'url' in paper and paper['url']:
                            print(f"   🔗 论文链接: {paper['url']}")
                        
                        # 立即更新数据
                        paper_data["papers"][title]["citations"] = new_citation
                        current_time = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
                        paper_data["papers"][title]["last_updated"] = current_time
                        
                        # 立即保存到文件
                        self.save_citations(paper_data)
                        
                        found = True
                        return True, new_citation
                
                if not found:
                    # 不重试，显示最佳匹配结果和作者信息
                    print(f"   ❌ 未找到完全匹配的标题")
                    
                    if data.get("data") and len(data["data"]) > 0:
                        # 找到相似度最高的结果（取第一个）
                        best_match = data["data"][0]
                        print(f"   🔍 最佳匹配结果:")
                        print(f"      API标题: '{best_match.get('title', '无标题')}'")
                        print(f"      当前搜索: '{search_title}'")
                        
                        # 显示作者信息
                        readme_authors = self.extract_authors_from_readme(title)
                        print(f"      README作者: {readme_authors}")
                        
                        api_authors = "无作者信息"
                        if 'authors' in best_match and best_match['authors']:
                            author_names = [author.get('name', '未知') for author in best_match['authors'][:5]]  # 只显示前5个作者
                            api_authors = ', '.join(author_names)
                            if len(best_match['authors']) > 5:
                                api_authors += f" 等{len(best_match['authors'])}人"
                        print(f"      API作者: {api_authors}")
                        
                        print(f"   📝 如确认是同一篇论文，请手动修改citations.json中该论文的title字段")
                    
                    return False, "标题不完全匹配"
                        
            except requests.exceptions.HTTPError as e:
                if "429" in str(e):  # 频率限制错误，重试
                    if attempt < retry_limit - 1:
                        print(f"   ⚠️ 第{attempt+1}次尝试: 请求频率限制，1秒后重试...")
                        time.sleep(self.api_delay)
                        continue
                    else:
                        print(f"   ❌ 已达到最大重试次数，跳过此论文")
                        return False, "已达到最大重试次数"
                else:
                    if attempt < retry_limit - 1:
                        print(f"   ⚠️ 第{attempt+1}次尝试: HTTP错误({e})，重试...")
                        time.sleep(self.api_delay)
                        continue
                    else:
                        print(f"   ❌ API请求错误: {e}")
                        return False, f"HTTP错误"
            except requests.exceptions.RequestException as e:
                if attempt < retry_limit - 1:
                    print(f"   ⚠️ 第{attempt+1}次尝试: 请求异常({e})，重试...")
                    time.sleep(self.api_delay)
                    continue
                else:
                    print(f"   ❌ API请求错误: {e}")
                    return False, "请求异常"
            
            # 请求成功后等待一段时间避免频率限制
            if attempt < retry_limit - 1:
                time.sleep(self.api_delay)
        
        return False, "超过最大重试次数"
    
    def get_citations(self, citations_data):
        """步骤2：获取论文引用数"""
        self.print_step(2, 3, "获取最新引用数")
        
        # 对论文标题进行排序，按更新日期升序（最久未更新的排在前面）
        paper_info = []
        for title, info in citations_data["papers"].items():
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
        print(f"\n📊 论文更新优先级排序（共{len(sorted_papers)}篇，按最后更新时间升序）:")
        for i, paper in enumerate(sorted_papers[:5]):  # 只显示前5个
            print(f"   {i+1}. 引用: {paper['citations']}, 最后更新: {paper['last_updated']}")
        if len(sorted_papers) > 5:
            print(f"   ... 还有 {len(sorted_papers)-5} 篇论文")
        
        # 创建一个新的有序字典，保留原始数据结构但按新顺序排列
        sorted_data = {"papers": {}}
        for title in paper_titles_ordered:
            sorted_data["papers"][title] = citations_data["papers"][title]
        
        # 保存排序后的数据到原始文件
        self.save_citations(sorted_data)
        
        # 逐个更新引用数并立即保存
        updated_papers = []
        skipped_papers = []
        skipped_recent = []
        
        need_update_count = 0
        # 先统计需要更新的论文数量
        for title in paper_titles_ordered:
            last_updated = sorted_data["papers"][title].get("last_updated", "1970-01-01-00:00:00")
            if not self.is_recently_updated(last_updated):
                need_update_count += 1
        
        print(f"📊 需要更新: {need_update_count} 篇，跳过: {len(paper_titles_ordered) - need_update_count} 篇（24小时内已更新）")
        
        current_update_index = 0
        for index, title in enumerate(paper_titles_ordered):
            # 检查是否在24小时内更新过
            last_updated = sorted_data["papers"][title].get("last_updated", "1970-01-01-00:00:00")
            if self.is_recently_updated(last_updated):
                skipped_recent.append({
                    "title": title,
                    "last_updated": last_updated
                })
                continue
            
            current_update_index += 1
            print(f"\n🔄 处理论文 {current_update_index}/{need_update_count}")
            
            success, result = self.update_paper_citation(title, sorted_data)
            
            if success:
                old_citations = sorted_data["papers"][title]["citations"] - (result if isinstance(result, int) else 0)
                updated_papers.append({
                    "title": title,
                    "old": old_citations,
                    "new": sorted_data["papers"][title]["citations"],
                    "change": sorted_data["papers"][title]["citations"] - old_citations,
                    "updated_time": sorted_data["papers"][title]["last_updated"]
                })
            else:
                skipped_papers.append({
                    "title": title,
                    "reason": result
                })
            
            # 在请求间添加延迟
            if index < len(paper_titles_ordered) - 1:
                time.sleep(self.api_delay)
        
        # 创建详细报告
        print(f"\n✅ 成功更新: {len(updated_papers)} ({(len(updated_papers)/len(paper_titles_ordered)*100):.1f}%)")
        print(f"⏭️ 跳过（24小时内已更新）: {len(skipped_recent)} ({(len(skipped_recent)/len(paper_titles_ordered)*100):.1f}%)")

        if updated_papers:
            print(f"📈 成功更新的论文 ({len(updated_papers)}篇):")
            for i, paper in enumerate(updated_papers[:10]):  # 只显示前10个
                change_symbol = "📈" if paper['change'] > 0 else "📉" if paper['change'] < 0 else "📊"
                print(f"   {i+1}. '{paper['title'][:50]}{'...' if len(paper['title']) > 50 else ''}'")
                print(f"      引用变化: {paper['old']} → {paper['new']} ({change_symbol}{paper['change']:+d})")
            if len(updated_papers) > 10:
                print(f"   ... 还有 {len(updated_papers)-10} 篇成功更新")
        
        
        if skipped_papers:
            print(f"❌ 未能更新的论文 ({len(skipped_papers)}篇):")
            for i, paper in enumerate(skipped_papers[:5]):  # 只显示前5个
                print(f"   {i+1}. '{paper['title'][:50]}{'...' if len(paper['title']) > 50 else ''}'")
                print(f"      原因: {paper['reason']}")
            if len(skipped_papers) > 5:
                print(f"   ... 还有 {len(skipped_papers)-5} 篇更新失败")
        
        return sorted_data, updated_papers
    
    def update_readme_citations(self, citations_data, updated_papers_list):
        """步骤3：更新README.md中的citation badges（严格保护，只更新badges）"""
        self.print_step(3, 3, "更新README.md中的引用标签")
        
        # 如果没有论文需要更新README
        if not updated_papers_list:
            return True
        
        try:
            with open(self.readme_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
                md_content = original_content  # 保留原始内容副本
        except Exception as e:
            print(f'❌ 读取 {self.readme_file} 失败: {str(e)}')
            return False
        
        # 只更新实际在步骤2中成功更新的论文
        papers_to_update = [paper["title"] for paper in updated_papers_list]
        print(f"📄 开始更新 {len(papers_to_update)} 篇论文的citation badges...")
        
        updated_count = 0
        error_count = 0
        
        # 只遍历需要更新的论文
        for paper_title in papers_to_update:
            try:
                paper_info = citations_data['papers'][paper_title]
                
                # 在markdown中查找完全匹配的论文标题
                matches = [m.start() for m in re.finditer(r'\*\*' + re.escape(paper_title) + r'\*\*', md_content)]
                
                # 检查匹配数量
                if len(matches) == 0:
                    print(f"   ⚠️ 未找到论文标题的匹配: {paper_title}")
                    error_count += 1
                    continue
                elif len(matches) > 1:
                    print(f"   ⚠️ 找到多个论文标题的匹配: {paper_title}")
                    error_count += 1
                    continue
                
                # 找到匹配位置后的citation badge
                match_pos = matches[0]
                badge_pattern = r'\[!\[\]\(https://img\.shields\.io/badge/citation-\d+-blue\)\]\(\)'
                badge_match = re.search(badge_pattern, md_content[match_pos:])
                
                if not badge_match:
                    print(f"   ⚠️ 未找到论文的citation badge: {paper_title}")
                    error_count += 1
                    continue
                
                # 更新citation数量
                old_badge = badge_match.group(0)
                new_badge = f'[![](https://img.shields.io/badge/citation-{paper_info["citations"]}-blue)]()'        
                
                # 只替换当前论文位置后的第一个badge
                before_match = md_content[:match_pos + badge_match.start()]
                after_match = md_content[match_pos + badge_match.end():]
                md_content = before_match + new_badge + after_match
                
                print(f"   ✅ 成功更新: '{paper_title[:50]}{'...' if len(paper_title) > 50 else ''}' → {paper_info['citations']} 引用")
                updated_count += 1
                
            except Exception as e:
                print(f"   ❌ 处理论文时出错: {paper_title} - {str(e)}")
                error_count += 1
                continue
        
        # 验证内容完整性：检查除了citation badges外是否有其他变化
        print(f"\n🔍 验证内容完整性...")
        
        # 移除所有citation badges进行对比
        original_no_badges = re.sub(r'\[!\[\]\(https://img\.shields\.io/badge/citation-\d+-blue\)\]\(\)', '', original_content)
        updated_no_badges = re.sub(r'\[!\[\]\(https://img\.shields\.io/badge/citation-\d+-blue\)\]\(\)', '', md_content)
        
        if original_no_badges != updated_no_badges:
            print(f"❌ 检测到除citation badges外的其他内容变化，拒绝保存以保护README完整性")
            return False
        
        # 保存更新后的README.md
        try:
            with open(self.readme_file, 'w', encoding='utf-8') as f:
                f.write(md_content)
            print(f"✅ 内容完整性验证通过")
            print(f"💾 {self.readme_file} 更新完成！")
            print(f"   ✅ 成功更新: {updated_count} 个citation badges")
            if error_count > 0:
                print(f"   ⚠️ 更新失败: {error_count} 个")
            return True
        except Exception as e:
            print(f'❌ 保存 {self.readme_file} 失败: {str(e)}')
            return False
    
    def run_workflow(self):
        """运行完整的引用数管理工作流"""
        print(f"⏰ 启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        try:
            # 步骤1: 同步论文列表
            citations_data = self.sync_papers()
            
            # 步骤2: 获取引用数
            updated_data, updated_papers_list = self.get_citations(citations_data)
            
            # 步骤3: 更新README
            readme_success = self.update_readme_citations(updated_data, updated_papers_list)
            
            # 最终报告
            
            print(f"\n{'✅' if readme_success else '❌'} 步骤3 - README更新: {'完成' if readme_success else '失败'}")
            print(f"⏰ 完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        except KeyboardInterrupt:
            print(f"\n\n⚠️ 用户中断了工作流程")
            print(f"💾 当前进度已保存到 {self.citations_file}")
        except Exception as e:
            print(f"\n\n❌ 工作流程执行失败: {str(e)}")
            sys.exit(1)

def main():
    """主函数"""
    workflow = CitationWorkflow()
    workflow.run_workflow()

if __name__ == "__main__":
    main() 