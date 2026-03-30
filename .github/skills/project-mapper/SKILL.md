---
name: project-mapper
description: "Use when: The user wants to map a new or existing codebase from `project_code.txt`. Generates `.agent/project_map.md`, `.agent/architecture.md`, and `.agent/session_memory.md` to organize project structure, architecture, and current context."
---

# Project Mapper Skill

When invoked, follow this multi-step workflow to analyze the codebase and generate the essential agent context files.

## Step 1: Read Project Data
1. Read the `project_code.txt` file (or other entry points if specified).
2. Analyze the workspace structure broadly to understand the project's purpose and layout.

## Step 2: Generate Project Map
Create or update `.agent/project_map.md`. Do not just dump code; instead, synthesize a high-level project map:
- **Project Goal:** What the project does.
- **Technologies:** Languages, frameworks, and tools used.
- **Run Commands:** How to run the project.
- **Test Commands:** How to test the project.
- **Main Modules:** Key components and directories.
- **Entry Points:** Main execution files.
- **File Relationships:** How important files interact.
- **Must-Read Files:** Which files an agent should read first when debugging or contributing.

## Step 3: Generate Architecture Document
Create or update `.agent/architecture.md`. This is deeper than the project map:
- **Data Flow:** How data moves through the system.
- **Request Lifecycle:** From input to output.
- **Folder Responsibilities:** What each directory is responsible for.
- **Naming Conventions:** Patterns used in the codebase.
- **Boundaries:** Separation of concerns.
- **Anti-patterns:** Forbidden patterns or bad practices specific to this codebase.

## Step 4: Generate Session Memory
Create or update `.agent/session_memory.md`. This prevents the agent from starting from scratch every time:
- **Last Architectural Decision:** Recent choices made.
- **Recently Changed Files:** Files that are actively being modified.
- **Open Issues:** Known bugs or tasks.
- **Assumptions:** Contextual assumptions made during development.
- **TODOs:** Future tasks or refactors.

## Completion
Once all three files are created or updated, notify the user that the project map, architecture, and session memory have been successfully scaffolded and are ready for future agent contexts.
