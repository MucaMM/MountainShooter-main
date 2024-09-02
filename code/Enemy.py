#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED[self.name]
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_speed = self.speed  

    def move(self):
        self.rect.left -= self.speed

        if self.name == 'Enemy3':
            self.rect.top += self.vertical_speed

            if self.rect.bottom >= WIN_HEIGHT:
                self.vertical_speed = -self.speed

            elif self.rect.top <= 0:
                self.vertical_speed = 2 * self.speed

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))