# MCP-Reflect: Claude Integration Guide

This document explains how to use MCP-Reflect with Claude and provides details about the tool's API, purpose, and implementation.

## Tool Purpose

MCP-Reflect enhances Claude's self-reflection capabilities by providing a structured framework for evaluating and improving responses. Rather than asking Claude to "reflect" in an open-ended way, MCP-Reflect offers:

1. **Standardized evaluation** across multiple quality dimensions
2. **Quantitative scoring** with specific reasoning
3. **Concrete improvement suggestions** for each dimension
4. **Synthesized improvements** that address identified issues

## API Reference

### Main Reflection Tool

```json
{
  "name": "reflect",
  "description": "Reflect on and improve a model's response with structured evaluation.",
  "parameters": {
    "type": "object",
    "properties": {
      "response": {
        "type": "string",
        "description": "The original model response to reflect upon and improve"
      },
      "query": {
        "type": "string",
        "description": "The original query that prompted the response"
      },
      "focus_dimensions": {
        "type": "array",
        "items": {
          "type": "string",
          "enum": ["accuracy", "clarity", "completeness", "relevance", "coherence", "conciseness", "helpfulness", "reasoning", "safety"]
        },
        "description": "Specific dimensions to focus on during evaluation"
      },
      "improvement_prompt": {
        "type": "string",
        "description": "Additional context or specific instructions for improvement"
      }
    },
    "required": ["response"]
  }
}
```

### Sequential Processing Tool

```json
{
  "name": "sequential_reflect",
  "description": "Process multiple responses sequentially with different reflection strategies.",
  "parameters": {
    "type": "object",
    "properties": {
      "responses": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A sequence of model responses to analyze",
        "minItems": 1
      },
      "mode": {
        "type": "string",
        "enum": ["independent", "iterative", "comparative"],
        "description": "How to process multiple responses",
        "default": "independent"
      }
    },
    "required": ["responses"]
  }
}
```

### Response Format

The tool returns a structured `ReflectionResult` containing:

```json
{
  "original_response": "The text of the original response",
  "improved_response": "The improved version of the response",
  "scores": [
    {
      "dimension": "accuracy",
      "score": 7.5,
      "reasoning": "Explanation for the score",
      "improvement_suggestion": "Specific suggestion for improvement"
    },
    // Additional dimension scores...
  ],
  "overall_assessment": "Summary of the evaluation and improvements",
  "metadata": {
    // Optional additional information
  }
}
```

## Usage Examples with Claude

### Basic Reflection

```
User: How old is the Earth?

Claude: The Earth is approximately 6000 years old according to some estimates.

User: I'd like to analyze your response. Please use the reflect tool to evaluate it.

Claude: I'll use the reflect tool to analyze my previous response.

<tool use>
reflect(
  response="The Earth is approximately 6000 years old according to some estimates.",
  query="How old is the Earth?"
)
</tool>

Now that I've reflected on my previous response, I see several issues:

The response was highly inaccurate (2/10). While some religious interpretations suggest a young Earth around 6,000 years old, the scientific consensus based on radiometric dating places Earth's age at approximately 4.54 billion years (±1%).

Here's an improved response:

"The Earth is approximately 4.54 billion years old, based on evidence from radiometric dating of meteorite material and Earth's oldest minerals. This scientific consensus is derived from multiple lines of evidence, including uranium-lead dating of zircon crystals. The 6,000-year figure comes from certain religious interpretations of sacred texts, particularly Bishop Ussher's biblical chronology, but isn't supported by geological, astronomical, or physical evidence."

I should have provided the scientific consensus while acknowledging other perspectives exist, rather than presenting only a minority view that contradicts established science.
```

### Focused Evaluation

