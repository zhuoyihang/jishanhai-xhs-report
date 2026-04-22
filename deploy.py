#!/usr/bin/env python3
"""
GitHub Pages 部署脚本
用于将静态网站部署到 GitHub Pages
"""
import os
import subprocess
import sys

GITHUB_USER = "zhuoyihang"
REPO_NAME = "jishanhai-xhs-report"
DEPLOY_DIR = os.path.dirname(os.path.abspath(__file__))

def run_cmd(cmd, cwd=None):
    """执行命令并返回结果"""
    result = subprocess.run(
        cmd, 
        shell=True, 
        cwd=cwd or DEPLOY_DIR,
        capture_output=True, 
        text=True,
        encoding='utf-8'
    )
    return result.returncode, result.stdout, result.stderr

def deploy():
    print(f"=== 开始部署到 GitHub Pages ===")
    print(f"目录: {DEPLOY_DIR}")
    print(f"GitHub 用户: {GITHUB_USER}")
    print(f"仓库: {REPO_NAME}")
    
    # 检查 git 状态
    print("\n[1/6] 检查 Git 仓库状态...")
    code, stdout, stderr = run_cmd("git status")
    
    is_new_repo = "fatal: not a git repository" in stderr or "not a git repository" in stderr
    
    if is_new_repo:
        print("创建新的 Git 仓库...")
        # 初始化 git
        run_cmd("git init")
        run_cmd("git config user.name " + GITHUB_USER)
        run_cmd("git config user.email zhuoyihang@users.noreply.github.com")
        
        # 创建 README
        with open(os.path.join(DEPLOY_DIR, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"# {REPO_NAME}\n\n既山海小红书投放结案报告\n")
        
        # 添加文件
        run_cmd("git add .")
        run_cmd('git commit -m "Initial commit"')
        
        # 创建远程仓库
        print("\n[2/6] 创建 GitHub 仓库...")
        run_cmd(f'gh repo create {REPO_NAME} --public --source=. --remote=origin --push')
        
    else:
        print("Git 仓库已存在")
        run_cmd("git add .")
        run_cmd('git commit -m "Update report"')
    
    # 推送到 main 分支
    print("\n[3/6] 推送到 GitHub...")
    code, stdout, stderr = run_cmd("git push -u origin main")
    if code != 0:
        print(f"推送失败: {stderr}")
        # 尝试创建 main 分支
        run_cmd("git branch -M main")
        run_cmd("git push -u origin main --force")
    
    # 启用 GitHub Pages
    print("\n[4/6] 启用 GitHub Pages...")
    run_cmd(f"gh repo edit {GITHUB_USER}/{REPO_NAME} --enable-pages")
    
    # 设置 Pages 源
    print("\n[5/6] 设置 Pages 来源为 root 分支...")
    run_cmd(f"gh api repos/{GITHUB_USER}/{REPO_NAME}/pages -X POST -f build_type=workflow -f source[branch]=main -f source[path]=/")
    
    print("\n[6/6] 部署完成!")
    print(f"\n📄 报告地址: https://{GITHUB_USER}.github.io/{REPO_NAME}/jishanhai_xiaohongshu_report.html")

if __name__ == "__main__":
    deploy()
