import requests
import sys
import json

colors = {
    "Easy": "green",
    "Medium": "yellow",
    "Hard": "red",
    "Insane": "purple"
}

badges = {
    "Easy": "success",
    "Medium": "caution",
    "Hard": "danger",
    "Insane": "tip"
}

def main():
    category = input("Choose a category: 1 for machines, 2 for chains: ")
    if category == "1":
        url = "https://api.vulnlab.com/api/v1/machines"
    elif category == "2":
        url = "https://api.vulnlab.com/api/v1/chains"
    else:
        print("Invalid category.")
        sys.exit(1)

    machine_name = input("Enter the machine name: ").capitalize()

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
    badge = badges.get(difficulty, "unknown")

    template = f"""---
title: {machine_name}
description: WU {machine_name}
categories: [Writeup]
tags: [writeup]
template: doc
sidebar:
  order: A CHANGER
  badge:
    text: '{difficulty}'
    variant: '{badge}'
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
   main()
