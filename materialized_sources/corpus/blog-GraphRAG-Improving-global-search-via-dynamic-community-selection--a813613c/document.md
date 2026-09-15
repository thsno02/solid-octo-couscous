# GraphRAG: Improving global search via dynamic community selection

Published November 15, 2024

By Bryan Li , Research Intern Ha Trinh , Senior Data Scientist Darren Edge , Senior Director Jonathan Larson , Partner Data Architect

Share this page

Share on Facebook

Share on X

Share on LinkedIn

Share on Reddit

Subscribe to our RSS feed

Retrieval-augmented generation (RAG) allows AI systems to provide additional information and context to a large language model (LLM) when generating a response to a user query. However, traditional RAG-based methods can struggle to retrieve information that requires high-level knowledge of the entire dataset, especially with abstract and global questions such as the keywordless query: “Catch me up on the last two weeks of updates.” These types of queries are known as “global” queries, as they require holistic understanding of the dataset to answer the question. GraphRAG aims to tackle these questions in two main steps: indexing and query. The indexing engine first breaks down a collection of text documents into segments which are then clustered into hierarchical communities with entities and relationships connecting each segment up through higher levels of abstraction. We then use an LLM to generate a summary of each community, known as a community report. The indexing engine thus creates a hierarchical knowledge graph of the dataset, with each level in the hierarchy representing a different level of abstraction and summarization of the o
