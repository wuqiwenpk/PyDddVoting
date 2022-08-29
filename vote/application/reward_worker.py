"""发奖后台进程"""
import schedule
import time

from vote.domain.service.reward import RewardService

# INTERVAL_SECONDS = 60*60*24
INTERVAL_SECONDS = 10


def reward_job():
    """发奖"""
    reward_svc = RewardService()
    # 获取当前票数最多选手id
    player_id = reward_svc.get_max_day_votes_player_id()
    # 发奖
    reward_svc.reward(player_id)


if __name__ == '__main__':
    schedule.every(INTERVAL_SECONDS).seconds.do(reward_job)
    while True:
        schedule.run_pending()
        time.sleep(1)
