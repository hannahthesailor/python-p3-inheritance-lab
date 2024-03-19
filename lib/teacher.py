#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge if knowledge is not None else [""]

    def teach(self):
        if self.knowledge:
            return random.choice(self.knowledge)
        else:
            return None