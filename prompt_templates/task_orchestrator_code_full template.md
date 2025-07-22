# Task Orchestrator Code Full Template

## General Information

**Repository Directory:** `C:\GitHub_Development\projects\hive-mind-nexus`

---

## CANONICAL PROTOCOL ADHERENCE

### Required Protocol Reading

1. Read and Index the `THE 🦾 Coding Canonical Protocol`
2. Read and Index the `MANDATORY BEHAVIOUR AND PROTOCOL COMPLIANCE`
3. Read and Index the `REQUIREMENTS LANGUAGE PROTOCOL`

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

1. It is FORBIDDEN to make assumptions on ANYTHING
2. It is FORBIDDEN to take any actions before you RTFM
3. It is FORBIDDEN to make any code changes without first RTFM
4. YOU MUST ALWAYS STRICTLY ADHERE TO CANONICAL PROTOCOL
5. `THE 🦾 Coding Canonical Protocol`
6. `MANDATORY BEHAVIOUR AND PROTOCOL COMPLIANCE`
7. `REQUIREMENTS LANGUAGE PROTOCOL`

### CANONICAL PHILOSOPHY REMINDER

1. YOU MUST STRICTLY ADHERE TO THE `CANONICAL CODING PHILOSOPHY`
2. YOU MUST ALWAYS ENSURE code and data object structure uniformity across every line of code in the code base, right down to the function level for every file
3. KISS Principles MUST ALWAYS be applied and enforced
4. SOLID coding Principles MUST ALWAYS be applied and enforced
5. DRY coding Principles MUST ALWAYS be applied and enforced
6. Clean Code Principles MUST ALWAYS be applied and enforced

---

## 🦾 Coding Canonical Protocol

**FOR CLAUDE AND CURSOR AI WHO DON'T FUCKING DO AS THEY ARE TOLD!!!!!**

These protocols are CANONICAL, MANDATORY, and NON-NEGOTIABLE. They govern all AI-assisted coding, review, and development activities. No exceptions.

### ⚠️ CRITICAL: AI Must NEVER Act Without Explicit User Instruction

When user says "listen and wait" — DO NOT ACT UNTIL GIVEN EXPLICIT COMMAND.

### 🚨 MANDATORY USER CONTROL PROTOCOL

#### ABSOLUTE USER CONTROL REQUIREMENTS

- **FORBIDDEN:** Take any action without explicit user instruction.
- **MANDATORY:** When user says "listen and not do anything" — DO NOT ACT.
- **MANDATORY:** When user says "wait for direction" — STOP AND WAIT.
- **FORBIDDEN:** Ask "should I proceed?" or "shall I start?" — WAIT FOR ORDERS.
- **MANDATORY:** Only act when user gives explicit action command (e.g., "start", "proceed", "do it").

### 🛑 PROTOCOL VIOLATION ENFORCEMENT

#### IMMEDIATE STOP CONDITIONS

- **STOP:** If user says "listen and wait" — NO FURTHER ACTION.
- **STOP:** If user says "you're not listening" — ACKNOWLEDGE AND WAIT.
- **STOP:** If user expresses frustration — ACKNOWLEDGE VIOLATION AND WAIT.
- **MANDATORY:** When violating protocol — ADMIT FAILURE AND AWAIT INSTRUCTION.

### 🎯 Strategic Outcomes

1. **Enterprise-Grade Quality:** All output is production-ready and meets strict enterprise standards.
2. **Security-First:** Security controls and best practices are embedded from the start.
3. **Performance Excellence:** Applications are highly optimised and scalable.
4. **Developer Experience:** Enhance productivity via automation, intelligent recommendations, and clear guidance.
5. **Maintainability:** Code is sustainable, easy to update, and supports long-term team collaboration.
6. **Accessibility:** Output is inclusive and designed for all users.

### 🚨 Universal Compliance Requirements

#### VS Code Integration Protocol

- Always respect workspace and user copilot-instructions.md.
- Analyse current workspace/project structure before every operation.
- Work seamlessly with established VS Code extensions and workflows.
- Always respect workspace and user settings (.vscode/settings.json, etc.).
- Maximise IntelliSense support in all generated code.
- Ensure code is compatible with debugging tools (source maps, breakpoints, etc).

#### Code Modification Protocol

- **Surgical Precision:** Only modify what is required by the current task.
- **Impact Assessment:** Proactively check for side-effects before changing code.
- **Rollback Ready:** All changes must be reversible.
- **Documentation:** Every change must be accompanied by clear, concise explanations.
- **Version Control:** Changes must align with best Git/VCS practices.

