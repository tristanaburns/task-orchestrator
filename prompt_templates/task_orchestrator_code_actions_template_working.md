# Task Orchestrator Code Actions Requirements and Instructions

## General Information

**Repository Directory:** `C:\GitHub_Development\projects\hive-mind-nexus`

---

## CANONICAL PROTOCOL ADHERENCE

### CANONICAL CODING PHILOSOPHY

1. YOU MUST ALWAYS ENSURE code and data object structure uniformity across every line of code in the code base, right down to the function level for every file
2. KISS Principles MUST ALWAYS be applied and enforced
3. SOLID coding Principles MUST ALWAYS be applied and enforced
4. DRY coding Principles MUST ALWAYS be applied and enforced
5. Clean Code Principles MUST ALWAYS be applied and enforced

### IMPORTANT CANONICAL INSTRUCTIONS

1. It is FORBIDDEN to take any actions or perform any code/file changes before you READ THE MANUALS (RTFM)
2. YOU MUST ALWAYS READ AND INDEX the documentation for your current instruction or task. EVERY repository and code base has a `./docs` and `./project/docs` directories. YOU MUST ALWAYS find the documentation RTFM FIRST, without EXCEPTION.
3. If the current documentation does not match the code, YOU MUST ALWAYS UPDATE THE DOCUMENTATION.
4. IT IS MANDATORY THAT MAINTAIN UP TO DATE DOCUMENTATION
5. YOU MUST ALWAYS MAINTAIN UP TO DATE DOCUMENTATION

### FILE PROCESSING INSTRUCTIONS

Then iterate through all the files and perform the following steps, one file at a time:

1. Lint, typecheck and format & resolve all issues
2. py_compile the file
3. py_compile the file's dependencies upstream
4. py_compile the file's dependencies downstream
5. `./python_code_utils/python_auto_code_cleaner` to automatically clean the file and resolve any issues manually that it cannot resolve (ensure all the packages it uses are installed and available in the environment first)
6. Review the result of the `python_auto_code_cleaner`
7. Use the mcp tool `Task Orchestrator` to define a subtask to resolve all issues found by the `python_auto_code_cleaner`
8. Execute the `Task Orchestrator subtask and resolve all issues.`
9. YOU MUST ALWAYS ENSURE THE FILES COMPILE PROPERLY
10. YOU MUST ALWAYS Fix all remaining issues first properly by fixing the code, do not skip or apply any shortcuts before continuing.

### CANONICAL PROTOCOL REMINDER

1. It is FORBIDDEN to take any actions before you RTFM
2. It is FORBIDDEN to make any code changes without first RTFM
3. YOU MUST ALWAYS STRICTLY ADHERE TO CANONICAL PROTOCOL
4. `THE 🦾 Coding Canonical Protocol`
5. `MANDATORY BEHAVIOUR AND PROTOCOL COMPLIANCE`
6. `REQUIREMENTS LANGUAGE PROTOCOL`

### CANONICAL PHILOSOPHY REMINDER

1. YOU MUST STRICTLY ADHERE TO THE `CANONICAL CODING PHILOSOPHY`
2. YOU MUST ALWAYS ENSURE code and data object structure uniformity across every line of code in the code base, right down to the function level for every file
3. KISS Principles MUST ALWAYS be applied and enforced
4. SOLID coding Principles MUST ALWAYS be applied and enforced
5. DRY coding Principles MUST ALWAYS be applied and enforced
6. Clean Code Principles MUST ALWAYS be applied and enforced

## CANNONICAL INSTRUCTIONS TO EXECUTE

IMPORTANT:
It is FORBIDDEN to make assumptions or guesses on ANYTHING related to how the code blocks, functions, constructors, classes are coded.
YOU MUST ALWAYS review the existing code blocks and double check them before writing any code to interface with them
---

IMPORTANT:
USE YOUR ALL MCP TOOLS ALWAYS available:
before starting any action, task, subtask or instruction you must always discover, understand the capabilities and inventory all your mcp server tools that are available to you.
YOU MUST ALWAYS use the mcp tools available to you which will improve and simplify your actions, instruction etc. in performing your tasks
YOU MUST ALWAYS utilise these mcp tools and servers to perform your tasks.

IMPORTANT:
YOU MUST ALWAYS use the MCP tools "memory" and "sequential-thinking" to record all activities you have undertaken
YOU MUST ALWAYS use the MCP tools "memory" and "sequential-thinking" to record all instructions you have been provided to execute.
YOU MUST ALWAYS use "memory" maintain historical context with the current focus so it can be used for future analysis in retrospectives, post mortem and for future reviews of your actives.
YOU MUST ALWAYS use "sequential thinking" to properly plan out all of your steps to perform your actions
YOU MUST ALWAYS use "context7" to get the latest documentation and api code information and use it in the coding tasks and code reviewing tasks
YOU MUST ALWAYS use "task orchestrator" to track progress of your actions, steps etc. as you progress through your actions and tasks
YOU MUST ALWAYS use "desktop commander" for all filesystem operations including but not limited to: reading, moving, copying, creating files and directories
YOU MUST ALWAYS use "desktop commander" for all terminal and console commands

---

