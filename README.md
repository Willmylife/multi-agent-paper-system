# 多 Agent 协同论文辅助系统

这是一个基于多 Agent 协作的自动化论文辅助系统 Demo，功能包括：

- 文献整理（生成 BibTeX / 文献摘要）
- 答辩 PPT 自动生成
- 论文引用检查报告生成
- 多 Agent 并行任务处理
- 日志自动记录

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

1. 设置 OpenAI API Key:

```bash
export OPENAI_API_KEY="你的 OpenAI API Key"
```

2. 运行系统:

```bash
python agents/full_paper_agent_system.py
```

生成的 PPT 会在 `outputs/` 目录，日志在 `logs/` 目录。