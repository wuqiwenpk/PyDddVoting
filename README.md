# DDD Python Example VotingSystem

### 目的：

领域驱动设计 Domain driven design

python 学习实践demo

### 简单业务需求：

投票系统：

- 用户能对选手进行投票

- 用户限定每天只能投一次

- 每天获得票数最多选手获得仓库随机奖品

1. 角色

    - 用户

    - 选手

2. 行为

    - 用户对选手今天投票

    - 系统给每天票数最多用户发奖

### 设计：

抽奖领域拆分：

- 抽奖子域

- 风控子域

- 奖品子域

模块结构编排：

- Entity

    - User -- 用户

    - Player -- 选手

    - Prize -- 奖品

- ValueObject

- AggregateRoot

### 环境：

python 3.9.13

```bash
pip3 install -r requirements.txt
```

### 启动：

```bash
flask run
```
