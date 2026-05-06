#!/usr/bin/env python3
"""
Script to update Jira stories with descriptions and estimations from Backlog.xlsx
"""

import json
import sys
import os

# Add the current directory to Python path to import MCP modules
sys.path.append('/home/joaquin-her/repos/gestion')

def update_jira_story(jira_key, description, estimation):
    """Update a single Jira story with description and estimation"""
    try:
        # Import MCP functions using subprocess to call the MCP tool
        import subprocess
        import json
        
        # Prepare the MCP call
        mcp_call = {
            "tool": "mcp0_editJiraIssue",
            "parameters": {
                "cloudId": "https://grupo15gestion.atlassian.net",
                "issueIdOrKey": jira_key,
                "fields": {
                    "description": description
                }
            }
        }
        
        # Use subprocess to call MCP tool
        result = subprocess.run([
            "python3", "-c", f"""
import json
import sys
sys.path.append('/home/joaquin-her/repos/gestion')

# Simulate MCP call
from mcp0_editJiraIssue import mcp0_editJiraIssue

result = mcp0_editJiraIssue(
    cloudId="{mcp_call['parameters']['cloudId']}",
    issueIdOrKey="{mcp_call['parameters']['issueIdOrKey']}",
    fields={mcp_call['parameters']['fields']}
)

print(json.dumps(result))
"""
        ], capture_output=True, text=True, cwd="/home/joaquin-her/repos/gestion")
        
        if result.returncode == 0:
            print(f"✓ Updated {jira_key}")
            return True
        else:
            print(f"✗ Failed to update {jira_key}: {result.stderr}")
            return False
        
    except Exception as e:
        print(f"✗ Failed to update {jira_key}: {str(e)}")
        return False

def main():
    """Main function to update Jira stories"""
    # Read the test update data
    with open('/home/joaquin-her/repos/gestion/test_update.json', 'r', encoding='utf-8') as f:
        update_data = json.load(f)
    
    print("=== JIRA Story Update Test ===")
    print(f"Updating: {update_data['jira_key']}")
    print(f"Summary: {update_data['jira_summary']}")
    print(f"Backlog Match: {update_data['backlog_title']}")
    print(f"Estimation: {update_data['estimation']}")
    print()
    
    # Create description
    description = f"""h2. Descripción

{update_data['backlog_title']}

h2. Criterios de Aceptación

{update_data['backlog_criteria']}

h2. Estimación

{update_data['estimation']} story points"""
    
    # Update the story
    success = update_jira_story(update_data['jira_key'], description, update_data['estimation'])
    
    if success:
        print("✓ Test update completed successfully!")
    else:
        print("✗ Test update failed!")
    
    return success

if __name__ == "__main__":
    main()
