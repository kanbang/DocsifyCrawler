### 项目功能描述

**DocsifyMDDownloader** 是一个用于自动化爬取 Docsify 站点的 Python 工具，能够下载站点中的所有 Markdown 文件，包括 `_sidebar.md` 文件，并以正确的编码方式保存到本地。该工具可以轻松地备份 Docsify 生成的静态站点内容，并确保 Markdown 文件中的中文或其他多语言字符不出现乱码问题。

#### 功能特点：
- 自动下载 Docsify 站点中的 `_sidebar.md` 文件。
- 解析并下载 Markdown 文件，保持站点原有的目录结构。
- 自动检测文件编码，确保中文及其他非 ASCII 字符正确保存。
- 支持递归下载，轻松备份大型 Docsify 站点的所有内容。

此工具非常适合希望备份 Docsify 站点内容或将其转换到其他平台的开发者。通过简洁的命令运行，用户可以迅速下载并保存站点的所有文档内容。