import pygame
from plane_sprite import *

pygame.init()

# 编写游戏的代码
# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 加载图像数据
bg = pygame.image.load("./images/background.png")
# blit 绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")
# 英雄的坐标和大小
screen.blit(hero, (150, 500))
# update 更新屏幕显示
pygame.display.update()
# 创建时钟对象
clock = pygame.time.Clock()
# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)

# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)



# 游戏循环
while True:
    # 时钟每秒刷新60次
    clock.tick(60)
    # 捕获事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("game over")
            pygame.quit()
            exit()

    # 修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 650
    # 绘制图像
    screen.blit(bg, (0, 0))
    # 绘制飞机
    screen.blit(hero, hero_rect)
    enemy_group.update()
    # 刷新屏幕显示
    enemy_group.draw(screen)
    pygame.display.update()
# 游戏结束退出游戏

print("游戏结束")
pygame.quit()
