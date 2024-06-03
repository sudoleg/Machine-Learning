# Indexing techniques

## multi-representation indexing

Multi-representation indexing is a technique where a document is split and a summary or proposition is created using a language model (LLM) to optimize retrieval. The summary is then embedded in a vector store for efficient search and retrieval, while the raw document is stored separately. When a query is made, the summary is used to retrieve the full document for further processing, such as with long-context language models.

### Step-by-Step Guide for Implementing Multi-Representation Indexing

1. **Load and Preprocess Documents:**
   - Load the raw documents, such as blog posts, that you want to index.
   - Use a language model to create summaries or propositions for each document.

2. **Define Vector Store and Document Store:**
   - Define a vector store to index the summaries or propositions.
   - Define a document store to store the full raw documents.

3. **Combine Vector and Document Stores:**
   - Create a multi Vector retriever that combines the vector store and document store.
   - Assign unique document IDs to each document for reference.

4. **Index Summaries and Full Documents:**
   - Add the summary documents to the vector store.
   - Add the full raw documents to the document store with corresponding document IDs.

5. **Perform Query and Retrieval:**
   - Run queries on the vector store using the summaries for efficient retrieval.
   - Retrieve the full document using the document IDs from the vector store.

6. **Retrieve Full Documents for Processing:**
   - Use the retrieved full documents for further processing, such as with long-context language models for generating responses or answers.

7. **Example Implementation:**
   - Load two blog posts, create summaries for each.
   - Index the summaries in the vector store and full documents in the document store.
   - Query the vector store for relevant documents based on the summaries.
   - Retrieve the full documents for processing based on the query results.

This technique allows for efficient indexing and retrieval of documents by using optimized summaries while still having access to the full content when needed for processing or analysis.