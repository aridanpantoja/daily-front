import random

questions = [
    {
        "pergunta": "What does a doctype do?",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "How do you serve a page with content in multiple languages?",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "What kind of things must you be wary of when designing or developing for multilingual sites?",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "What are data- attributes good for?",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "Consider HTML5 as an open web platform. What are the building blocks of HTML5?",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "Describe the difference between a cookie, sessionStorage and localStorage.",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "Describe the difference between <script>, <script async> and <script defer>.",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "Why is it generally a good idea to position CSS <link>s between <head></head> and JS <script>s just before </body>? Do you know any exceptions?",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "What is progressive rendering?",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "Why you would use a srcset attribute in an image tag? Explain the process the browser uses when evaluating the content of this attribute.",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "Have you used different HTML templating languages before?",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "What is the difference between canvas and svg?",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "What are empty elements in HTML?",
        "categoria": "HTML",
        "subperguntas": []
    },
    {
        "pergunta": "What is CSS selector specificity and how does it work?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What is the difference between 'resetting' and 'normalizing' CSS? Which would you choose, and why?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Describe Floats and how they work.",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Describe z-index and how stacking context is formed.",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Describe BFC (Block Formatting Context) and how it works.",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What are the various clearing techniques and which is appropriate for what context?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "How would you approach fixing browser-specific styling issues?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "How do you serve your pages for feature-constrained browsers?",
        "categoria": "CSS",
        "subperguntas": [
            "What techniques/processes do you use?"
        ]
    },
    {
        "pergunta": "What are the different ways to visually hide content (and make it available only for screen readers)?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Have you ever used a grid system, and if so, what do you prefer?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Have you used or implemented media queries or mobile specific layouts/CSS?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Are you familiar with styling SVG?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Can you give an example of an @media property other than screen?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What are some of the 'gotchas' for writing efficient CSS?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What are the advantages/disadvantages of using CSS preprocessors?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Describe what you like and dislike about the CSS preprocessors you have used.",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "How would you implement a web design comp that uses non-standard fonts?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Explain how a browser determines what elements match a CSS selector.",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Describe pseudo-elements and discuss what they are used for.",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Explain your understanding of the box model and how you would tell the browser in CSS to render your layout in different box models.",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What does * { box-sizing: border-box; } do? What are its advantages?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What is the CSS display property and can you give a few examples of its use?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What is the difference between inline and inline-block?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What is the difference between the 'nth-of-type()' and 'nth-child()' selectors?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What is the difference between a relative, fixed, absolute and statically positioned element?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What existing CSS frameworks have you used locally, or in production? How would you change/improve them?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Have you used CSS Grid?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Can you explain the difference between coding a web site to be responsive versus using a mobile-first strategy?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Have you ever worked with retina graphics? If so, when and what techniques did you use?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Is there any reason you'd want to use translate() instead of absolute positioning, or vice-versa? And why?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "How is clearfix css property useful?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Can you explain the difference between px, em and rem as they relate to font sizing?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "Can you give an example of a pseudo class? Can you provide an example use case for a pseudo class?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What is the difference between a block level element and an inline element? Can you provide examples of each type of element?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What is the difference between CSS Grid and Flexbox? When would you use one over the other?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What is the difference between fixed, fluid and responsive layouts?",
        "categoria": "CSS",
        "subperguntas": []
    },
    {
        "pergunta": "What did you learn yesterday/this week?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "What excites or interests you about coding?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "What is a recent technical challenge you experienced and how did you solve it?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "When building a new web site or maintaining one, can you explain some techniques you have used to increase performance?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Can you describe some SEO best practices or techniques you have used lately?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Can you explain any common techniques or recent issues solved in regards to front-end security?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "What actions have you personally taken on recent projects to increase maintainability of your code?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Talk about your preferred development environment.",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Which version control systems are you familiar with?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Can you describe your workflow when you create a web page?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "If you have 5 different stylesheets, how would you best integrate them into the site?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Can you describe the difference between progressive enhancement and graceful degradation?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "How would you optimize a website's assets/resources?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "How many resources will a browser download from a given domain at a time?",
        "categoria": "general questions",
        "subperguntas": [
            "What are the exceptions?"
        ]
    },
    {
        "pergunta": "Name 3 ways to decrease page load (perceived or actual load time).",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "If you jumped on a project and they used tabs and you used spaces, what would you do?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Describe how you would create a simple slideshow page.",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "If you could master one technology this year, what would it be?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Explain the importance of standards and standards bodies.",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "What is Flash of Unstyled Content? How do you avoid FOUC?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Explain what ARIA and screenreaders are, and how to make a website accessible.",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Explain some of the pros and cons for CSS animations versus JavaScript animations.",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "What does CORS stand for and what issue does it address?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "How did you handle a disagreement with your boss or your collaborator?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "What resources do you use to learn about the latest in front end development and design?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "What skills are needed to be a good front-end developer?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "What role do you see yourself in?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Can you explain what happens when you enter a URL into the browser?",
        "categoria": "general questions",
        "subperguntas": []
    },
    {
        "pergunta": "Describe the difference between SSR and CSR. Discuss the pros and cons.",
        "categoria": "general questions",
        "subperguntas": [
            "Are you familiar with static rendering?",
            "Rehydration?"
        ]
    }
]

chosen_question = random.choice(questions)

readme_file = "README.md"
header = "# Daily Front 🎨\n\n"
question = f"""### Question: {chosen_question["pergunta"]}\n ### Category: {chosen_question["categoria"]}"""
content = f"{header} {question}"

with open(readme_file, "w", encoding="utf-8") as file:
    file.write(content)