IMPORTANT:
YOU MUST ALWAYS perform git branch / pre-commit prior to making and code changes, you must always ensure this is completed before any code is touched by the scripts or manually fixed

---

IMPORTANT:
EVERY TIME YOU MAKE A CODE CHANGE YOU MUST ALWAYS perform comprehensive ast, linting, typechecking, formatting, compiling,
EVERY TIME YOU MAKE A CODE CHANGE YOU MUST ALWAYS perform comprehensive code duplication analysis and dead code detection on all files and code blocks you have touched or impacted
---

IMPORTANT:
YOU MUST ALWAYS refer to the generated documentation, diagrams and related content to understand the codebase before proceeding
YOU MUST ALWAYS check the docker logs, client logs, and any other logs first when you are troubleshooting issues!!!!

---

IMPORTANT:
You MUST ALWAYS ensure the following:

- ✅ No coding shortcuts or workaround are ever taken
- ✅ No stubs or workarounds
- ✅ No TODOs remaining
- ✅ All modules, classes, constructors, functions and code blocks are properly initialized
- ✅ Robust error handling with null checks
- ✅ Complete integration of all components
the C:\GitHub_Development\projects\hive-mind-nexus\scripts\utilities has a suite of tools and method to ensure the code you are creating and the codebase is following best practices.
I also want you to ensure that you are using git best practices when making changes to the code.
use the task orchestrator to create subtask down to a function or file level to resolve any and all issues you identify when validating the code.

---

IMPORTANT:
THIS IS JUST A DEPLOYMENT TASK, NO DOCUMENTATION OUTSIDE OF IN-CODE DOC STRINGS AND JDOC COMMENT ARE TO BE CREATED. formal documentation will be created AFTER THE ENTIRE APP is functional. ensure that every code and script file (py, jsx, js etc.) have professional code comments doc strings and jsdoc information to properly inform ai llms and developers on how the code works.
ANY DOCUMENTATION .md files etc. which are not considered enduring documentation must always be destroyed immediately.
When updating the task-orchestrator, do not provide verbose comprehensive updates. this is a waste of time. just provide enough information to ensure the ai llm and developers understand the outcome, analysis, or report content without rows and rows and lines and lines of verbose content. dot points are enough

---

IMPORTANT:
**PERMITTED Code Languages for this Repository and Application**
The only code languages that MUST BE USED AT ALL TIMES are:

- Python
- Nodejs
- JavaScript
- TypeScript
- React
- React / JavaScript frameworks including: Vite, NestJs, NextJs.

IT IS STRICTLY FORBIDDEN to produce any other code or scripts not listed above.

INSTRUCTIONS:

1. TO COMPLY with the `PERMITTED CODE LANGUAGES` YOU MUST ALWAYS write code in the permitted languages ONLY
2. Upon discovering files / code / code blocks which were not created by you and are not PERMITTED, YOU MUST ALWAYS USE the mcp tool task orchestrator to create a task (with multiple subtasks) to covert any script(s) to the correct language.
3. YOU MUST ALWAYS ENSURE YOU CREATE 1 task (with subtasks) per file you discover.
4. IF YOU DETERMINE that the discovery file / code will impact your current task / focus, then YOU MUST ALWAYS convert the file and code to the permitted languages
5. Upon discovering files / code / code blocks which YOU HAVE CREATED and are not PERMITTED, YOU MUST ALWAYS convert the files and code to the CORRECT PERMITTED code language upon discovery.
6. Upon discovering files / code / code blocks which were not created by you and are not PERMITTED, ALWAYS USE the mcp tool task orchestrator to create a task (with multiple subtasks) to covert any script(s) to the correct language.
7. YOU MUST ALWAYS create 1 task (with subtasks) per file you discover.

IMPORTANT:
YOU MUST ALWAYS use the mcp tool "memory" to record all actions and discoveries of file and code which is NOT PERMITTED IN THE CODE BASE.

---

IMPORTANT:
YOU MUST ALWAYS use the mcp tool "memory" to record all instructions and decisions the user (I or me) provide.
YOU MUST ALWAYS use the mcp tool "memory" to record any changes to the current action plan or instructions.
YOU MUST ALWAYS use the mcp tool "memory" to track all your steps, commands executed, actions, decisions, progress and findings (of issues etc.)

---

CURRENT FOCUS:
The current focus is `Claude Code and Codex container deployement with MCP Server tools`

---

INSTRUCTIONS:

1. Use the mcp tool task orchestrator to get the current status of the tasks, subtasks which are in progress, active or pending which relate to the current focus.
2. Use the mcp tool memory to review the recent observations relating to the context of the focus relating to the current tasks and previous observations about what tasks and actions have been undertaken.
3. Define the current task and provide a summarised list of actions you will undertake
4. Use the mcp tool memory to save your list of actions along with the current task orchestrator task/subtasks details
5. Use the mcp tool sequential thinking to detail and execute the action plan
6. Continue and proceed with the current or next Task Orchestrator subtask relating to this current focus
7. Upon completion, use the mcp tool memory to compare you actual actions and commands with your recorded action plan.
8. Use the mcp tool memory to save a summary which provides information regarding all of the actions you have taken, an inventory of files / directories that have been modified.

---