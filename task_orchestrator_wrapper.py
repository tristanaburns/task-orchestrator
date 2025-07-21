#!/usr/bin/env python3
"""
Wrapper script for MCP Task Orchestrator Server that suppresses logging output
to prevent JSON-RPC protocol interference.
"""

import sys
import logging
import asyncio
import os

# Set environment variable to control logging level
os.environ["MCP_TASK_ORCHESTRATOR_LOG_LEVEL"] = "ERROR"

# Completely suppress all logging by creating a null handler
class NullHandler(logging.Handler):
    def emit(self, record):
        pass

# Set up null logging before importing the server
root_logger = logging.getLogger()
root_logger.handlers.clear()
root_logger.addHandler(NullHandler())
root_logger.setLevel(logging.CRITICAL)

# Also suppress specific loggers that might be created
logging.getLogger('mcp_task_orchestrator').setLevel(logging.CRITICAL)
logging.getLogger('mcp_task_orchestrator').handlers.clear()
logging.getLogger('mcp_task_orchestrator').addHandler(NullHandler())

# Now import the server module
from mcp_task_orchestrator.server import main

# Override any logging configuration that might have been set during import
def configure_silent_logging():
    """Ensure all logging is completely suppressed."""
    # Get all existing loggers
    for logger_name in logging.Logger.manager.loggerDict:
        logger = logging.getLogger(logger_name)
        logger.handlers.clear()
        logger.addHandler(NullHandler())
        logger.setLevel(logging.CRITICAL)
        logger.propagate = False

if __name__ == "__main__":
    # Configure silent logging after import
    configure_silent_logging()
    
    # Run the main function
    asyncio.run(main())
