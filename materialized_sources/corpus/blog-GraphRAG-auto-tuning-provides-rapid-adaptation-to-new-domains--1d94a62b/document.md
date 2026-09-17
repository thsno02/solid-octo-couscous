# GraphRAG auto-tuning provides rapid adaptation to new domains

Published September 9, 2024

By Alonso Guevara Fernández , Senior Software Engineer Katy Smith , Data Scientist II Joshua Bradley , Senior Data Scientist Darren Edge , Senior Director Ha Trinh , Senior Data Scientist Sarah Smith , Principal Program Manager Ben Cutler , Senior Director Steven Truitt , Principal Program Manager Jonathan Larson , Partner Data Architect

Share this page

Share on Facebook

Share on X

Share on LinkedIn

Share on Reddit

Subscribe to our RSS feed

GraphRAG uses large language models (LLMs) to create a comprehensive knowledge graph that details entities and their relationships from any collection of text documents. This graph enables GraphRAG to leverage the semantic structure of the data and generate responses to complex queries that require a broad understanding of the entire text. In previous blog posts, we introduced GraphRAG and demonstrated how it could be applied to news articles . In this blog post, we show that it can also be tuned to any domain to enhance the quality of the results.

The knowledge graph creation process is called indexing . An LLM, guided by a set of domain-specific prompts, reads all the source content and extracts the relevant information, including entities and relationships, which are then used to construct the graph. For example, when analyzing news articles, entities like people, places, and organizations are important. Here, relationship types might i
