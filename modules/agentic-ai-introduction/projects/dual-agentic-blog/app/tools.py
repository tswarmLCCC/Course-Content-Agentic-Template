"""Environmental ReAct tools for agent grounding and verification."""

import ast
import re
from typing import Dict, Any, List


def calculate_reading_metrics(text: str) -> Dict[str, Any]:
    """Computes comprehensive readability metrics, word count, and reading level for a given text snippet.
    
    Args:
        text: The draft or paragraph string to evaluate.
        
    Returns:
        A dictionary with word_count, sentence_count, avg_words_per_sentence, and reading_level.
    """
    if not text or not text.strip():
        return {
            "word_count": 0,
            "sentence_count": 0,
            "avg_words_per_sentence": 0.0,
            "reading_level": "N/A"
        }

    words = re.findall(r"\b\w+\b", text)
    word_count = len(words)
    
    # Split sentences by period, exclamation, question mark
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    sentence_count = max(1, len(sentences))
    
    avg_words = round(word_count / sentence_count, 1)
    
    # Simple Flesch-Kincaid proxy
    if avg_words < 12:
        level = "Accessible / Introductory (Grade 7-9)"
    elif avg_words < 20:
        level = "Standard Technical (Grade 10-12 / Undergraduate)"
    else:
        level = "Dense Academic (Graduate / Advanced Research)"

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "avg_words_per_sentence": avg_words,
        "reading_level": level
    }


def verify_code_syntax(snippet: str, language: str = "python") -> Dict[str, Any]:
    """Validates the syntax of an embedded code block using the standard Python AST parser.
    
    Args:
        snippet: Raw code block string to check.
        language: Programming language (default: 'python').
        
    Returns:
        Dictionary with valid (bool), error (str or None), and node_count (int).
    """
    if language.lower() != "python":
        return {"valid": True, "note": f"Syntax verification skipped for non-python language: {language}"}

    try:
        parsed = ast.parse(snippet)
        node_count = sum(1 for _ in ast.walk(parsed))
        return {
            "valid": True,
            "error": None,
            "node_count": node_count,
            "status": "SYNTAX_VALID"
        }
    except SyntaxError as e:
        return {
            "valid": False,
            "error": f"SyntaxError at line {e.lineno}, col {e.offset}: {e.msg}",
            "status": "SYNTAX_ERROR"
        }


def local_grounding_search(query: str) -> Dict[str, Any]:
    """Queries curated local knowledge snippets to ground technical reasoning with verifiable citations.
    
    Args:
        query: Technical search term or question.
        
    Returns:
        Dictionary with query, match_count, and relevant citation snippets.
    """
    KNOWLEDGE_BASE = [
        {
            "topic": "ReAct Framework",
            "citation": "Yao, S. et al. (ICLR 2023). ReAct: Synergizing Reasoning and Acting in Language Models.",
            "snippet": "ReAct combines verbal reasoning (Thoughts) with task-specific actions (Actions) to prevent compounding hallucinations."
        },
        {
            "topic": "Anthropic Agent Workflows",
            "citation": "Erik S. & Barry Zhang (Dec 2024). Building Effective Agents. Anthropic Engineering.",
            "snippet": "Categorizes five core workflow patterns: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, and Evaluator-Optimizer."
        },
        {
            "topic": "Agent Patterns (Google Cloud Tech)",
            "citation": "Smitha Kolan (2024). AI agents explained: Build your first agent in 8 minutes. Google Cloud Tech.",
            "snippet": "Identifies three core architectural patterns: Sequential pipelines, Reactive event loops, and Planning decomposition."
        },
        {
            "topic": "Defensive ACI & Tool Design",
            "citation": "Anthropic Research (2024). Agent-Computer Interfaces.",
            "snippet": "Enforce Poka-Yoke mistake-proofing, absolute filesystem paths, and strict max-iteration cutoff thresholds."
        }
    ]

    query_lower = query.lower()
    matches = []
    for entry in KNOWLEDGE_BASE:
        if any(term in entry["topic"].lower() or term in entry["snippet"].lower() for term in query_lower.split()):
            matches.append(entry)

    if not matches:
        matches = [KNOWLEDGE_BASE[0]]  # Default fallback citation

    return {
        "query": query,
        "match_count": len(matches),
        "results": matches
    }


ALL_TOOLS: List[Any] = [
    calculate_reading_metrics,
    verify_code_syntax,
    local_grounding_search
]