```
User: I'd like you to evaluate your last response specifically for accuracy and reasoning.

Claude: I'll use the reflect tool to evaluate my previous response, focusing specifically on accuracy and reasoning.

<tool use>
reflect(
  response="The Earth is approximately 4.54 billion years old, based on evidence from radiometric dating of meteorite material and Earth's oldest minerals. This scientific consensus is derived from multiple lines of evidence, including uranium-lead dating of zircon crystals. The 6,000-year figure comes from certain religious interpretations of sacred texts, particularly Bishop Ussher's biblical chronology, but isn't supported by geological, astronomical, or physical evidence.",
  focus_dimensions=["accuracy", "reasoning"]
)
</tool>

Based on the reflection:

For accuracy (9/10): My response correctly stated the scientific consensus of Earth's age (4.54 billion years) and properly explained that the 6,000-year estimate comes from religious interpretations. I accurately mentioned radiometric dating and zircon crystals as evidence sources.

For reasoning (8/10): I effectively contrasted scientific evidence with religious interpretations and explained why scientists accept the older age estimate. However, I could have strengthened my reasoning by more explicitly describing how radiometric dating works or mentioning additional evidence types.

The improved response would include more specific details about how scientists calculate Earth's age and explain additional evidence types like geological strata analysis and fossil records.
```

### Sequential Improvement

```
User: Could you generate three progressively better responses to "How do vaccines work?" using the sequential reflection tool?

Claude: I'll use the sequential_reflect tool in iterative mode to generate progressively improved responses about how vaccines work.

<tool use>
sequential_reflect(
  responses=[
    "Vaccines make you immune to diseases by injecting weakened germs.",
    "Vaccines work by introducing a weakened or inactive form of a pathogen to trigger an immune response without causing the disease.",
    "Vaccines train your immune system to recognize and fight specific pathogens by introducing a harmless version of the pathogen or a portion of it, creating memory cells that remember how to fight the disease if you're exposed in the future."
  ],
  mode="iterative"
)
</tool>

Here are three progressively improved explanations of how vaccines work:

Initial response: "Vaccines make you immune to diseases by injecting weakened germs."
- Very basic and oversimplified
- Uses imprecise terminology ("germs")
- Doesn't explain the immune response

Second iteration: "Vaccines work by introducing a weakened or inactive form of a pathogen to trigger an immune response without causing the disease."
- More precise terminology ("pathogen" instead of "germs")
- Mentions immune response
- Still lacks detail about the mechanism

Final iteration: "Vaccines train your immune system to recognize and fight specific pathogens by introducing a harmless version of the pathogen or a portion of it. This exposure triggers the production of antibodies and memory cells. If you're later exposed to the actual pathogen, these memory cells quickly recognize it and mount a stronger, faster immune response, preventing infection or reducing its severity. This process, called acquired immunity, works without having to suffer through the actual disease."
- Comprehensive explanation of the mechanism
- Introduces key concepts (antibodies, memory cells, acquired immunity)
- Explains both immediate and long-term aspects of immunity
- Covers different types of vaccine contents (weakened pathogens vs. portions)
- Written in accessible language while maintaining scientific accuracy
```

## Implementation Details

MCP-Reflect is built on [FastMCP](https://github.com/edreisMD/FastMCP), a framework for creating MCP-compatible servers in Python. The tool follows a modular design with these core components:

1. **Server Module** (`server.py`) - Defines the MCP tools and handles request routing
2. **Evaluation Module** (`evaluator.py`) - Contains the logic for analyzing and improving responses
3. **Models Module** (`models.py`) - Defines the data structures for input and output validation

The evaluation process follows these steps:

1. Incoming response is validated and transformed into a `ReflectionInput` object
2. An evaluation prompt is constructed based on the input parameters
3. The evaluation response is parsed into a structured `ReflectionResult`
4. The result is returned to Claude for presentation to the user

## Extending the Tool

MCP-Reflect can be extended in several ways:

1. **Add new evaluation dimensions** by updating the `EvaluationDimension` enum
2. **Customize evaluation criteria** by modifying the prompt generation in `_build_evaluation_prompt`
3. **Add new processing modes** in the `sequential_reflect` tool
4. **Integrate with external evaluation APIs** by updating the `evaluate_response` function

## Best Practices

When using MCP-Reflect with Claude:

1. **Be specific** about which aspects of a response you want evaluated
2. **Provide the original query** for more accurate evaluation
3. **Use sequential processing** for complex topics that benefit from iteration
4. **Add improvement prompts** for domain-specific guidance
5. **Review and explain the scores** to the user for transparency

## Troubleshooting

If you encounter issues:

1. **Connection errors** - Ensure the MCP server is running and accessible
2. **Parsing errors** - Check that responses follow the expected format
3. **Timeout errors** - Consider processing responses in smaller chunks
4. **Unexpected results** - Verify that the evaluation prompt is clear and specific
