# Claude Desktop Configuration Manager - PowerShell Version
# Automatically updates Claude Desktop MCP server configurations

Write-Host "🔧 Updating Claude Desktop Configuration..." -ForegroundColor Cyan
Write-Host ""

# Change to the task-orchestrator directory
Set-Location "C:\GitHub_Development\task-orchestrator"

# Run the configuration manager
python claude_config_manager.py

Write-Host ""
Write-Host "✅ Configuration update complete!" -ForegroundColor Green
Write-Host ""
Write-Host "To run this again in the future, just execute:" -ForegroundColor Yellow
Write-Host "    C:\GitHub_Development\task-orchestrator\update_claude_config.ps1" -ForegroundColor White
Write-Host ""

# Optional: Pause to see results
Read-Host "Press Enter to continue"
