---
project: qraft
repository: dasheck0/qraft
license: MIT License
source_file: tasks/prd-copy-no-sync-flag.md
source_url: https://github.com/dasheck0/qraft/blob/0bf1d57e3e3ad0736b5ffd0fcd85c47c9cb33c65/tasks/prd-copy-no-sync-flag.md
downloaded_at: 2025-12-05T10:42:25.626499+00:00
consensus_grade_level: 12.3
headings_per_sentence: 0.3
lists_per_sentence: 0.63
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.03
anaphora_per_sentence: 0.08
sentence_cv: 1.125
cpre_terms_per_sentence: 0.42
---
# PRD: Add --no-sync Flag to Copy Command

## Introduction/Overview

Add a new `--no-sync` flag to the `qraft copy` command that prevents the creation of the `.qraft` directory and associated manifest files. This enables users to pull single files or templates without integrating them into the qraft sync cycle.

Currently, when using `qraft copy`, the CLI always creates a `.qraft` directory containing manifest and metadata files to enable synchronization and update tracking. However, there are use cases where users want to pull content for one-time use without the overhead of sync tracking.

## Goals

1. **Enable one-time file copying**: Allow users to copy template content without creating sync metadata
2. **Reduce directory clutter**: Prevent unnecessary `.qraft` directories when sync tracking isn't needed
3. **Maintain backward compatibility**: Preserve existing behavior as the default
4. **Improve user control**: Give users explicit choice over sync tracking behavior

## User Stories

1. **As a developer**, I want to copy a single configuration file from a template box without creating a `.qraft` directory, so that I can use the file without committing to the sync workflow.

2. **As a project maintainer**, I want to extract specific files from template boxes for reference purposes without cluttering my directory with metadata, so that I can keep my workspace clean.

3. **As a CI/CD pipeline**, I want to copy template files without sync tracking so that automated processes don't create unnecessary metadata directories.

## Functional Requirements

1. The copy command must accept a new `--no-sync` flag (with `-n` alias)
2. When `--no-sync` is specified, the system must skip creating the `.qraft` directory
3. When `--no-sync` is specified, the system must skip storing manifest and metadata files
4. File copying functionality must work identically regardless of sync flag setting
5. Default behavior (without `--no-sync`) must remain unchanged
6. Interactive mode must prompt users about sync preference when no explicit flag is provided
7. Success messages must clearly indicate whether sync tracking is enabled or disabled
8. The flag must be documented in help text and command descriptions

## Non-Goals (Out of Scope)

1. Modifying other commands (create, update, list) - only copy command is affected
2. Global configuration for default sync behavior
3. Retroactively removing `.qraft` directories from existing copies
4. Advanced sync management features

## Design Considerations

### CLI Interface
```bash
# Current behavior (unchanged)
qraft copy my-template

# New no-sync behavior
qraft copy my-template --no-sync
qraft copy my-template -n

# Interactive mode will prompt for sync preference
qraft copy my-template --interactive
```

### Output Messages
**With sync tracking (current):**
```
✅ Successfully copied 5 files
📁 Files copied to: /target/directory
📦 Box tracking enabled in .qraft/ directory
```

**Without sync tracking (new):**
```
✅ Successfully copied 5 files
📁 Files copied to: /target/directory
ℹ️  No sync tracking (use without --no-sync to enable updates)
```

## Technical Considerations

### Implementation Areas
1. **CLI Definition**: Add flag to commander.js options in `src/cli.ts`
2. **Interface Updates**: Extend `CopyOptions` and `BoxOperationConfig` interfaces
3. **Core Logic**: Modify `BoxManager.copyBox()` to conditionally skip manifest storage
4. **Interactive Mode**: Update prompts to include sync preference question

### Backward Compatibility
- Default behavior remains identical to current implementation
- Existing scripts and automation continue to work without changes
- No breaking changes to public APIs

### Error Handling
- In sync mode: If manifest storage fails, show warning but continue operation
- In no-sync mode: Skip manifest storage entirely (eliminates potential failure point)

## Success Metrics

1. **Functional Success**: `--no-sync` flag prevents `.qraft` directory creation in 100% of test cases
2. **Compatibility Success**: All existing copy operations continue to work without modification
3. **User Adoption**: Clear documentation and help text enable users to discover and use the feature
4. **Test Coverage**: 100% test coverage for new functionality including edge cases

## Open Questions

1. Should the flag name be `--no-sync`, `--no-track`, or `--standalone`?
2. Should interactive mode default to sync enabled or prompt every time?
3. Should we add a warning when using `--no-sync` to inform users about lost update capabilities?
4. Should the short alias be `-n` or something else to avoid conflicts?

---

## Implementation Notes

### Files to Modify
- `src/cli.ts` - Add command line option
- `src/commands/copy.ts` - Update CopyOptions interface and pass flag
- `src/types.ts` - Update BoxOperationConfig interface  
- `src/core/boxManager.ts` - Add conditional logic in copyBox method
- `src/interactive/interactiveMode.ts` - Add sync preference prompt

### Testing Requirements
- Unit tests for flag parsing and option handling
- Integration tests for both sync and no-sync file copying
- Interactive mode tests with sync preference scenarios
- Backward compatibility tests to ensure default behavior unchanged
