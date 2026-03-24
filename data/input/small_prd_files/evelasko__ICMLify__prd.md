---
project: ICMLify
repository: evelasko/ICMLify
license: MIT License
source_file: prd.md
source_url: https://github.com/evelasko/ICMLify/blob/26bb4ed0162a7628ca72008b2a116f44b5c60166/prd.md
downloaded_at: 2025-12-05T10:30:21.852651+00:00
consensus_grade_level: 10.8
headings_per_sentence: 0.09
lists_per_sentence: 0.36
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.13
anaphora_per_sentence: 0.32
sentence_cv: 0.996
cpre_terms_per_sentence: 0.25
---
# ICMLify - Product Requirements Document

---

## Overview

**Product:** ICMLify  
**Problem:** There is no modern, well-documented, or easy-to-use JavaScript/TypeScript library for converting structured content like Markdown into the InDesign Content Markup Language (ICML). Developers wishing to programmatically generate rich-text content for Adobe InDesign workflows are forced to manually construct complex, verbose, and poorly-documented XML, a process which is brittle and highly error-prone. The primary source of truth is reverse-engineering InDesign's own output, which is a significant barrier to entry.  
**Target Audience:** Software developers building integrations with Adobe InDesign. This includes plugin developers (UXP/CEP), web-to-print automation engineers, and anyone building content management systems that need to output professionally formatted documents. The initial consumer will be the "Thesis Bridge" plugin.  
**Value Proposition:** ICMLify is a zero-dependency, open-source TypeScript library that provides a simple, high-level API for converting structured Markdown into valid, clean ICML files. It abstracts away the complexity of the ICML format, allowing developers to generate rich, stylable InDesign stories with just a few lines of code, dramatically accelerating development and improving reliability.

## Core Features

### 1. Markdown-to-ICML Conversion Engine

* **What it does:** Serves as the core function of the library. It accepts a string of Markdown text and a configuration object, and returns a string containing a complete, valid ICML file.
* **Why it's important:** This is the library's entire reason for being. It provides the "magic" that translates simple text into a complex XML structure.
* **How it works at a high level:** It uses `markdown-it` as a base parser to create an Abstract Syntax Tree (AST) from the Markdown input. It then walks this AST, token by token, using a set of "renderer" rules to generate the corresponding ICML tags. Each renderer rule is responsible for a specific Markdown element (e.g., a heading, a list item).

### 2. Style Mapping Configuration

* **What it does:** Allows the developer to provide a simple JavaScript object to map Markdown elements to specific InDesign style names.
* **Why it's important:** This decouples content from presentation and is the key to creating professionally styled documents. Without this, all content would be unformatted.
* **How it works at a high level:** The main conversion function accepts a `styleMap` object. When the renderer encounters a Markdown element, it looks up the corresponding InDesign style name in this map and injects it into the appropriate `AppliedParagraphStyle` or `AppliedCharacterStyle` attribute in the generated ICML.

### 3. Advanced Feature Rendering

* **What it does:** Provides dedicated support for complex InDesign features that have no direct Markdown equivalent. This includes footnotes, tables with table/cell styles, and internal cross-references.
* **Why it's important:** These features are non-negotiable for professional publishing and academic documents. The library must handle them gracefully to be truly useful.
* **How it works at a high level:** It uses custom plugins for `markdown-it` to parse specialized syntax (e.g., footnotes `[^1]`). The renderers for these tokens are highly specialized, generating complex XML structures for tables (`<Table>`, `<Cell>`), footnotes (`<Footnote>`), and hyperlinks/anchors (`<Hyperlink>`, `<HyperlinkTextDestination>`).

### 4. Asset Path and Link Resolution Hooks

* **What it does:** Provides a mechanism for the consuming application to resolve paths for local images and destinations for cross-references.
* **Why it's important:** A library cannot know the file structure of the project it's used in. This feature allows the consuming application (like Thesis Bridge) to inject its project-specific knowledge into the compilation process.
* **How it works at a high level:** The configuration object accepts optional resolver functions, e.g., `resolveImagePath` and `resolveLinkDestination`. When the ICMLify renderer encounters an image or a link, it calls the provided function with the path/link text. The consuming application's function returns the final, absolute path or unique anchor ID, which ICMLify then embeds in the final ICML.

## User Experience

*As a developer library, the "UX" is the "Developer Experience" (DX).*

### User Personas

* **Maria (Plugin Developer):** Maria is building the "Thesis Bridge" plugin. She needs a reliable library to handle the conversion logic so she can focus on the UI and workflow orchestration. She values clear documentation, TypeScript support, and a simple API.
* **David (Backend Engineer):** David is working on a web-to-print service where users design brochures online. He needs to generate InDesign-ready content on a server. He values performance, reliability, and zero dependencies (especially non-JS ones).

