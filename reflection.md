# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game took a while to load, but eventually I was able to get it to run. 
- List at least two concrete bugs you noticed at the start  
  1. I would enter a number, but the hint would be wrong. ex. select 100, says go higher, but actual number is 49
  2. Press new game, it does not start a new game, says game over, try again
  3. Difficulty level is messed up, normal is 1 - 100 and hard is 1- 50
  4. Initially, the text box to entre the number was not there, I had to enter twice and then it came

---

##TF - Hint
I would ask the student to add the fixme at a method which contains keywords that describes the error or bug. Example, if error is in sidebar, will guide them to add the fix me near the line where it says sidebar. 


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
It was because of the alternating str() cast on the secret. This made wrong numerical comparisons or raised typeerror. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns are basically the script reloading everytime a widget is clicked. To ensure the app doesnt start from the beginning, the session state stores the variables at the end of the previous rerun and uses them to the new rerun
- What change did you make that finally gave the game a stable secret number?
got rid of the str casting and swapped the hint messages within the code. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
The ability of creating a virtual environment everytime I start a new project
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I will try to look more deeper into the changes that it is suggesting. I was kind of skimming through its suggestions
- In one or two sentences, describe how this project changed the way you think about AI generated code.
Ai generated code is awesome with minor code adjustments and fixing bugs. When it comes to complex tasks like creating pytests, it struggles to create reliable code at the first try itself. 
