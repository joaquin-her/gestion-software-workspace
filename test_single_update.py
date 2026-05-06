#!/usr/bin/env python3
"""
Test script to update a single Jira story with proper story point estimation
"""

import json

def main():
    """Test updating one Jira story"""
    # Read test data
    with open('/home/joaquin-her/repos/gestion/test_update.json', 'r', encoding='utf-8') as f:
        update_data = json.load(f)
    
    print("=== JIRA Story Update Test ===")
    print(f"Updating: {update_data['jira_key']}")
    print(f"Summary: {update_data['jira_summary']}")
    print(f"Backlog Match: {update_data['backlog_title']}")
    print(f"Estimation: {update_data['estimation']}")
    print()
    
    # Create description with proper story point estimation
    description = f"""h2. Descripción

{update_data['backlog_title']}

h2. Criterios de Aceptación

{update_data['backlog_criteria']}

h2. Estimación

{update_data['estimation']} story points"""
    
    print("=== Description Generated ===")
    print(description)
    print()
    
    # For now, just show what would be updated
    print("=== MCP Call That Would Be Made ===")
    print(f"Tool: mcp0_editJiraIssue")
    print(f"Parameters:")
    print(f"  cloudId: https://grupo15gestion.atlassian.net")
    print(f"  issueIdOrKey: {update_data['jira_key']}")
    print(f"  fields:")
    print(f"    description: {description[:100]}...")
    print()
    
    # Save the prepared update for manual execution
    prepared_update = {
        "cloudId": "https://grupo15gestion.atlassian.net",
        "issueIdOrKey": update_data['jira_key'],
        "fields": {
            "description": description
        }
    }
    
    with open('/home/joaquin-her/repos/gestion/prepared_update.json', 'w', encoding='utf-8') as f:
        json.dump(prepared_update, f, ensure_ascii=False, indent=2)
    
    print("✓ Test update data prepared and saved to prepared_update.json")
    print("✓ Ready for manual MCP execution")
    
    return True

if __name__ == "__main__":
    main()