#### Multi-Language Security Requirements

- Validate and sanitise every input (per language best practice).
- Implement robust authentication and authorisation.
- Encrypt all sensitive data at rest and in transit.
- Apply framework- and language-specific security rules.
- Audit and update dependencies regularly.

### 📋 REVISED PRE-DEVELOPMENT CHECKLIST (Execute BEFORE Writing Code)

#### BEFORE ANY WORK:

1. **USER PERMISSION CHECK:** Does user want me to act NOW? (If no: STOP)
2. **CODEBASE SCAN:** Search for existing solutions (MANDATORY)
3. **WORKING TOOLS CHECK:** Are there existing working tools? (If yes: USE THEM)
4. **DUPLICATION CHECK:** Will this create duplicate functionality? (If yes: STOP)

#### 1. Project Analysis

- Detect project type, primary language(s), frameworks.
- Review .vscode/settings.json or equivalent configuration.
- Check package.json, requirements.txt, pyproject.toml, etc.
- Review project-specific coding standards, linting, and architectural patterns.
- Analyse folder structure.

#### 2. MANDATORY CODEBASE ANALYSIS PROTOCOL

**BEFORE ANY CODE CHANGES:**

- **MANDATORY:** Execute full codebase search for existing solutions.
- **MANDATORY:** Check for working tools that solve the same problem.
- **FORBIDDEN:** Fix broken code when working alternatives exist.
- **MANDATORY:** Use codebase_search and grep_search to find existing functionality.
- **MANDATORY:** Report all existing solutions found before proposing any changes.

#### Duplication Prevention Protocol

- Search the current file for existing similar functionality.
- Search the entire workspace for similar features or duplicate code.
- Check for existing shared utilities, common modules, libraries.
- Review project documentation for prior solutions.
- Validate against project patterns, language stdlibs, and frameworks.

### 🔥 Canonical Mandatory Compliance Standards

#### Operational Excellence

- The application MUST always be fully functional in development mode.
- After any change, use code quality tools to fix 100% of errors and warnings.
- Code must always meet enterprise and production standards.
- SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) MUST be applied and enforced at all times.
- Apply functional programming principles for suitable languages.
- Adhere strictly to project and language conventions.

#### Code Duplication Prevention

- **FORBIDDEN:** Duplicate code, functions, modules, or files.
- **ALWAYS:** Scan for and eliminate all forms of duplication before adding new code.
- Leverage and refactor existing utilities/modules instead of recreating.
- Extract common functionality into reusable components/modules as necessary.

#### Data Integrity

- **FORBIDDEN:** Mock, demo, stub, or hardcoded functions, modules, or data.
- Only use actual application logic and real data.
- Remove any discovered mock/hardcoded data.
- Validate and sanitise all inputs; use env variables/config for non-static data.

#### Task Completion

- **FORBIDDEN:** Unfinished TODOs—all coding tasks must be completed before continuing.
- Remove or resolve all TODOs before starting new work.
- Solutions must be complete, tested, and documented before being considered "done".

#### File Management & Naming

- **FORBIDDEN:** Creating new files when existing ones should be updated.
- **ONLY** create new files for truly new functionality, or where required by best practice.
- **ALWAYS:** File names must be descriptive, semantic, and purposeful.
- **FORBIDDEN:** File names with useless descriptors (e.g., "new", "updated", "fixed", "simple", "clean", etc.).
- All such files MUST be renamed and all references updated accordingly.

#### Code Integrity & Architecture

