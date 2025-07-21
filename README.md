# Task Orchestrator Database

This repository contains the database and configuration files for the MCP Task Orchestrator server.

## Contents

- `task_orchestrator.db*` - SQLite database files (main database, shared memory, and write-ahead log)
- `roles/` - Project role configurations and YAML files
- `logs/` - Database persistence and operational logs
- `server_state/` - Server state information

## Database Files

The SQLite database uses Write-Ahead Logging (WAL) mode, which creates these files:
- `task_orchestrator.db` - Main database file
- `task_orchestrator.db-shm` - Shared memory file
- `task_orchestrator.db-wal` - Write-ahead log file

## Usage

This database is used by the MCP Task Orchestrator server to:
- Store task breakdowns and subtask information
- Track task progress and completion status
- Maintain specialist role assignments
- Store artifacts and detailed work content
- Preserve session state and context

## Configuration

The task orchestrator server is configured to use this directory as its working directory via the Claude Desktop MCP configuration.

## Backup

This repository serves as a backup and version control system for the task orchestrator database, ensuring no task data is lost.

## Last Updated

Database last active: July 18, 2025
Repository created: July 21, 2025
