# Text splitting for retrieval

The goals of text splitting are:

- to reduce the number of input tokens to fit into the models context window
- to divide the text into meaningful parts, which can be retrieved for value later

## Character split

- most simple and fast method
- splits by number of characters

## Recursive character split

- a bit smarter than the previous method, as it takes the structure of the document (e.g. paragraphs) into account
- maximum amount of tokens per chunk is defined, but the length of it isn't fixed
- the idea is that paragraphs contain standalone pieces of information that differ from other paragraphs at least a little bit
- good place to start, because of the high ROI

## Document specific split

- takes the syntax of the document into account
- e.g. HTML, Markdown, code etc.
- for example, we could split by classes and functions in code, because they can be identified by keywords such as `class` or `def` (in python)
- another example: in HTML or .md docs, we can extract images and tables

## Semantic split

## Agentic splitting

## Resources

- 1hr YT video - [The 5 Levels Of Text Splitting For Retrieval](https://youtu.be/8OJC21T2SL4?si=oy8iXMm-H44BjSPo) - by Greg Kamradt
- [ChunkViz](https://chunkviz.up.railway.app/) app for splitting visuialization
- [unstructured](https://github.com/Unstructured-IO/unstructured) - libraries and APIs for ingesting and pre-processing images and text documents (such as PDFs, HTML, Word docs) to optimize the data processing workflow for LLMs
