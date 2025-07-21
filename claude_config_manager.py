#!/usr/bin/env python3
"""
Claude Desktop Configuration Manager
Automatically manages and updates Claude Desktop MCP server configurations.
"""

import json
import os
import shutil
import sys
from pathlib import Path

class ClaudeDesktopConfigManager:
    def __init__(self):
        self.config_path = Path.home() / "AppData" / "Roaming" / "Claude" / "claude_desktop_config.json"
        self.backup_path = Path.home() / "AppData" / "Roaming" / "Claude" / "claude_desktop_config.backup.json"
        
    def load_config(self):
        """Load existing Claude Desktop configuration"""
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"mcpServers": {}}
    
    def backup_config(self):
        """Create backup of current configuration"""
        if self.config_path.exists():
            shutil.copy2(self.config_path, self.backup_path)
            print(f"✅ Backup created: {self.backup_path}")
    
    def save_config(self, config):
        """Save configuration to Claude Desktop"""
        # Ensure directory exists
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        print(f"✅ Configuration saved: {self.config_path}")
    
    def update_task_orchestrator_config(self, repo_path=None):
        """Update task-orchestrator configuration to use repository location"""
        if repo_path is None:
            repo_path = Path("C:/GitHub_Development/task-orchestrator")
        else:
            repo_path = Path(repo_path)
        
        # Verify repository exists
        if not repo_path.exists():
            print(f"❌ Repository path does not exist: {repo_path}")
            return False
        
        # Verify wrapper exists
        wrapper_path = repo_path / "task_orchestrator_wrapper.py"
        if not wrapper_path.exists():
            print(f"❌ Wrapper script not found: {wrapper_path}")
            return False
        
        # Load current config
        config = self.load_config()
        
        # Update task-orchestrator configuration
        config["mcpServers"]["task-orchestrator"] = {
            "type": "stdio",
            "command": "python",
            "args": ["task_orchestrator_wrapper.py"],
            "cwd": str(repo_path).replace("/", "\\")
        }
        
        # Create backup and save
        self.backup_config()
        self.save_config(config)
        
        print(f"✅ Task-orchestrator configured to use: {repo_path}")
        return True
    
    def ensure_standard_servers(self):
        """Ensure all standard MCP servers are configured with correct settings"""
        config = self.load_config()
        
        # Standard server configurations
        standard_servers = {
            "brave-search": {
                "runtime": "node",
                "env": {
                    "BRAVE_API_KEY": "BSAtUDwjm_Ossvatwzk57N0DzJR5WrH"
                },
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-brave-search"]
            },
            "context7": {
                "type": "stdio",
                "command": "npx",
                "args": ["-y", "@upstash/context7-mcp@latest"]
            },
            "desktop-commander": {
                "type": "stdio",
                "command": "npx",
                "args": ["-y", "desktop-commander"]
            },
            "firecrawl": {
                "type": "stdio",
                "command": "npx",
                "args": ["-y", "firecrawl-mcp@latest"],
                "env": {
                    "FIRECRAWL_API_KEY": "fc-b6e9a7f2e9e845d4a6f7e9f0a8b1c2d3"
                }
            },
            "filesystem": {
                "type": "stdio",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}"]
            },
            "fetch": {
                "type": "stdio",
                "command": "python",
                "args": ["-m", "mcp_server_fetch"]
            },
            "json-processor": {
                "type": "stdio",
                "command": "npx",
                "args": ["-y", "@gongrzhe/server-json-mcp@1.0.3"]
            },
            "markitdown": {
                "type": "stdio",
                "command": "uvx",
                "args": ["markitdown-mcp"]
            },
            "memory": {
                "type": "stdio",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-memory@latest"],
                "env": {
                    "MEMORY_FILE_PATH": "memory.json"
                }
            },
            "sequentialthinking": {
                "type": "stdio",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-sequential-thinking@latest"]
            }
        }
        
        # Update each server configuration
        updated = False
        for server_name, server_config in standard_servers.items():
            if server_name not in config["mcpServers"] or config["mcpServers"][server_name] != server_config:
                config["mcpServers"][server_name] = server_config
                updated = True
                print(f"✅ Updated {server_name} configuration")
        
        if updated:
            self.backup_config()
            self.save_config(config)
        else:
            print("✅ All standard servers already correctly configured")
        
        return updated
    
    def status(self):
        """Show current configuration status"""
        config = self.load_config()
        print(f"\n📋 Claude Desktop Configuration Status")
        print(f"Config file: {self.config_path}")
        print(f"Backup file: {self.backup_path}")
        print(f"Configured servers: {len(config.get('mcpServers', {}))}")
        
        for server_name in sorted(config.get('mcpServers', {}).keys()):
            server_config = config['mcpServers'][server_name]
            command = server_config.get('command', 'Unknown')
            print(f"  • {server_name}: {command}")
        
        # Check task-orchestrator specifically
        if 'task-orchestrator' in config.get('mcpServers', {}):
            task_config = config['mcpServers']['task-orchestrator']
            cwd = task_config.get('cwd', 'Not set')
            print(f"\n🎯 Task-orchestrator working directory: {cwd}")

def main():
    """Main function to handle command line arguments"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Manage Claude Desktop MCP Configuration')
    parser.add_argument('--update-task-orchestrator', metavar='PATH', 
                       help='Update task-orchestrator to use specified repository path')
    parser.add_argument('--ensure-standard', action='store_true',
                       help='Ensure all standard MCP servers are configured')
    parser.add_argument('--status', action='store_true',
                       help='Show current configuration status')
    parser.add_argument('--backup', action='store_true',
                       help='Create backup of current configuration')
    
    args = parser.parse_args()
    
    manager = ClaudeDesktopConfigManager()
    
    if args.status:
        manager.status()
    elif args.backup:
        manager.backup_config()
    elif args.ensure_standard:
        manager.ensure_standard_servers()
    elif args.update_task_orchestrator:
        manager.update_task_orchestrator_config(args.update_task_orchestrator)
    else:
        # Default: Update task-orchestrator and ensure standard servers
        print("🔧 Updating Claude Desktop configuration...")
        manager.ensure_standard_servers()
        manager.update_task_orchestrator_config()
        manager.status()

if __name__ == "__main__":
    main()
