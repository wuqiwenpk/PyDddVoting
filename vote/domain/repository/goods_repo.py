import random

from vote.domain.repository.base import Repository


class Goods:
    def __init__(self, id, name, count):
        self.id: int = id
        self.name: str = name
        self.count: int = count


GoodsList = [
    Goods(id=1, name="苹果手机", count=11),
    Goods(id=2, name="小米手机", count=0),
    Goods(id=3, name="华为手机", count=3),
    Goods(id=4, name="一加手机", count=5),
]


class GoodsRepository(Repository):

    def add(self, obj):
        ...

    def remove(self, id):
        ...

    def update(self, id, obj):
        ...

    def get(self, id):
        for a in GoodsList:
            if a.id == id:
                return a
        return None

    @classmethod
    def list(cls):
        return GoodsList

    def award_prizes(self, goods_id: int):
        # todo 发奖 商品数量-1
        goods = self.get(goods_id)
        print(f"发奖 {goods.name}商品数量-1")
        pass

    def goods_choice(self) -> Goods:
        """从奖池抽取一件商品"""
        return self.list()[random.randint(0, 3)]
