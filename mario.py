import pygame
from pygame.sprite import Sprite


class Mario(Sprite):
    mario_idle_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/75.png')]
    mario_run_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/79.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/81.png')]
    mario_jump_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/86.png')]
    mario_swim_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/76.png'),
                        pygame.image.load('Cut-Sprites-For-Mario/Mario/77.png'),
                        pygame.image.load('Cut-Sprites-For-Mario/Mario/78.png'),
                        pygame.image.load('Cut-Sprites-For-Mario/Mario/80.png'),
                        pygame.image.load('Cut-Sprites-For-Mario/Mario/83.png')]

    mario_idle_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/73.png')]
    mario_run_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/69.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/68.png')]
    mario_jump_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/64.png')]
    mario_swim_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/67.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/70.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/71.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/72.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/74.png')]

    big_mario_idle_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/54.png')]
    big_mario_run_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/51.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/52.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/53.png')]
    big_mario_jump_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/49.png')]
    big_mario_swim_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/40.png'),
                            pygame.image.load('Cut-Sprites-For-Mario/Mario/41.png'),
                            pygame.image.load('Cut-Sprites-For-Mario/Mario/42.png'),
                            pygame.image.load('Cut-Sprites-For-Mario/Mario/43.png'),
                            pygame.image.load('Cut-Sprites-For-Mario/Mario/44.png'),
                            pygame.image.load('Cut-Sprites-For-Mario/Mario/45.png')]
    big_mario_crouch_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/48.png')]

    big_mario_idle_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/55.png')]
    big_mario_run_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/58.png'),
                          pygame.image.load('Cut-Sprites-For-Mario/Mario/57.png'),
                          pygame.image.load('Cut-Sprites-For-Mario/Mario/56.png')]
    big_mario_jump_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/60.png')]
    big_mario_swim_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/34.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/35.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/36.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/37.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/38.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/39.png')]
    big_mario_crouch_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/61.png')]

    fire_idle_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/23.png')]
    fire_run_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/19.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/20.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/21.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/22.png')]
    fire_jump_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/17.png')]
    fire_swim_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/11.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/12.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/13.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/14.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/15.png')]
    fire_crouch_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/16.png')]
    fire_throw_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/20.png')]

    fire_idle_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/24.png')]
    fire_run_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/28.png'),
                     pygame.image.load('Cut-Sprites-For-Mario/Mario/27.png'),
                     pygame.image.load('Cut-Sprites-For-Mario/Mario/26.png'),
                     pygame.image.load('Cut-Sprites-For-Mario/Mario/25.png')]
    fire_jump_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/30.png')]
    fire_swim_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/10.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/9.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/8.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/7.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/6.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/5.png')]
    fire_crouch_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/31.png')]
    fire_throw_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/27.png')]

    mario_death = [pygame.image.load('Cut-Sprites-For-Mario/Mario/62.png')]
    fire_flagpole = [pygame.image.load('Cut-Sprites-For-Mario/Mario/1.png'),
                     pygame.image.load('Cut-Sprites-For-Mario/Mario/4.png')]
    big_flagpole = [pygame.image.load('Cut-Sprites-For-Mario/Mario/46.png'),
                    pygame.image.load('Cut-Sprites-For-Mario/Mario/33.png')]
    mario_flagpole = [pygame.image.load('Cut-Sprites-For-Mario/Mario/84.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/66.png')]

    def __init__(self, settings, screen):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings

        self.is_facing_right = True
        self.is_facing_left = False
        self.moving_right = False
        self.moving_left = False
        self.jump = False
        self.falling = False
        self.is_big = False
        self.is_fire = False
        self.throw_fire = False
        self.crouch = False
        self.count = 0
        self.death = False
        self.sprint = False
        self.flag = False
        self.mario_bounce = False
        self.last_y_position = 0

        self.grounded = True
        self.colliding = False
        self.dropping = False
        self.after_flag = False
        self.ending = False

        self.rect = pygame.Rect(4, 385, 30, 30)
        self.screen_rect = screen.get_rect()
        self.rect.x = 4
        self.rect.y = 385
        self.center = float(self.rect.centerx)

        self.big_rect = pygame.Rect(self.rect.x, self.rect.y, 30, 60)

        self.image = pygame.transform.scale(self.mario_idle_right[0], (self.rect.width, self.rect.height))
        self.vel_y = -1
        self.vel_x = 1

    def fire_run_right_animation(self):
        if self.count < 7:
            self.image = pygame.transform.scale(self.fire_run_right[0], (self.rect.width,
                                                                         self.rect.height))
        elif 7 <= self.count < 15:
            self.image = pygame.transform.scale(self.fire_run_right[1], (self.rect.width,
                                                                         self.rect.height))
        elif 15 <= self.count < 22:
            self.image = pygame.transform.scale(self.fire_run_right[2], (self.rect.width,
                                                                         self.rect.height))
        elif 22 <= self.count < 30:
            self.image = pygame.transform.scale(self.fire_run_right[3], (self.rect.width,
                                                                         self.rect.height))
        elif self.count > 30:
            self.count = 0
        self.count += 1
        return self.image

    def big_run_right_animation(self):
        if self.count < 30:
            self.image = pygame.transform.scale(self.big_mario_run_right[0], (self.rect.width,
                                                                              self.rect.height))
        elif 10 <= self.count < 20:
            self.image = pygame.transform.scale(self.big_mario_run_right[1], (self.rect.width,
                                                                              self.rect.height))
        elif 20 <= self.count < 30:
            self.image = pygame.transform.scale(self.big_mario_run_right[2], (self.rect.width,
                                                                              self.rect.height))
        elif self.count > 30:
            self.count = 0
        self.count += 1
        return self.image

    def run_right_animation(self):
        if self.count < 15:
            self.image = pygame.transform.scale(self.mario_run_right[0], (self.rect.width,
                                                                          self.rect.height))
        elif 15 <= self.count < 30:
            self.image = pygame.transform.scale(self.mario_run_right[1], (self.rect.width,
                                                                          self.rect.height))
        elif self.count > 30:
            self.count = 0
        self.count += 1
        return self.image

    def fire_run_left_animation(self):
        if self.count < 7:
            self.image = pygame.transform.scale(self.fire_run_left[0], (self.rect.width,
                                                                        self.rect.height))
        elif 7 <= self.count < 15:
            self.image = pygame.transform.scale(self.fire_run_left[1], (self.rect.width,
                                                                        self.rect.height))
        elif 15 <= self.count < 22:
            self.image = pygame.transform.scale(self.fire_run_left[2], (self.rect.width,
                                                                        self.rect.height))
        elif 22 <= self.count < 30:
            self.image = pygame.transform.scale(self.fire_run_left[3], (self.rect.width,
                                                                        self.rect.height))
        elif self.count > 30:
            self.count = 0
        self.count += 1
        return self.image

    def big_run_left_animation(self):
        if self.count < 10:
            self.image = pygame.transform.scale(self.big_mario_run_left[0], (self.rect.width,
                                                                             self.rect.height))
        elif 10 <= self.count < 20:
            self.image = pygame.transform.scale(self.big_mario_run_left[1], (self.rect.width,
                                                                             self.rect.height))
        elif 20 <= self.count < 30:
            self.image = pygame.transform.scale(self.big_mario_run_left[2], (self.rect.width,
                                                                             self.rect.height))
        elif self.count > 30:
            self.count = 0
        self.count += 1
        return self.image

    def run_left_animation(self):
        if self.count < 15:
            self.image = pygame.transform.scale(self.mario_run_left[0], (self.rect.width,
                                                                         self.rect.height))
        elif 15 <= self.count < 30:
            self.image = pygame.transform.scale(self.mario_run_left[1], (self.rect.width,
                                                                         self.rect.height))
        elif self.count > 30:
            self.count = 0
        self.count += 1
        return self.image

    def fire_jump_right_animation(self):
        self.image = pygame.transform.scale(self.fire_jump_right[0], (self.rect.width,
                                                                      self.rect.height))
        return self.image

    def big_jump_right_animation(self):
        self.image = pygame.transform.scale(self.big_mario_jump_right[0], (self.rect.width,
                                                                           self.rect.height))
        return self.image

    def jump_right_animation(self):
        self.image = pygame.transform.scale(self.mario_jump_right[0], (self.rect.width,
                                                                       self.rect.height))
        return self.image

    def fire_jump_left_animation(self):
        self.image = pygame.transform.scale(self.fire_jump_left[0], (self.rect.width,
                                                                     self.rect.height))
        return self.image

    def big_jump_left_animation(self):
        self.image = pygame.transform.scale(self.big_mario_jump_left[0], (self.rect.width,
                                                                          self.rect.height))
        return self.image

    def jump_left_animation(self):
        self.image = pygame.transform.scale(self.mario_jump_left[0], (self.rect.width,
                                                                      self.rect.height))
        return self.image

    def shooting_fireballs_right(self):
        self.image = pygame.transform.scale(self.fire_throw_right[0], (self.rect.width,
                                                                       self.rect.height))
        return self.image

    def shooting_fireballs_left(self):
        self.image = pygame.transform.scale(self.fire_throw_left[0], (self.rect.width,
                                                                      self.rect.height))
        return self.image

    def dead(self):
        self.image = pygame.transform.scale(self.mario_death[0], (self.rect.width,
                                                                  self.rect.height))
        self.blitme()
        self.rect.y += self.settings.mario_speed
        # if self.rect.y >= self.settings.screen_height:
        # self.rect.x = 4
        # self.rect.y = 385

    def update(self):
        if self.count >= 30:
            self.count = 0

        if not self.death:
            if self.is_facing_right and not self.moving_right and not self.moving_left and not self.jump and not \
                    self.falling and not self.flag:
                if not self.is_big and not self.is_fire:
                    self.image = pygame.transform.scale(self.mario_idle_right[0], (self.rect.width, self.rect.height))
                elif self.is_big and not self.is_fire:
                    self.rect.width, self.rect.height = self.big_rect.width, self.big_rect.height
                    self.image = pygame.transform.scale(self.big_mario_idle_right[0], (self.rect.width,
                                                                                       self.rect.height))
                elif self.is_big and self.is_fire:
                    self.rect.width, self.rect.height = self.big_rect.width, self.big_rect.height
                    self.image = pygame.transform.scale(self.fire_idle_right[0], (self.rect.width, self.rect.height))
            elif self.is_facing_left and not self.moving_right and not self.moving_left and not self.jump and not \
                    self.falling and not self.flag:
                if not self.is_big and not self.is_fire:
                    self.image = pygame.transform.scale(self.mario_idle_left[0], (self.rect.width, self.rect.height))
                elif self.is_big and not self.is_fire:
                    self.rect.width, self.rect.height = self.big_rect.width, self.big_rect.height
                    self.image = pygame.transform.scale(self.big_mario_idle_left[0], (self.rect.width,
                                                                                      self.rect.height))
                elif self.is_big and self.is_fire:
                    self.rect.width, self.rect.height = self.big_rect.width, self.big_rect.height
                    self.image = pygame.transform.scale(self.fire_idle_left[0], (self.rect.width, self.rect.height))

            if self.moving_right and self.rect.right < self.screen_rect.right:  # / 2:
                if self.is_big and not self.is_fire:
                    self.image = self.big_run_right_animation()
                elif self.is_big and self.is_fire:
                    self.image = self.fire_run_right_animation()
                elif not self.is_big and not self.is_fire:
                    self.image = self.run_right_animation()
                self.vel_x = 1
                self.rect.x += self.vel_x
                if self.rect.x >= self.settings.start_scrolling_pos_x:
                    self.rect.x = self.settings.start_scrolling_pos_x
                    if self.settings.bg_x + (self.settings.bg_width + - self.settings.screen_width) >= 0:
                        self.settings.bg_x -= self.vel_x
            elif self.moving_right and self.rect.right == self.screen_rect.right / 2:
                if self.is_big and not self.is_fire:
                    self.image = self.big_run_right_animation()
                elif self.is_big and self.is_fire:
                    self.image = self.fire_run_right_animation()
                elif not self.is_big and not self.is_fire:
                    self.image = self.run_right_animation()
            if self.sprint:
                if self.is_facing_right:
                    if self.is_big and not self.is_fire:
                        self.image = self.big_run_right_animation()
                    elif self.is_big and self.is_fire:
                        self.image = self.fire_run_right_animation()
                    elif not self.is_big and not self.is_fire:
                        self.image = self.run_right_animation()
                    self.vel_x = 1
                    self.rect.x += self.vel_x * 2
                    if self.rect.x >= self.settings.start_scrolling_pos_x:
                        self.rect.x = self.settings.start_scrolling_pos_x
                        if self.settings.bg_x + (self.settings.bg_width + - self.settings.screen_width) >= 0:
                            self.settings.bg_x -= self.vel_x * 3
                elif self.is_facing_left:
                    if self.is_big and not self.is_fire:
                        self.image = self.big_run_left_animation()
                    elif self.is_big and self.is_fire:
                        self.image = self.fire_run_left_animation()
                    elif not self.is_big and not self.is_fire:
                        self.image = self.run_left_animation()
                    self.vel_x = -1
                    self.rect.x += self.vel_x * 2
            if self.moving_left and self.rect.left > 0:
                if self.is_big and not self.is_fire:
                    self.image = self.big_run_left_animation()
                elif self.is_big and self.is_fire:
                    self.image = self.fire_run_left_animation()
                elif not self.is_big and not self.is_fire:
                    self.image = self.run_left_animation()
                self.vel_x = -1
                self.rect.x += self.vel_x
            if self.is_big and not self.is_fire and self.crouch:
                if self.is_facing_right:
                    self.image = pygame.transform.scale(self.big_mario_crouch_right[0], (self.rect.width,
                                                                                         self.rect.height))
                elif self.is_facing_left:
                    self.image = pygame.transform.scale(self.big_mario_crouch_left[0], (self.rect.width,
                                                                                        self.rect.height))
            elif self.is_big and self.is_fire and self.crouch:
                if self.is_facing_right:
                    self.image = pygame.transform.scale(self.fire_crouch_right[0], (self.rect.width, self.rect.height))
                elif self.is_facing_left:
                    self.image = pygame.transform.scale(self.fire_crouch_left[0], (self.rect.width, self.rect.height))
            if self.jump:
                if self.is_facing_right:
                    if self.is_big and not self.is_fire:
                        self.image = self.big_jump_right_animation()
                    elif self.is_big and self.is_fire:
                        self.image = self.fire_jump_right_animation()
                    elif not self.is_big and not self.is_fire:
                        self.image = self.jump_right_animation()
                elif self.is_facing_left:
                    if self.is_big and not self.is_fire:
                        self.image = self.big_jump_left_animation()
                    elif self.is_big and self.is_fire:
                        self.image = self.fire_jump_left_animation()
                    elif not self.is_big and not self.is_fire:
                        self.image = self.jump_left_animation()
                self.vel_y = -1
                self.rect.y += self.vel_y
                if abs(self.last_y_position - self.rect.y) > 160:
                    self.jump = False
                    self.falling = True
            if not self.jump and self.falling:
                if self.is_facing_right:
                    if self.is_big and not self.is_fire:
                        self.image = self.big_jump_right_animation()
                    elif self.is_big and self.is_fire:
                        self.image = self.fire_jump_right_animation()
                    elif not self.is_big and not self.is_fire:
                        self.image = self.jump_right_animation()
                elif self.is_facing_left:
                    if self.is_big and not self.is_fire:
                        self.image = self.big_jump_left_animation()
                    elif self.is_big and self.is_fire:
                        self.image = self.fire_jump_left_animation()
                    elif not self.is_big and not self.is_fire:
                        self.image = self.jump_left_animation()
                self.vel_y = 1
                self.rect.y += self.vel_y * self.settings.mario_jump_speed
                if self.rect.y > 385:
                    self.falling = False
                    self.rect.y = 385
            # if self.falling:
            #     if self.is_facing_right:
            #         if self.is_big and not self.is_fire:
            #             self.image = self.big_jump_right_animation()
            #         elif self.is_big and self.is_fire:
            #             self.image = self.fire_jump_right_animation()
            #         elif not self.is_big and not self.is_fire:
            #             self.image = self.jump_right_animation()
            #     elif self.is_facing_left:
            #         if self.is_big and not self.is_fire:
            #             self.image = self.big_jump_left_animation()
            #         elif self.is_big and self.is_fire:
            #             self.image = self.fire_jump_left_animation()
            #         elif not self.is_big and not self.is_fire:
            #             self.image = self.jump_left_animation()
            #     self.vel_y = 1
            #     self.rect.y += self.vel_y * self.settings.mario_jump_speed
            #     if self.rect.y > 385:
            #         self.falling = False
            #         self.rect.y = 385

            if self.mario_bounce and self.falling:
                self.last_y_position = self.rect.y
                self.falling = False

            if self.mario_bounce:
                if self.is_facing_right:
                    if self.is_big and not self.is_fire:
                        self.image = self.big_jump_right_animation()
                    elif self.is_big and self.is_fire:
                        self.image = self.fire_jump_right_animation()
                    elif not self.is_big and not self.is_fire:
                        self.image = self.jump_right_animation()
                elif self.is_facing_left:
                    if self.is_big and not self.is_fire:
                        self.image = self.big_jump_left_animation()
                    elif self.is_big and self.is_fire:
                        self.image = self.fire_jump_left_animation()
                    elif not self.is_big and not self.is_fire:
                        self.image = self.jump_left_animation()
                self.vel_y = -1
                self.rect.y += self.vel_y
                if abs(self.last_y_position - self.rect.y) > 50:
                    self.mario_bounce = False
                    self.falling = True

            if not self.mario_bounce and self.falling:
                if self.is_facing_right:
                    if self.is_big and not self.is_fire:
                        self.image = self.big_jump_right_animation()
                    elif self.is_big and self.is_fire:
                        self.image = self.fire_jump_right_animation()
                    elif not self.is_big and not self.is_fire:
                        self.image = self.jump_right_animation()
                elif self.is_facing_left:
                    if self.is_big and not self.is_fire:
                        self.image = self.big_jump_left_animation()
                    elif self.is_big and self.is_fire:
                        self.image = self.fire_jump_left_animation()
                    elif not self.is_big and not self.is_fire:
                        self.image = self.jump_left_animation()
                self.vel_y = 1
                self.rect.y += self.vel_y * self.settings.mario_jump_speed
                if self.rect.y > 385:
                    self.falling = False
                    self.rect.y = 385

            if self.is_fire and self.throw_fire:
                if self.is_facing_right:
                    self.image = self.shooting_fireballs_right()
                elif self.is_facing_left:
                    self.image = self.shooting_fireballs_left()
            if self.flag:
                if self.is_big and self.is_fire:
                    if self.rect.y < 379:
                        self.image = pygame.transform.scale(self.fire_flagpole[0], (self.rect.width, self.rect.height))
                        self.blitme()
                        self.vel_y = 1
                        self.rect.y += self.vel_y
                    elif 379 <= self.rect.y < 383:
                        self.image = pygame.transform.scale(self.fire_flagpole[1], (self.rect.width, self.rect.height))
                        self.blitme()
                        self.rect.x += 32
                        self.vel_y = 1
                        self.rect.y += self.vel_y
                    elif self.rect.y == 383:
                        self.rect.x += 64
                        self.rect.y = 385
                        self.flag = False
                elif self.is_big and not self.is_fire:
                    if self.rect.y < 379:
                        self.image = pygame.transform.scale(self.big_flagpole[0], (self.rect.width, self.rect.height))
                        self.blitme()
                        self.vel_y = 1
                        self.rect.y += self.vel_y
                    elif 379 <= self.rect.y < 383:
                        self.image = pygame.transform.scale(self.big_flagpole[1], (self.rect.width, self.rect.height))
                        self.blitme()
                        self.rect.x += 32
                        self.vel_y = 1
                        self.rect.y += self.vel_y
                    elif self.rect.y == 383:
                        self.rect.x += 64
                        self.rect.y = 385
                        self.flag = False
                elif not self.is_big and not self.is_fire:
                    if self.rect.y < 379:
                        self.image = pygame.transform.scale(self.mario_flagpole[0], (self.rect.width, self.rect.height))
                        self.blitme()
                        self.vel_y = 1
                        self.rect.y += self.vel_y
                    elif 379 <= self.rect.y < 383:
                        self.image = pygame.transform.scale(self.mario_flagpole[1], (self.rect.width, self.rect.height))
                        self.blitme()
                        self.rect.x += 32
                        self.vel_y = 1
                        self.rect.y += self.vel_y
                    elif self.rect.y == 383:
                        self.rect.x += 64
                        self.rect.y = 385
                        self.flag = False
            if self.after_flag:
                if self.is_big and self.is_fire:
                    self.image = self.fire_run_right_animation()
                    self.rect.x += 40
                elif self.is_big and not self.is_fire:
                    self.image = self.big_run_right_animation()
                    self.rect.x += 40
                elif not self.is_big and not self.is_fire:
                    self.image = self.run_right_animation()
                    self.rect.x += 40
            if self.ending:
                self.image = pygame.transform.scale(pygame.image.load('Cut-Sprites-For-Mario/Mario/Blank.png'),
                                                    (self.rect.width, self.rect.height))

            if not self.grounded and not self.colliding and not self.falling:  # and self.dropping:
                self.drop()
                # print("I AM DROPPING")

        else:
            self.dead()
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def fall(self):
        if self.falling:
            if self.is_facing_right:
                if self.is_big and not self.is_fire:
                    self.image = self.big_jump_right_animation()
                elif self.is_big and self.is_fire:
                    self.image = self.fire_jump_right_animation()
                elif not self.is_big and not self.is_fire:
                    self.image = self.jump_right_animation()
            elif self.is_facing_left:
                if self.is_big and not self.is_fire:
                    self.image = self.big_jump_left_animation()
                elif self.is_big and self.is_fire:
                    self.image = self.fire_jump_left_animation()
                elif not self.is_big and not self.is_fire:
                    self.image = self.jump_left_animation()
            self.vel_y = 1
            self.rect.y += self.vel_y * self.settings.mario_jump_speed
            if self.rect.y > 385:
                self.falling = False
                self.rect.y = 385

    def drop(self):
        if self.rect.y < 385 and not self.mario_bounce and not self.jump and not self.grounded and not self.colliding:
            self.rect.y += self.vel_y * self.settings.mario_jump_speed
            # self.falling = True
            # print("dropping")
