# 같은 폴더에 있어야 문제없이 모듈을 사용할 수 있다.

# import practice_module
# practice_module.price(3) # 3명이서 영화 보러 갔을 때
# practice_module.price_morning(4) # 4명이서 조조 할인
# practice_module.price_army(6) # 6명이서 군인 할인

# import practice_module as mv # 모듈명이 practice_module로 너무 길어서 mv로 짧게 지정할 수 있다.
# mv.price(3)
# mv.price_morning(4)
# mv.price_army(6)

# from practice_module import *
## from random import * 사용할 때 같은 방식
## 앞에 모듈 없이 사용 가능하게 함
# price(3)
# price_morning(4)
# price_army(6)

# from practice_module import price, price_morning
## 두 개만 따로 지정해서 모듈을 사용할 수 있다. 그럼 기존의 army는 사용이 안됌

from practice_module import price_army as mv
# 위에서 줄이는 방법을 이제 응용해서 한개의 지정된 값만 사용가능.
mv(5)