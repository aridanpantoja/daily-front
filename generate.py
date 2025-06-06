import random
from questions import questions

chosen_question = random.choice(questions)

content = f"""
<h1>Daily Front 🎨</h1>

<p>
    <b>A repository that uses Python and GitHub Actions to automate the generation of daily questions about front-end development. Perfect for anyone looking to practice and reinforce their knowledge consistently every day.</b>
</p>

<h2 id="daily-question">Daily Question 💬</h2>
<p>{chosen_question["pergunta"]} {" ".join(chosen_question["subperguntas"])}</p>

![CATEGORY](https://img.shields.io/badge/Category-{chosen_question["categoria"]}-blue) \

![SUBQUESTIONS](https://img.shields.io/badge/Subquestions-{len(chosen_question["subperguntas"])}-{"green" if len(chosen_question["subperguntas"]) > 0  else "red"})

<h2 id="tech-stack">Tech Stack 💻</h2>

[![My Skills](https://skillicons.dev/icons?i=python,git,github)](https://skillicons.dev)

<h2>Related</h2>

Here are some related projects

- [Front-end Developer Interview Questions](https://github.com/h5bp/Front-end-Developer-Interview-Questions)
- [Pokemmon Greeting](https://github.com/isyuricunha/pokemon-greeting)

<h2 id="license">License 📃 </h2>

This project is under [MIT](./LICENSE) license
"""

with open("README.md", "w", encoding="utf-8") as file:
    file.write(content)