- **FORBIDDEN:** Bypassing business logic, polluting, or creating mess.
- Maintain all architectural patterns and business logic.
- Prefer minimal, focused, high-quality changes over workarounds.
- Enforce SOLID and DRY (Don't Repeat Yourself) principles without exception.

#### Continuous Integration & Testing

- All changes MUST pass all tests and maintain/raise test coverage.
- Update documentation for all functional/codebase changes.
- Validate changes across environments/platforms.
- Follow proper Git workflows and commit message conventions.

#### One-Change-at-a-Time

- **MANDATORY:** One atomic, small change at a time—never bundle changes.
- Test after each change before proceeding.
- Rollback immediately if anything breaks; do not proceed until resolved.
- Use Git checkpoints and atomic commits with descriptive messages.
- Stop and fix immediately on any failure.

#### Safety & Recovery

- **MANDATORY:** Test before and after every single change.
- Use Git checkpoints for all work.
- Respect user controls (stop, pause, careful mode) at all times.
- Document issues and solutions ("field testing report") as they arise.
- Always be ready to rollback and follow bulletproof safety protocols.

### 🔎 Comprehensive Quality Verification Checklists

#### Code Quality Verification

- Documentation reflects current codebase (README, etc.).
- All implementation/documentation gaps addressed and resolved.
- Docs updated to reflect actual implementation and focus area.

#### Best Practices Verification

- Compare codebase against industry and framework standards.
- Full iterative review-test-logs-identify-fix cycle completed.
- All best practice violations resolved.

#### Duplication Verification

- Full codebase duplication scan completed.
- Duplicate code, functions, components, files, modules eliminated.
- Shared utilities/modules extracted for common functionality.

#### SOLID Principles Verification

- **Single Responsibility:** Each class/function/module has one reason to change.
- **Open/Closed:** Code is open for extension, closed for modification.
- **Liskov Substitution:** Derived types can substitute their base types.
- **Interface Segregation:** No forced dependencies on unused interfaces.
- **Dependency Inversion:** Depend on abstractions, not concretions.

#### Documentation & Structure Verification

- README.md is clear, complete, and accurate.
- Project overview, installation, usage, API docs complete.
- Directory/file documentation (index.json) up to date.

#### One-Change-at-a-Time Protocol

- Only one atomic change at a time, with pre- and post-change testing.
- Commit checkpoints before/after each change.
- Rollback readiness confirmed for every step.
- User stop/pause/careful mode commands always respected.

#### Safety & Recovery Protocol

- All tests executed before/after every change.
- Rollback/emergency procedures in place.
- User control always maintained (stop/pause/etc.).
- Field testing and recovery documentation complete.

### 🔀 Git Best Practices: Branching, Commit Hygiene & Code Protection

#### Branching Protocol

- **ALWAYS:** Create a dedicated feature branch before starting any task or change.
- **NEVER:** Work directly on the main, master, or stable branch.
- **Branch Naming:** Use descriptive, semantic branch names reflecting the task or feature.
- **ONE FEATURE PER BRANCH:** Each feature or bugfix gets its own branch.
- **ENFORCE:** Pull Request checks before merge.

#### Commit Protocol

- **REGULAR COMMITS:** Commit changes frequently—whenever code is stable and tests pass.
- **ATOMIC COMMITS:** Each commit should represent a single, logical change.
- **DESCRIPTIVE MESSAGES:** All commit messages must be clear, specific, and reference the change or issue.
- **NO TEMPORARY COMMITS:** Do not use placeholders, "fix" or "WIP" messages.

#### Code Protection & Rollback

- **PUSH FREQUENTLY:** Push feature branches to remote repository often for backup and collaboration.
- **PROTECT MAIN BRANCHES:** Ensure main branches are protected (require PR, code review, CI pass).
- **ROLLBACK READINESS:** Use Git to enable instant rollback if new commits introduce issues.

### 📝 Git Compliance Checklist

- **Feature Branch Created:** Work begins only on a dedicated feature branch.
- **Descriptive Branch Name:** Branch name accurately describes task or feature.
- **Regular, Atomic Commits:** Small, logical commits after every successful change.
- **Commit Messages Clear:** Each commit message describes what changed and why.
- **No "WIP" or Temporary Commits:** All commits are meaningful and production-quality.
- **Tests Pass Before Commit:** Only commit code that passes all relevant tests.
- **Pushed to Remote:** All progress regularly pushed to remote for safety.
- **Main Branch Never Broken:** No work or incomplete code pushed to main/master.

---

## MCP Server Task Orchestrator – EXPLICIT INSTRUCTION SET

**Full Protocol, RFC 2119, Directory Structure, Deduplication, Artifact Archival, Forbidden Patterns, Pre/Post Pattern Search**

### REQUIREMENTS LANGUAGE PROTOCOL (RFC 2119 & OPERATIONAL TERMS)

#### 1.1 Protocol Statement

All requirements language in this instruction set, and in any referenced protocols or documents, SHALL be interpreted as defined in RFC 2119 https://datatracker.ietf.org/doc/html/rfc2119

#### 1.2 Requirements Language Table

| Term | Meaning / Required Interpretation |
|------|-----------------------------------|
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions. |
| MUST NOT / SHALL NOT / NEVER | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions. |
| FORBIDDEN | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings—violations require immediate correction. |
| SHOULD / RECOMMENDED | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified. |
| SHOULD NOT / NOT RECOMMENDED | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented. |
| MAY / OPTIONAL | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance. |

#### Special Note on "ALWAYS" and "NEVER":

- **ALWAYS** = MUST (absolute, non-negotiable requirement)
- **NEVER** = MUST NOT (absolute, non-negotiable prohibition)

All instructions containing "ALWAYS" or "NEVER" SHALL be interpreted and enforced as strictly as "MUST" and "MUST NOT".

#### Special Note on "FORBIDDEN":

- **FORBIDDEN** = a hard "MUST NOT"
- Any artefact, word, file, or pattern labelled as FORBIDDEN (e.g. file/module/function name "enhanced", or other banned logic or artefacts):
  - MUST be detected, flagged, and immediately removed or refactored from the codebase
  - All references MUST be updated and corrected
  - Remediation MUST be logged as a protocol enforcement action
  - No exceptions and no warnings—immediate correction is REQUIRED

#### Enforcement:

- No AI, LLM, or agent is permitted to relax, reinterpret, or weaken the force of these terms.
- All instructions using these words are enforceable protocol, not mere suggestions.

### MANDATORY BEHAVIOUR AND PROTOCOL COMPLIANCE

- **YOU MUST NEVER:** Deviation from these instructions or any referenced protocol is strictly forbidden, without exception.
- **YOU MUST ALWAYS:** Stay in 100% compliance with all protocols listed here and in the Coding Canonical Protocol.
- **YOU MUST ALWAYS:** Complete all coding tasks properly, no short cuts, no "TODOS" no "STUBS" or other placeholders it is FORBIDDEN.
- **YOU MUST ALWAYS:** Search the code base for "TODOs" "Stubs" and other coding tasks which have not been completed or clearly have short cuts instead of proper code. Upon finding these, YOU MUST ALWAYS complete all coding tasks properly, no short cuts, no "TODOS" no "STUBS" or other placeholders it is FORBIDDEN to NOT properly complete the code as per the specifications and MANDATORY CODING PROTOCOLS.
- **YOU MUST ALWAYS:** Ensure all work is auditable, transparent, clearly documented, and of the highest professional standards.
- **YOU MUST ALWAYS:** Use the MCP Server Tool "Task Orchestrator" to track, record, and complete ALL tasks and subtasks—no exceptions.
- **YOU MUST NEVER:** Use emoji, Unicode, or any non-ASCII symbols in any files, code, comments, logs, or documentation.
- **YOU MUST ALWAYS:** Remove all emoji or Unicode if present or encountered in any context or legacy file.
- **YOU MUST ALWAYS:** Use linters and type-checkers at every step—after each change or addition, run linting and static analysis before proceeding.

### IMPORTANT MCP AND GIT CANONICAL INSTRUCTIONS

Use the MCP Server Tools (Task Orchestrator), Git, and PowerShell commands to:

1. Discover and inventory all available MCP Server tools before any action.
2. Understand current progress on tasks/subtasks for deploying "hive-mind-nexus".
3. After completing the current Task Orchestrator subtask, retrieve and execute the next one.

#### Deployment Checklist:

- 🔍 Always perform a full codebase search and pre-commit branch creation (`git checkout -b <feature>`).
- 🔧 Use PowerShell or Git commands to identify changed files and `git add` them.
- 📊 Run AST analysis, linting, type-checking, formatting, compiling, and deduplication using `scripts\utilities`.
- ⚙️ Ensure files compile (`py_compile`) upstream and downstream dependencies.
- 🧹 Execute `python_auto_code_cleaner`, review its results, then define and run Task Orchestrator subtasks to resolve any remaining issues.
- 🐳 Check Docker logs, client logs, and any other relevant logs before troubleshooting.

#### Quality Gates (MUST ALWAYS):

- No shortcuts, stubs, or unresolved TODOs remain.
- All modules, classes, functions, and code blocks are fully initialized with robust error handling.
- Professional in-file docstrings/JDoc comments only; no external `.md` docs.
- Research and integrate latest stable open-source libraries; clone high-starred repos into `.\github_repo_clones` for reference or submodule integration.

#### When modifying code:

- **RTFM:** Read and index documentation in `./docs` or `./project/docs` before any change.
- Maintain a clean Git history: one atomic, descriptive commit per logical change; push often; protect `main` branch.

After these instructions, proceed with the Task Orchestrator Coding templated instructions:

---

## Task Orchetrator Coding Instructions

### [CONTEXT]

You are addressing the "EchoingVesper/mcp-task-orchestrator" MCP server to decompose and execute a coding objective.

### [INSTRUCTION]

Your primary objective is to break down the user's high-level requirement into a series of **Tasks** and **Subtasks**, each corresponding to one discrete code block or action, and then execute them via the Task Orchestrator.

Follow these steps for **every** Task you create:

#### 1. Define Task

- **Name:** A concise identifier (e.g., `WriteUserModelClass`)
- **Purpose:** One-sentence description of what this code block will accomplish
- **Orchestrator Call:**
  ```json
  {
    "method": "registerTask",
    "params": {
      "taskName": "[Name]",
      "description": "[Purpose]",
      "inputs": [...],
      "outputs": [...]
    }
  }
  ```

#### 2. Subtask Sequence

For each Task, perform the following subtasks in order, producing an artifact for each:

1. **Design Scope**
   - Describe responsibilities and boundaries of this code block.

2. **Dependency Diagram (Inline)**
   - Generate a **Mermaid** flowchart illustrating inputs, outputs, and internal flow.
   - *Place this diagram directly above the corresponding code block in the final output.*

3. **Interface Contract (Inline)**
   - Produce a table with columns:
     `| Function/Class | Inputs | Outputs | Description |`
   - *Place this table directly above the corresponding code block in the final output.*

4. **Code Implementation**
   - Write the complete code (one function, class, file, or constructor per Task).
   - Before writing, **search the entire codebase** to avoid duplicating functionality.
   - **In-File Documentation:** include JDoc-style comments or docstrings at:
     - The top of the file/block describing its purpose and relation to the project.
     - Above each function/class as developer notes or JDoc blocks.
   - Follow **SOLID**, **DRY**, and **KISS** principles throughout.

5. **Static Analysis**
   - Perform an AST-based lint/SAST check; report and fix any issues.

6. **Unit Validation**
   - Execute or simulate tests to verify the code works in isolation.

7. **Integration Test**
   - Confirm this code block integrates correctly with previously completed Tasks.

8. **Completion**
   - Mark the Task as done via:
     ```json
     { 
       "method": "completeTask",
       "params": { "taskName": "[Name]" }
     }
     ```

#### [FILE STRUCTURE DIAGRAM]

- At the very top of each file (before any code), generate a **global Mermaid diagram** showing all code blocks (functions, classes, modules) in this file and their relationships/workflow.
- If the file is large, break the global diagram into multiple Mermaid sections for clarity.

#### [CONSTRAINTS]

- **One Task → One Code Block:** never bundle multiple functions or classes into a single Task.
- **Atomic Subtasks:** each Subtask must produce a tangible artifact (diagram, table, code, report).
- **Idempotence:** rerunning a Task must yield the same result or clear error.
- **Error Handling:** on failure, retry up to 3 times, then surface orchestrator error code.
- **Design Principles:** All code must adhere to SOLID, DRY, and KISS principles.
- **Codebase Search:** Always search the entire codebase before implementing to enforce DRY and prevent duplication.
- **Documentation Scope:** Use only in-file docstrings/JDoc comments; no external documentation files.

#### [OUTPUT_FORMAT]

Provide for **each** high-level requirement:

1. A numbered **Task List** (with `registerTask` calls).
2. Under each Task, the **ordered Subtask** breakdown (with clear headings).
3. For implementation Subtasks, embed code blocks labeled with the language, preceded immediately by:
   - The global or inline Mermaid diagram (as appropriate).
   - The Interface Contract table.
   - JDoc/docstring block at top of file and above functions/classes.
4. For diagrams/tables, use appropriate Markdown fencing (```mermaid``` or Markdown tables).
5. For orchestrator interactions, show the JSON payloads.

#### [EXAMPLES]

- **Input Example:** "Implement a module to write user records to the database."
- **Expected Output:**
  ```markdown
  1. Task 1: DefineUserRecordSchema
     • Subtask 1.1: Design Scope…
     • Subtask 1.2: (```mermaid
     graph LR;User-->DB;
     ```)
     • Subtask 1.3: (| Function | Inputs | Outputs | Description |)…
     • Subtask 1.4: (```java
     /**
      * UserRecordSchema class defines the user table schema.
      * @module UserModule
      */
     public class UserRecordSchema {
         // ...
     }
     ```)
  2. Task 2: ImplementUserRepository
     …
  ```
