# Notes on the retrieval step of the RAG pipeline

## Query translation

**Problem statement**: User queries may be ambigous or poorly written. Because we embed the query and search for similar documents, the retrieved information may be irrelevant.

By translating the query in some way, we increase the chance of receiving relevant documents.
