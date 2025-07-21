# Task Orchestrator Database

This repository contains the database and configuration files for the MCP Task Orchestrator server.

## Contents

- `task_orchestrator.db*` - SQLite database files (main database, shared memory, and write-ahead log)
- `task_orchestrator_wrapper.py` - Python wrapper script that suppresses logging for JSON-RPC compatibility
- `claude_config_manager.py` - Automated Claude Desktop configuration manager
- `update_claude_config.bat` - Windows batch script to update configuration
- `update_claude_config.ps1` - PowerShell script to update configuration
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

## Automated Configuration Management

This repository includes automated tools to manage Claude Desktop MCP server configurations:

### Quick Update
Simply run one of these scripts to automatically configure Claude Desktop:
- **Windows**: `update_claude_config.bat`
- **PowerShell**: `update_claude_config.ps1`

### Manual Configuration Management
Use the Python configuration manager directly:
```bash
# Show current status
python claude_config_manager.py --status

# Update all configurations
python claude_config_manager.py

# Create backup only
python claude_config_manager.py --backup

# Update just standard servers
python claude_config_manager.py --ensure-standard
```

The configuration manager automatically:
- Creates backups before making changes
- Ensures all standard MCP servers are properly configured
- Updates task-orchestrator to use the correct repository path
- Maintains proper API keys and server settings

## Configuration

The task orchestrator server is configured to use this directory as its working directory via the Claude Desktop MCP configuration.

## Backup

This repository serves as a backup and version control system for the task orchestrator database, ensuring no task data is lost.

## Last Updated

Database last active: July 18, 2025
Repository created: July 21, 2025