### Key User Flows (Developer Journeys)

1. **Basic Conversion:**
    1. Developer installs the library: `npm install iclify`.
    2. Imports the main function: `import { iclify } from 'icmlify';`.
    3. Defines a simple Markdown string and a style map.
    4. Calls the function: `const icmlString = iclify(markdown, { styleMap });`.
    5. Saves the `icmlString` to a file and places it in InDesign, seeing a fully styled story.

2. **Conversion with Image Paths:**
    1. Developer has a Markdown string with `![](./assets/figure1.png)`.
    2. They define a resolver function that knows how to convert the relative path to an absolute `file://` URI based on the source file's location.
    3. They pass this function in the configuration: `iclify(md, { resolveImagePath: myResolver });`.
    4. The resulting ICML contains a valid, absolute link to the image file on disk.

## Technical Architecture

### System Components

* **Core Module (`index.ts`):** Exports the main `iclify` function and its associated types.
* **Parser (`parser.ts`):** Initializes and configures the `markdown-it` instance with all necessary base plugins and custom plugins (for footnotes, etc.).
* **Renderer (`renderer.ts`):** Contains the class or object that defines the rendering rules. This is the heart of the library. It holds the logic for converting each `markdown-it` token into an ICML string (e.g., `renderer.rules.heading_open = () => '<ParagraphStyleRange...>';`).
* **Type Definitions (`types.ts`):** Contains all public-facing TypeScript interfaces for configuration objects (`IclifyConfig`, `StyleMap`, etc.).
* **Utilities (`utils.ts`):** A set of helper functions, most importantly an `escapeXml` function to prevent malformed output.

### Data Models

* **`IclifyConfig` (TypeScript Interface):** The main configuration object passed to the library.

    ```typescript
    interface IclifyConfig {
      styleMap: StyleMap;
      linkResolver?: (link: LinkInfo) => ResolvedLink | null;
      imageResolver?: (imagePath: string) => string | null;
      // ... other options
    }
    ```

* **`StyleMap` (TypeScript Interface):** Defines the mapping from Markdown elements to InDesign styles.

    ```typescript
    interface StyleMap {
      h1?: string;
      h2?: string;
      // ...
      p?: string;
      strong?: string;
      em?: string;
      table?: string;
      tableHeader?: string;
      footnote?: string;
      // ...
    }
    ```

### APIs and Integrations

* **Public API:** The library exposes a single primary function: `iclify(markdown: string, config: IclifyConfig): string`.
* **Dependencies:**
  * `markdown-it`: The core Markdown parser.
  * `@types/markdown-it`: Type definitions for the parser.
  * (Optional but recommended) `markdown-it-footnote`: A standard plugin for footnote syntax.
* **Testing Framework:** Jest or Vitest will be used for unit testing. Each renderer rule will have its own dedicated test to verify its XML output against a known-good snapshot.

## Development Roadmap

*Scope-based phases for building the library.*

### Phase 1: The Core Foundation (MVP)

**Goal:** Create a functional library that can handle the most common text formatting tasks.

* **Scaffolding:** Set up the project with TypeScript, `markdown-it`, and a testing framework.
* **Renderer Implementation:** Implement renderers for the following basic elements:
  * Headings (H1-H6)
  * Paragraphs
  * Bold (`strong`)
  * Italic (`em`)
  * Code Spans (`code_inline`)
  * Hard and soft line breaks
* **Style Mapping:** Implement the basic `styleMap` configuration for the elements listed above.
* **Testing:** Write snapshot tests for the ICML output of each implemented renderer.
* **Outcome:** A working library that can convert a simple Markdown document into a styled ICML file.

### Phase 2: Structural Elements

**Goal:** Add support for more complex, block-level structures essential for long-form documents.

* **Renderer Implementation:**
  * Ordered and Unordered Lists (including proper nesting).
  * Blockquotes.
  * Horizontal Rules.
  * Code Blocks (rendering as a single paragraph with a specific Paragraph Style and a Character Style applied to the content for font/spacing control).
  * Tables (GitHub Flavored Markdown). The renderer must generate the full `<Table>` and `<Cell>` structure and apply `table` and `tableHeader` styles from the `styleMap`.
* **Testing:** Add snapshot tests for all new structural elements.
* **Outcome:** A library capable of handling the vast majority of standard Markdown documents.

### Phase 3: Advanced Publishing Features

**Goal:** Implement the complex features required by the "Thesis Bridge" plugin and other professional workflows.

* **Footnotes:** Integrate `markdown-it-footnote` and write a custom renderer to generate the native InDesign `<Footnote>` tags and references.
* **Image and Link Resolvers:** Implement the hook-based system (`imageResolver`, `linkResolver`). The default behavior if no resolver is provided should be to pass paths through as-is.
* **Cross-Reference Primitives:** The `linkResolver` implementation will require the renderers to be able to generate two distinct structures:
  * `<HyperlinkTextDestination Name="unique-anchor-id">` for anchors.
  * `<Hyperlink Source="..." Destination="HyperlinkDestinations/unique-anchor-id">` for the links themselves.
