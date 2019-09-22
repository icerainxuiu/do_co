import pygame
import time
from plane_sprite import *


class PlaneGame(object):
    """飞机大战住程序"""

    def __init__(self):
        print("游戏初始化")
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT,200)
        pygame.time.set_timer(HERO_FIRE_EVENT, 50)

    def __create_sprites(self):
        bg1 = BlackGround()
        bg2 = BlackGround(True)
        self.back_ground = pygame.sprite.Group(bg1, bg2)
        # 创建低级的精灵组
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始")

        while True:
            # 设置刷新帧
            self.clock.tick(FRAM_PRE_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新绘制精灵
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        # 判断是否要退出
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("低级出场")
                # 创建低级精灵
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("友")
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 8
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -8
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            time.sleep(1)
            PlaneGame.__game_over()
            time.sleep(0.5)

    def __update_sprites(self):
        self.back_ground.update()
        self.back_ground.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("game over")
        pygame.quit()
        exit()
if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()