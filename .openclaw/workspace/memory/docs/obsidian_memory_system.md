# OpenClaw Memory System and Obsidian Integration Guide

This technical guide explains the architecture and functionality of OpenClaw's memory storage and recall system, with a focus on its integration with Obsidian for knowledge management.

## 1. Memory File Structure and Organization

### Core Memory Files
```
~/.openclaw/workspace/
├── MEMORY.md           # Long-term, persistent memory (main session only)
├── memory/
│   ├── YYYY-MM-DD.md  # Daily memory logs
│   ├── docs/          # Technical documentation
│   └── topics/        # Topic-specific memory files
└── USER.md            # User preferences and context
```

### Daily Logs
Daily memory files (`YYYY-MM-DD.md`) serve as temporal indexes for conversations and actions. Each entry follows this format:

```markdown
## [HH:MM UTC] Context/Topic
- Action or conversation content
- Related decisions or outcomes
```

### Topic-Based Organization
Topic-specific memories are organized in the `memory/topics/` directory using semantic filenames:
- `projects/`: Project-specific memory files
- `preferences/`: User preferences and settings
- `skills/`: Learned capabilities and procedures

## 2. Memory Recall with Markdown Files

### File-Based Memory Model
OpenClaw uses a markdown-based memory system that leverages file structure and content for recall:

1. **Temporal Access**: Recent memories from daily logs
2. **Semantic Access**: Topic-based recall from organized directories
3. **Cross-Reference Links**: Obsidian-compatible wiki links between related content

### Memory Loading Process
1. On session start:
   - Load current day's log
   - Load previous day's context
   - Main session loads MEMORY.md
   - Process USER.md for preferences

2. During operation:
   - Write new memories immediately
   - Update cross-references
   - Maintain temporal and semantic indexes

## 3. Search and Retrieval Mechanisms

### Search Methods
1. **Direct File Access**
   - Temporal: Access daily logs
   - Semantic: Navigate topic structure
   - Reference: Follow wiki links

2. **Content Search**
   ```bash
   # Full text search example
   rg "search term" ~/.openclaw/workspace/memory/
   ```

3. **Metadata Query**
   - Use frontmatter for structured data
   - Query by tags, dates, or categories

### Retrieval Optimization
- Index frequently accessed content
- Maintain topic hierarchies
- Use consistent tagging
- Create summary files for large topics

## 4. OpenClaw-Obsidian Integration

### Connection Points
1. **File Format Compatibility**
   - Standard markdown syntax
   - YAML frontmatter support
   - Wiki-style internal links

2. **Directory Structure**
   ```
   .obsidian/
   ├── config/
   ├── plugins/
   └── workspace
   ```

3. **Link Formats**
   ```markdown
   [[direct-link]]
   [[link|alias]]
   [[folder/note#heading]]
   ```

### Synchronization
- Files readable by both systems
- Maintains link integrity
- Preserves metadata
- Supports attachments

## 5. Memory Management Best Practices

### Organization Guidelines
1. **Consistent Structure**
   - Use clear file naming conventions
   - Maintain organized directories
   - Follow markdown formatting standards

2. **Effective Tagging**
   ```markdown
   ---
   tags: [project, technical, active]
   date: 2026-03-01
   status: active
   ---
   ```

3. **Link Management**
   - Create meaningful connections
   - Maintain bidirectional links
   - Update broken references

### Maintenance Procedures
1. **Regular Cleanup**
   - Archive old daily logs
   - Update index files
   - Verify link integrity

2. **Content Organization**
   - Consolidate related information
   - Split large files
   - Update cross-references

3. **Performance Optimization**
   - Remove duplicate content
   - Maintain efficient file structure
   - Optimize search indexes

## Usage Examples

### Creating a New Memory Entry
```markdown
## [16:45 UTC] Project: Memory System
- Implemented new indexing structure
- Updated search mechanisms
- [[projects/memory-system]] updated with changes
```

### Topic Cross-Reference
```markdown
## Memory System Components
- Daily Logs: [[system/daily-logs]]
- Search Engine: [[system/search]]
- Integration: [[obsidian/integration]]
```

### Search and Retrieval
```bash
# Find recent project updates
rg "Project: Memory System" memory/2026-03-*.md

# Search across all topic files
rg "search pattern" memory/topics/
```

## Conclusion

OpenClaw's memory system combines robust file organization with Obsidian's powerful knowledge management capabilities. By following these guidelines and best practices, you can maintain an efficient and effective memory system that scales with your needs.

Remember to:
- Write memories immediately
- Maintain clear structure
- Use consistent formatting
- Keep cross-references updated
- Regular maintenance and optimization