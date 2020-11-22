#!/data/data/com.termux/files/usr/bin/python3

import os


def main():
	path = "/data/data/com.termux/files/usr/etc/bash.bashrc"
	colors = {
			"black": 30,
			"blue": 34,
			"cyan": 36,
			"green": 32,
			"red": 31,
			"purple": 35,
			"yellow": 33
		}


	os.system("clear")
	print("GitHub × github.com/securityhigh\n")

	text = input("Enter a new line > ")
	print("")
	print("black, blue, cyan, green, red, purple, yellow, white")
	color = input("Select color name > ")


	if color not in colors:
		result = text

	else:
		color_number = colors[color]
		result = f"\[\e[{color_number}m\]{text} \[\e[0m\]"


	content = ""
	with open(path, "r") as bashrc:
		content = bashrc.read()

	with open(path, "w") as bashrc:
		content = content.split("\n")
		for index, line in enumerate(content):
			if "PS1" in line:
				content[index] = f"PS1=\"{result}\""

		bashrc.write("\n".join(content))

	print("\nDone! Restart termux now")


if __name__ == "__main__":
	main()
