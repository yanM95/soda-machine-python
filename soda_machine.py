# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:55:56 2022

@author: yannis_montreer
"""
from item import Item
from Singleton import Singleton_base

class SodaMachine (Singleton_base):

    def __init__(self):

        self.items = [
            Item("Coke", 20, 5),
            Item("Sprite", 15, 3),
            Item("Fanta", 15, 3),
        ]

        self.money_inserted = 0

    def display_items (self) :
        for code, item in enumerate(self.items, start = 1):
            print(f"n°{code} - {item.name} - {item.price} NOK - {item.inventory} remaining")

    def insert_money (self, money) :
        if money <= 0:
            raise ValueError
        self.money_inserted += money

        
