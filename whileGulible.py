#!/usr/bin/python

print("Hello, World!")
counter = 0
print("input any number but ", counter)
user = int(input())
print("You input", user)
while (user != counter):
	counter += 1
	print("Input any number but ", counter)
	user = int(input())
	print("You input", user)
print("Nice!!")

