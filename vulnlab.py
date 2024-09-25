import requests
import sys
import json

colors = {
    "Easy": "green",
    "Medium": "yellow",
    "Hard": "red",
    "Insane": "purple"
}

def main(argv):
    if len(argv) != 1:
        print('python3 vulnlab.py <machine_name>')
        sys.exit(2)

    machine_name = argv[0].capitalize()

    url = "https://api.vulnlab.com/api/v1/machines"
    response = requests.get(url)
    data = json.loads(response.text)

    system = ''
    difficulty = ''
    difficulty_color = ''
    for machine in data['message']:
        if machine['name'] == machine_name:
            system = machine['os']
            difficulty = machine['difficulty']
            break

    if not system or not difficulty:
        print(f"Machine name '{machine_name}' not found on the website.")
        sys.exit(1)
    color = colors.get(difficulty, "unknown")

    template = f"""---
title: {machine_name} - {difficulty}
description: WU {machine_name} - {difficulty}
categories: [Writeup]
tags: [writeup]
template: doc
---
import {{ Image }} from 'astro:assets';
import banner from '../../../../assets/writeup/vulnlab/banner.jpeg';

<Image src={{banner}} alt="banner" format="avif" quality={{"mid"}}/>

# {machine_name}

| OS | Difficulty | Target |
|----|----|----|
| {system} | <span style="color:{color}">**{difficulty}**</span> | target |

## 🔭 Enumeration

## 👣 Foothold

## 🔄 Lateral Movement

## 🎯 Privilege Escalation
"""

    filename = f"{machine_name}-{difficulty}.mdx"
    with open(filename, "w") as file:
        file.write(template)

if __name__ == "__main__":
   main(sys.argv[1:])
