Here is a single-line explanation for each function in the script, in order of appearance:

1. get_embedding: Sends a text string to Ollama's embedding API and returns its numerical vector representation.
2. generate_answer: Prompts the Ollama chat model with a strict system guardrail and retrieved context to generate a grounded answer.
3. load_documents: Reads all .txt files from the target directory and returns their filenames and contents as a list of dictionaries.
4. chunk_text: Splits a long string into smaller, overlapping text segments of CHUNK_SIZE characters.
5. create_index: Loads all documents, splits them into chunks, computes embeddings for each, and saves the resulting vector store to vector_store.json.
6. load_vector_store: Reads and parses the saved chunk texts and embeddings from vector_store.json into memory.
7. cosine_similarity: Calculates the cosine similarity score between two embedding vectors using NumPy.
8. retrieve: Embeds the user's question, scores it against every indexed chunk, and returns the top_k most similar matches.
9. build_context: Formats the retrieved top chunks along with their metadata (source, chunk ID, similarity score) into a single prompt string.
10. rag: Orchestrates a single query by retrieving matching chunks, printing them, building the context, and displaying the LLM's final answer.
11. check_ollama: Verifies that the local Ollama server is reachable and warns if the configured LLM or embedding models are missing.
12. main: Runs the interactive CLI loop that initializes the vector index and processes user questions or /reindex and /exit commands.
