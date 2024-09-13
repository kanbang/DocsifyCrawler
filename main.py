import os
import re
import requests
import chardet  # 新增 chardet 库来检测编码

# Docsify 站点的基础 URL
base_url = 'https://handbook.sansi.io/'

# 创建存储 markdown 文件的文件夹
if not os.path.exists('markdown_files'):
    os.makedirs('markdown_files')

# 下载并保存 _sidebar.md 文件
def download_sidebar():
    sidebar_url = base_url + '_sidebar.md'
    response = requests.get(sidebar_url)
    
    if response.status_code == 200:
        # 自动检测编码
        detected_encoding = chardet.detect(response.content)['encoding']
        response.encoding = detected_encoding

        with open('markdown_files/_sidebar.md', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"_sidebar.md 下载成功，编码: {detected_encoding}")
        return response.text
    else:
        print(f"未能下载 _sidebar.md, 状态码: {response.status_code}")
        return None

# 下载 Markdown 文件
def download_markdown_file(file_url, save_path):
    response = requests.get(file_url)
    
    if response.status_code == 200:
        # 自动检测编码
        detected_encoding = chardet.detect(response.content)['encoding']
        response.encoding = detected_encoding

        # 使用 UTF-8 保存文件，避免中文乱码
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"{save_path} 下载成功，编码: {detected_encoding}")
    else:
        print(f"未能下载 {file_url}, 状态码: {response.status_code}")

# 从 _sidebar.md 中提取并下载所有 Markdown 文件
def download_all_markdown_files(sidebar_content):
    # 正则表达式匹配 Markdown 链接: [文本](链接)
    pattern = r'\[.*?\]\((.*?)\)'
    links = re.findall(pattern, sidebar_content)

    for href in links:
        # 只处理 .md 文件的链接
        if href.endswith('.md'):
            # 确定文件的完整 URL 和保存路径
            file_url = base_url + href
            save_path = os.path.join('markdown_files', href.strip('/'))
            dir_name = os.path.dirname(save_path)
            
            # 创建文件夹
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            
            # 下载并保存 Markdown 文件
            download_markdown_file(file_url, save_path)

# 主程序
def main():
    # 下载 _sidebar.md 文件
    sidebar_content = download_sidebar()
    
    # 如果 _sidebar.md 下载成功，则继续下载内容
    if sidebar_content:
        download_all_markdown_files(sidebar_content)

if __name__ == '__main__':
    main()
