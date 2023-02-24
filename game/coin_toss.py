import random
from logging import getLogger

class InvalidInputError(Exception):
    """無効な値が入力されたことを知らせるエラー"""
    pass

def game_start():
    # loggerをインスタンス化
    logger = getLogger(__name__)
    # ゲーム開始ログの出力
    logger.debug('game start')

    guess = ''
    while guess not in ('表', '裏'):
        print('コインの表裏を当ててください。表か裏を入力してください。')
        guess = input()

    toss = random.randint(0,1)
    if toss == 0:
        toss = '表'
    elif toss == 1:
        toss = '裏'
    # 追加　tossとguessの値を調べてみる
    logger.debug(f"toss='{toss}")
    logger.debug(f"guess='{guess}'")
    if toss == guess:
        print('あたり')
    else:
        print('ハズレもう一回')
        guess = input()
        if guess not in('表', '裏'):
            logger.error(f'2回目のguessで無効な値が入力された!guess={guess}')
            raise InvalidInputError('入力は表か裏にしてください')
        
        if toss == guess:
            print('あたり')
        else:
            print('ハズレ。このゲーム苦手ですね。')
    
    # ゲーム終了ログの出力
    logger.debug('game end')