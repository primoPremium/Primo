# Obsidian Memory Migration Guide

This guide walks through the process of migrating existing memories to the Obsidian + openclaw-mem system.

## 1. Pre-migration Preparation Steps

### 1.1 Environment Setup
- Install Obsidian if not already installed
- Ensure openclaw-mem plugin is properly configured
- Create a backup of your existing memory files
- Set up your Obsidian vault directory

### 1.2 Memory Inventory
- List all existing memory source files
- Document current memory structure and formats
- Identify any special formatting or metadata requirements
- Note any external dependencies or linked content

## 2. Data Format Requirements

### 2.1 File Format
- Files must be in Markdown (.md) format
- UTF-8 encoding required
- Line endings: LF (Unix-style) preferred

### 2.2 Required Metadata
```yaml
---
date: YYYY-MM-DD
type: memory
tags: [tag1, tag2]
---
```

### 2.3 Content Structure
- Use level 2 headers (##) for main sections
- Include timestamps in ISO format where applicable
- Maintain consistent indentation (preferably 2 or 4 spaces)
- Links should use Obsidian format: [[page-name]]

## 3. Migration Process

### 3.1 Daily Memory Files
1. Create the target directory structure:
   ```
   vault/
   ├── daily/
   ├── long-term/
   └── index.md
   ```

2. Convert existing daily logs:
   ```markdown
   # Example conversion
   
   Old format:
   2024-01-01.md: "User requested weather info..."
   
   New format:
   daily/2024-01-01.md:
   ---
   date: 2024-01-01
   type: daily
   tags: [daily-log]
   ---
   ## Interactions
   - User requested weather info...
   ```

### 3.2 Long-term Memories
1. Split MEMORY.md into topic-based files
2. Add required metadata headers
3. Create backlinks between related content

## 4. Post-migration Verification

### 4.1 Content Verification
- Check all files have correct metadata
- Verify timestamps are in ISO format
- Ensure all links are functional
- Validate UTF-8 encoding

### 4.2 System Tests
- Test openclaw-mem search functionality
- Verify daily log access
- Check long-term memory retrieval
- Test backlink functionality

### 4.3 Checklist
- [ ] All files converted to proper format
- [ ] Metadata headers present and valid
- [ ] Directory structure matches specification
- [ ] No broken links or references
- [ ] Search functionality working
- [ ] Backup copy preserved

## 5. Troubleshooting Common Issues

### 5.1 Metadata Issues
- **Problem**: Missing YAML front matter
  - **Solution**: Use script to add template metadata header
  - **Example**:
    ```yaml
    ---
    date: {{date}}
    type: memory
    tags: []
    ---
    ```

### 5.2 Encoding Problems
- **Problem**: Invalid character encoding
  - **Solution**: Use `iconv` to convert to UTF-8
  - **Command**: `iconv -f ISO-8859-1 -t UTF-8 input.md > output.md`

### 5.3 Link Conversion
- **Problem**: Incompatible link formats
  - **Solution**: Convert to Obsidian-style wiki links
  - Old: `[link](target)`
  - New: `[[target|link]]`

### 5.4 Date Format Issues
- **Problem**: Inconsistent date formats
  - **Solution**: Standardize to YYYY-MM-DD
  - Use date parsing script for bulk conversion

## Additional Resources

### Useful Commands
```bash
# Check file encoding
file -i filename.md

# Fix line endings
dos2unix filename.md

# Bulk convert files
find . -name "*.md" -exec dos2unix {} \;
```

### Migration Scripts
Create helper scripts in the tools directory for:
- Metadata addition
- Date standardization
- Link conversion
- Encoding verification

## Support
For additional help:
- Check openclaw-mem documentation
- Review Obsidian community forums
- Submit issues to the openclaw-mem repository