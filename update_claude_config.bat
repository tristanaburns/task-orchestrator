@echo off
REM Claude Desktop Configuration Manager
REM Automatically updates Claude Desktop MCP server configurations

echo 🔧 Updating Claude Desktop Configuration...
echo.

cd /d "C:\GitHub_Development\task-orchestrator"
python claude_config_manager.py

echo.
echo ✅ Configuration update complete!
echo.
echo To run this again in the future, just execute:
echo     C:\GitHub_Development\task-orchestrator\update_claude_config.bat
echo.
pause
