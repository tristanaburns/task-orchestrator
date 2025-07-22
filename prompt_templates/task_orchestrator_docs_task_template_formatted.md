# Task Orchestrator Documentation Task Template

## CANONICAL DOCUMENTATION REQUIREMENTS AND INSTRUCTIONS

### IMPORTANT MANDATORY REQUIREMENT

- ALL CONTENT AND DOCUMENTATION CREATED WHICH DOES NOT HAVE ANY ENDURING PURPOSE SHALL BE DESTROYED IMMEDIATELY.
- ALL DOCUMENTATION NOT CREATED AND STORED IN THE CORRECT LOCATION SHALL BE IMMEDIATELY DESTROYED AND REJECTED.
- YOU MUST THEN RECREATE THE DOCUMENTATION WHICH IS AGAINST THE `Coding Canonical Protocol` and the DRY Principles.
- BREAKING THESE DOCUMENTATION PROTOCOLS IS STRICTLY FORBIDDEN.

### Documentation and Archival Requirements

1. YOU MUST ALWAYS create and maintain exactly **one** subdirectory per feature or module under the root `./docs/` (e.g., `./docs/<feature-name>/`). All documentation, diagrams, and related content must reside within its corresponding subdirectory. Any content outside this structure must IMMEDIATELY be moved into the appropriate feature/module subdirectory and placed in a `.draft/` subfolder until finalized.

2. YOU MUST ALWAYS follow and adhere to the Diátaxis documentation framework <https://diataxis.fr/start-here/>

3. IT IS STRICTLY FORBIDDEN TO CREATE ANY DOCUMENTATION outside of the `./docs/python_offline_bundle_kit` directory.

4. The following table defines the maximum amount of documentation. This SHALL BE STRICTLY ENFORCED. ANY ADDITIONAL DOCUMENTS CREATED WILL BE IMMEDIATELY DESTROYED:

| document        | Quantity | Description            |
| --------------- | -------- | ---------------------- |
| getting-started | Up to 1  | Tutorials              |
| user-guides     | Up to 1  | How-to guides          |
| how-to-guides   | Up to 1  | Task-specific guides   |
| reference       | Up to 1  | Information lookup     |
| architecture    | Up to 1  | Understanding-oriented |
| development     | Up to 1  | Developer resources    |
| examples        | Up to 1  | Practical examples     |
| reports         | Up to 1  | Technical reports      |

- IT IS FORBIDDEN TO CREATE DOCUMENTATION AND CONTENT FOR THE SAKE OF IT. IF IT'S NOT PROFESSIONAL, CONCISE AND ABSOLUTELY REQUIRED… IT MUST NOT BE CREATED.
- 1 README at the root of the toolkit
- 1 toolkit overview
- 1 how-to user guide

YOU MUST NOT PRODUCE ANY MORE DOCUMENTS OR CONTENT OUTSIDE OF THIS

5. YOU MUST ALWAYS ensure that each documentation file is no longer than 400–500 lines. Content should favour concise dot-point summaries and workflows illustrated with Mermaid diagrams over large blocks of text or paragraphs.

6. YOU MUST ALWAYS include a Mermaid diagram and a corresponding structure table at the top of each documentation file to define the core and key aspects of the feature or module.

---

## [CONTEXT]

You are addressing the "EchoingVesper/mcp-task-orchestrator" MCP server to decompose and execute a **documentation and archival** objective for the "hive-mind-nexus" codebase.

## [INSTRUCTION]

Your primary objective is to break down the user's documentation requirement into **Tasks** and **Subtasks**, one Task per document or content piece, then execute them via the Task Orchestrator to update, structure, and archive docs under `/docs/python_offline_bundle_kit`.

Follow these steps for **every** Task you create:

### 1. Define Task

- **Name**: e.g. `UpdateGettingStartedTutorial`
- **Purpose**: One-sentence description (e.g. "Bring the 'getting-started' tutorial up to date with current CLI flags and deployment steps.")
- **Orchestrator Call**:

```json
{
  "method": "registerTask",
  "params": {
    "taskName": "[Name]",
    "description": "[Purpose]",
    "inputs": ["docs/python_offline_bundle_kit/getting-started/tutorial.md"],
    "outputs": ["docs/python_offline_bundle_kit/getting-started/tutorial.md"]
  }
}
```

### 2. Subtask Sequence

1. **Diátaxis Classification**
   - Identify the document type (Tutorial, How-to, Reference, Explanation).

2. **Content Audit**
   - Compare existing content against current feature matrix; note gaps.

3. **Structure Outline**
   - Generate a Mermaid flowchart of the document's sections and navigation.

4. **Section Interface Table**
   - Produce a table: `| Section | Purpose | Diátaxis Type | Notes |`

5. **Content Update**
   - Edit or rewrite each section to match current code and Diátaxis guidance.
   - Embed code snippets, API calls, diagrams as needed.

6. **Link & Cross-Ref Check**
   - Verify all intra-docs links point to the correct files.

7. **Static Doc Lint**
   - Run markdown linters (spellcheck, link-check) and fix issues.

8. **Archival Snapshot**
   - Commit before/after versions of the doc, archive previous version in `/docs/python_offline_bundle_kit/archive/[date]/`.

9. **Completion**

```json
{
  "method": "completeTask",
  "params": { "taskName": "[Name]" }
}
```

## [DOCUMENTATION CONSTRAINTS]

- **Directory Structure** under `/docs/python_offline_bundle_kit/` **MUST** match exactly the table above.
- **In-file metadata**: each `.md` must start with:

```markdown
---
title: <Descriptive Title>
type: <tutorial|how-to|reference|explanation>
last_updated: YYYY-MM-DD
---
```

## [OUTPUT_FORMAT]

1. Numbered **Task List** with JSON `registerTask` calls.
2. Under each Task, **ordered Subtask** breakdown with headings.
3. For diagrams/tables, use Markdown fencing (`mermaid` or tables).
4. For orchestrator interactions, show JSON payloads.

## [EXAMPLE]

> "Bring `/docs/python_offline_bundle_kit/reference/api.md` up to date with latest REST endpoints."

Expected snippet:

```markdown
1. Task 1: UpdateAPIReference
   ```json
   { "method": "registerTask", … }
   ```

   1. Subtask 1.1: Diátaxis Classification – Reference
   2. Subtask 1.2: Content Audit…
   3. Subtask 1.3: Structure Outline

   ```mermaid
   graph LR
   API[API Reference] --> Endpoints[Endpoints Section]
   Endpoints --> GET[GET /config]
   Endpoints --> POST[POST /upload]
   ```

   4. Subtask 1.4: Section Interface Table

   | Section    | Purpose             | Diátaxis Type | Notes    |
   |------------|---------------------|---------------|----------|
   | GET Config | Retrieve config     | reference     | Updated |

   …
```