* **Testing:** Write unit tests for the resolver hooks and integration tests for the cross-reference generation.
* **Outcome:** A feature-complete library ready for use in the Thesis Bridge plugin.

## Logical Dependency Chain

1. **Project Setup:** The initial scaffolding with TypeScript, `markdown-it`, and a test runner is the absolute first step.
2. **Core Renderer Logic:** The renderer for a simple `<ParagraphStyleRange>` with plain text is the "hello world" of the library. All other renderers are variations on this theme.
3. **Basic Inline Styles:** Bold and Italic are the next logical step, as they introduce the concept of nested `<CharacterStyleRange>` tags.
4. **Block-Level Elements:** Lists and Blockquotes can be built next, as they build upon the paragraph and inline styling logic.
5. **Complex Blocks (Tables):** Table rendering is a self-contained, complex feature that depends on the basic styling infrastructure being in place.
6. **Extending with Plugins (Footnotes):** Once the core renderer is stable, it can be extended by adding `markdown-it` plugins and writing custom renderers for the new tokens they produce.
7. **Resolver Hooks:** The resolver hook system is an architectural layer that sits on top of the image and link renderers. The renderers must be functional before the hooks can be integrated.

## Risks and Mitigations

| Risk                                  | Description                                                  | Mitigation Strategy                                          |
| :------------------------------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **Technical: ICML Verbosity**         | The ICML format is extremely verbose. A small Markdown feature can result in dozens of lines of XML boilerplate. | **Mitigation:** Adhere strictly to the **Reverse-Engineering Methodology**. Create minimal "one thing" sample files. Use snapshot testing to prevent regressions and ensure the generated XML is both correct and as lean as possible. |
| **Scope: Supporting All of Markdown** | The Markdown spec has many ambiguities and edge cases. Trying to support every possible permutation is a trap. | **Mitigation:** Clearly define the supported feature set based on the **PRD Roadmap**. Target CommonMark + GFM Tables + Footnotes as the official spec. Document unsupported features explicitly. |
| **Maintenance: XML Escaping**         | A single unescaped character (`<`, `&`, `>`) in user content will invalidate the entire XML file. | **Mitigation:** Create a robust `escapeXml` utility function. Write extensive unit tests for this function with all known edge cases. Apply this function religiously to *all* user-provided content before inserting it into an ICML tag. |

## Appendix

### Exhaustive List of Required InDesign Samples

This is the "test plan" for the reverse-engineering effort. For each item, an `.indd` file must be created and exported to ICML to serve as the ground truth.

**A. Basic Inline Formatting:**

1. `plain-paragraph.indd`: A single paragraph of lorem ipsum.
2. `bold.indd`: A word with a "Bold" Character Style applied.
3. `italic.indd`: A word with an "Italic" Character Style applied.
4. `bold-italic.indd`: A word with both styles applied.
5. `inline-code.indd`: A word with a "Code" Character Style applied.

**B. Basic Block Formatting:**
6.  `headings.indd`: One of each heading (H1-H6), each with a corresponding Paragraph Style (e.g., "Heading 1").
7.  `blockquote.indd`: A paragraph with a "Blockquote" Paragraph Style.
8.  `horizontal-rule.indd`: A document containing only a horizontal rule (`<Rectangle>`).

**C. Lists:**
9.  `unordered-list.indd`: A simple 3-item bulleted list.
10. `ordered-list.indd`: A simple 3-item numbered list.
11. `nested-list.indd`: A mixed list with at least two levels of nesting.

**D. Code Blocks:**
12. `code-block.indd`: A multi-line block of code, formatted with a specific "Code Block" Paragraph Style (which should use a monospaced font and disable hyphenation).

**E. Tables:**
13. `table-simple.indd`: A 2x2 table with no styling.
14. `table-styled.indd`: A 3x3 table with a "Basic Table" Table Style and "TableHeader" / "TableCell" Cell Styles applied.

**F. Links and Images:**
15. `hyperlink-url.indd`: A hyperlink to an external URL (e.g., `https://adobe.com`).
16. `image.indd`: An image placed as an inline/anchored object.

**G. Advanced Publishing Features:**
17. `footnote.indd`: A paragraph containing a single footnote reference, with the footnote text at the bottom of the page.
18. `cross-reference-setup.indd`: A document with two paragraphs. The second paragraph has a **Hyperlink Text Destination** (an anchor) applied.
19. `cross-reference-link.indd`: A document containing a **Hyperlink** that points to the anchor created in sample #18. (This requires two files to test inter-document linking, simulating the final use case).
