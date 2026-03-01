# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game took a while to load, but eventually I was able to get it to run. 
- List at least two concrete bugs you noticed at the start  
  1. I would enter a number, but the hint would be wrong. ex. select 100, says go higher, but actual number is 49
  2. Press new game, it does not start a new game, says game over, try again
  3. Difficulty level is messed up, normal is 1 - 100 and hard is 1- 50

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude AI
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI did see the normal and hard ranges were switched. I manually looked at the section it cited to confirm
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI said on of the pytest should work. I ran pytest in the terminal and noticed that it was giving an error. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran the pytest and saw them all passed. I also took a look at the app to see if the bug was fixed
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran pytest and it said there was an import error as it was missing a package. I manually imported that package and everything worked. 
- Did AI help you design or understand any tests? How?
AI did help me to understand the test by adding clear variable names and some comments along with some emojis. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
