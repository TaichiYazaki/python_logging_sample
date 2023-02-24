import random

guess = ''
while guess not in ('表', '裏'):
    print('コインの表裏を当ててください。表か裏を入力してください。')
    guess = input()

toss = random.randint(0,1)
if toss == guess:
    print('あたり')
else:
    print('ハズレもう一回')
    guess = input()
    if toss == guess:
        print('あたり')
    else:
        print('ハズレ。このゲーム苦手ですね。')