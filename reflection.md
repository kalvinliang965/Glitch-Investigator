# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
```
The game has a developer debug info tab that shows the secret, the correct hidden value, attempts user has made, score, difficulty of the game, and history log.

User could enter their guesses in the input tab. There is a submit guess button user could click on to submit their guess. After clicking that button, the value is being logged to the history field inside developer debug info. 
```
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

```

bug i have noticed is that 
    - the hint is reverse. 
    - the new game button wont start a new game. secret changes but attempt does not get reset.
    - for my first submit, the value is not being logged.

```

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

```
Claude
```

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

```
while i was asking AI to statically analyzing the bug, it correctly point out the flaw inside get_ranage_for_difficulty() such that `hard` should have wider range than normal and easy. However the code show that `hard` has smaller range.
```

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

```
When i ask AI to write testcase for TDD, the compilation crashed because im importing the util function wrong. AI didnot recognize it and believe it compiled successfully, which failed when i do it manually. The solution to this was adding __init__.py to the root directory and the `tests` directory.
```

```
I asked AI on specific glitch  "the hint is reverse". I pointed me the correct code that the issue is inside check_guess() and the comparator is reversed. However it mislead me to think the variable nameing is wrong and didn't actually flip the comparsion in the correction.

```

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
```
i wrote actual test function to test the code and tried again on the website.
```
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

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
