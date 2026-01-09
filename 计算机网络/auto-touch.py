import os
import re

# ================= 配置区域 =================
TARGET_DIR = "./U06"      # 笔记存放目录
TOPIC_NAME = "RIP"        # 当前正在学习的主题
PAGE_STEP = 1             # 这一篇笔记涵盖的页数（比如学了4页，就填4）
# ===========================================

def get_next_info():
    """扫描文件夹，获取下一个文件的起始页码和序号"""
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        return 1, 1 # 如果文件夹是空的，从第1页、序号01开始

    max_page = 0
    max_index = 0
    
    # 正则表达式说明：匹配 p数字-数字.主题数字.md 或 p数字.主题数字.md
    # 捕获组1: 起始页, 捕获组2: 结束页(可选), 捕获组3: 序号
    pattern = re.compile(rf"p(\d+)(?:-(\d+))?\.{TOPIC_NAME}(\d+)\.md")

    for filename in os.listdir(TARGET_DIR):
        match = pattern.match(filename)
        if match:
            start_p = int(match.group(1))
            end_p = int(match.group(2)) if match.group(2) else start_p
            idx = int(match.group(3))
            
            # 记录目前扫描到的最大页码和最大序号
            if end_p > max_page:
                max_page = end_p
            if idx > max_index:
                max_index = idx

    # 返回：下一篇的起始页（最大页+1），下一篇的序号（最大序号+1）
    return max_page + 1, max_index + 1

def create_single_note():
    # 1. 自动计算起始页码和序号
    start_page, next_idx = get_next_info()
    
    # 2. 根据当前的步长计算结束页码
    end_page = start_page + PAGE_STEP - 1
    
    # 3. 格式化文件名
    if PAGE_STEP == 1:
        page_range = f"p{start_page}"
    else:
        page_range = f"p{start_page}-{end_page}"
        
    file_name = f"{page_range}.{TOPIC_NAME}{next_idx:02d}.md"
    file_path = os.path.join(TARGET_DIR, file_name)

    # 4. 创建文件
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {TOPIC_NAME} 笔记 - {page_range}\n\n")
        print(f"--- 🚀 成功创建下一篇笔记 ---")
        print(f"文件名: {file_name}")
        print(f"路径: {file_path}")
    else:
        print(f"❌ 错误：文件 {file_name} 已存在，请检查配置或手动更名。")

if __name__ == "__main__":
    create_single_note()