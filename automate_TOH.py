import pyautogui as pgui

import cv2
import time

pgui.FAILSAFE = True # 0, 0に持っていくと止まる



class Tower:
    """
     → x
    ↓
    y
    """

    
    # ボタンの座標一覧
    pos_summon = 918, 628
    
    pos_hero_tab = 665, 1020
    pos_soldier_tab = 799, 1028
    
    pos_box = 615, 311
    pos_close = 999, 370
    pos_box2 = 604, 445
    pos_close2 = 861, 720
    pos_box3 = 671, 382
    pos_close3 = 953, 457

    pos_times = 1030, 678
    
    pos_dope = 847, 175
    pos_money = 904, 184
    pos_warp = 973, 176
    pos_tyhoon = 1044, 182
    
    # スクロール用の座標
    
    def __init__(self):
        self.tab_state = 0 # 0:閉じ, 1:ヒーロー,2:ソルジャー
        # 時間
        self.start = time.time()
        self.time_limit = 1200
        
    
    
    ##########################
    # 基本操作
    ##########################
    def open_hero_tab(self):
        """
        この関数はヒーロータブを開く
        """
        if self.tab_state != 1:
            pgui.click(Tower.pos_hero_tab) # 勇者タブを開く
            self.tab_state = 1
        else:
            pass
    
    def open_soldier_tab(self):
        if self.tab_state != 2:
            pgui.click(Tower.pos_soldier_tab) # ソルジャータブを開く
            self.tab_state = 2
        else:
            pass
        
    def get_super_soldier(self):
        """
        終盤で強い戦士を獲得する
        """
        t = time.time() - self.start
        if t >= self.time_limit*0.8:
            for i in range(3):
                self.top2btm_const()
                pgui.click(1038, 946)

    def get_soldier(self):
        """
        ソルジャーを獲得する
        
        タブを開く
        タブを最下位に移動
        獲得をクリック
        """
        self.open_soldier_tab()
        self.btm2top()
        self.click_get_soldier()
        
        
    
    def summon(self,times=10):
        """
        勇者を召喚
        """
        for i in range(times):
            pgui.click(x=885, y=613) # 勇者召喚
            
    def click_get_soldier(self):
        """
        ソルジャーの獲得ボタンを押す
        """
        pgui.click(pgui.locateOnScreen('get_soldier.png', confidence=0.9))
          
    def click_target(self, img_name):
        """
        画像の名前を渡し、右下に位置するレベルアップを押す
        """
        self.target_x, self.target_y = pgui.center(pgui.locateOnScreen(img_name, confidence=0.9))
        self.target_x += 415
        self.target_y += 57
        pgui.click(self.target_x, self.target_y)
        
    def click_times(self, times=4):
        for t in range(times):
            pgui.click(Tower.pos_times)
        
    def click_four_bottun(self):
        pgui.click(Tower.pos_dope)
        pgui.click(Tower.pos_money)
        pgui.click(Tower.pos_warp)
        pgui.click(Tower.pos_tyhoon)
    
        
    def open_box(self):
        # 宝箱
        pgui.click(Tower.pos_box)
        pgui.click(Tower.pos_close)
        
        # ログインボーナス宝箱
        pgui.click(Tower.pos_box2)
        pgui.click(Tower.pos_close2)
        
        # 豪華宝箱
        pgui.click(Tower.pos_box3)
        pgui.click(Tower.pos_close3)
        pgui.click(Tower.pos_close)
        
    def renew_dungeon(self):
        """
        10分経っていたら
        勇者タブの最下位にいるときに、
        ダンジョンを更新
        """
        t = time.time() - self.start
        if t >= self.time_limit: # 10min だと早いので1h
            self.start = time.time()
    #         self.click_target("dungeon.png")
            try:
                pgui.click(x=1035, y=942) # renew
                time.sleep(0.1)
                pgui.click(x=936, y=716) # yes
                time.sleep(0.1)
                pgui.click(x=936, y=716) # yes
                time.sleep(5)
                pgui.click(x=787, y=672) # 参加
                time.sleep(0.1)
                pgui.click(x=776, y=716) # no
                time.sleep(5)
                pgui.click(x=842, y=696) # start
                time.sleep(5)
                pgui.click(x=787, y=672) # 参加


    #             self.click_target("dungeon.png")
                try:
                    pgui.click(pgui.center(pgui.locateOnScreen("yes.png", confidence=1)))
                    try:
                        pgui.click(pgui.center(pgui.locateOnScreen("yes.png", confidence=1)))
                        pgui.click(pgui.center(pgui.locateOnScreen("no.png", confidence=1)))
                    except:
                        pass
                except:
                    pass
            except:
                print("no dungeon")


    def btm2top(self,times=1):
        """
        タブを下へ移動させる
        """
        for t in range(times):
            # 下に移動
            # x=1138, y=973
            pgui.moveTo(1138,973)

            # 上にドラッグ
            # x=1138, y=720
            pgui.dragTo(1138, 720, 0.2)
    
    def top2btm(self,times=1):
        """
        タブを上へ移動させる
        """
        for t in range(times):
            # 上に移動
            # x=1138, y=720
            pgui.moveTo(1138, 720)

            # 下にドラッグ
            # x=1138, y=973
            pgui.dragTo(1138,973, 0.2)
    
    def top2btm_const(self,times=1):
        """
        タブを上へ移動させる
        """
        for t in range(times):
            # 上に移動
            # x=1138, y=720
            pgui.moveTo(1138, 720)

            # 下にドラッグ
            # x=1138, y=844+>>760->>800->810+>805>>795-->820++>815>814>815
            pgui.dragTo(1138,815, 0.2)

    
    def clime(self, times=1):
        """
        階層を上へ移動させる
        """
        for t in range(times):
            # 上に移動
            # x=813, y=281
            pgui.moveTo(x=813, y=281)

            # 下にドラッグ
            # x=835, y=662
            pgui.dragTo(835, 662, 0.2)
            
    ##########################
    # 一連操作
    ##########################
    def initial_action(self):
        """
        １．ヒーロータブを開く
        click_times(
        ２．塔の一番上に移動
        ３．タブを一番上へ移動
        ４．勇者を召喚
        """
        self.open_hero_tab()
        self.click_times()
        self.clime(times=2)
        self.top2btm(times=2)
        self.summon(times=10)

    def level_up_hero(self):
        """
        ヒーロータブを開く
        タブを最上位に移動
        勇者サモンをレベルアップ
        勇者をレベルアップ
        """
        self.open_hero_tab()
#         self.top2btm()
        self.btm2top(5)
        self.renew_dungeon()
        
        for i in range(12):
            self.top2btm_const()
            pgui.click(1038, 946)
        try:
            self.click_target("summon.png")
        except:
            pass
        try:
            self.click_target("hero.png")
        except:
            pass

    def try_level_up(self):
        """
        宝箱を開き、
        閉じる
        
        
        
        ソルジャータブを開き、
        最下位に移動し、
        兵士を獲得
        
        勇者タブを開き、
        勇者をレベルアップさせる(ダンジョンを更新)
        
        ４つのボタンを押す
        """
        self.open_box()
        self.get_soldier()
        self.get_super_soldier()
        self.level_up_hero()
        self.click_four_bottun()
        
    def main(self):
        self.initial_action()
        for i in range(1000):
            self.try_level_up()
            for i in range(4):
                self.clime(times=1)
                self.summon(times=100)
if __name__ == "__main__":
    tower = Tower()
    tower.main()