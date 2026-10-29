# AIML 1010: Generative AI & Agentic Curriculum Update

> **Standalone Modular Course Import Bundle for Canvas LMS**  
> *Designed to drop directly into an existing AIML 1010 Canvas course shell without altering the host syllabus or homepage.*

---

## 1. Overview & Objectives

This package ingests and standardizes 9 new Generative AI and Agentic AI curricular modules from `ref/AIML 1010 Update/New Modules/` into a production-grade Canvas Common Cartridge (`.imscc`).

### Deliverable:
- **Modular Cartridge**: `AIML_1010_Generative_AI_Update_Modules_Import.imscc`
- **Scope**: 9 Modular Units, each containing:
  1. **Reading Page**: DesignPLUS-styled WikiPage with unit objectives, slide deck briefing notes, and direct link to the notes-annotated slide PDF (`$IMS-CC-FILEBASE$/slides/...`).
  2. **Applied Assignment**: Native Canvas Assignment converted from the hands-on student lab decks (`[Assignment] ... .pptx`).
  3. **Knowledge Check (Quiz)**: Verified, error-corrected QTI 1.2 assessment converted from the source spreadsheets.
  4. **Discussion Board**: Canvas native threaded DiscussionTopic structured with asynchronous participation guidelines and 3-4 conceptual/applied prompts.
  5. **Annotated Slide Deck PDF**: 540x720 Notes Pages PDF containing the full slide visuals and instructor speaker notes.

---

## 2. Included Modules (9 Units)

| Module ID | Module Title (Hyphenated per ADR-003) | Focus & Technologies |
| :--- | :--- | :--- |
| **01** | `Module 01 - Demystifying Agentic AI` | Autonomous Agents, Reflex vs Goal/Utility Agents, Tool Use, Human-in-the-Loop |
| **02** | `Week 03 - Prompt Engineering I` | Foundations of Prompt Engineering, NLP Evolution, RGC Framework, Zero/Few-shot |
| **03** | `Week 04 - Prompt Engineering II` | Advanced Prompting, Chain-of-Thought, Directional Stimulus, ReAct, Prompt Chaining |
| **04** | `Week 10 - Transformers and Evolution of Large Language Models` | Self-Attention, Transformer Architecture, Sequence-to-Sequence, Emergent Abilities |
| **05** | `Week 11 - Diffusion Models and the Evolution of Text-to-Image Generation` | Latent Diffusion, Denoising, Text Conditioning (CLIP), Image Synthesis |
| **06** | `Week 12 - Pre-Training Generative AI Models` | Pre-Training Pipeline, Tokenization (BPE), Web Scraping/Filtering, Compute Scaling |
| **07** | `Week 13 - Fine-Tuning Generative AI Models` | SFT, LoRA/PEFT, Transfer Learning, Domain Adaptation, Dataset Formatting |
| **08** | `Week 15 - Prototyping Generative AI Applications` | Fast Prototyping, Streamlit, API Integration, Gradio, User Evaluation |
| **09** | `Week 16 - LLM Alignment and the Responsible Use of Generative AI` | RLHF, Constitutional AI, Bias, Jailbreaking, Watermarking, Red Teaming |

---

## 3. Directory Layout

```
modules/aiml-1010-generative-ai-update/
├── README.md
├── AIML_1010_Generative_AI_Update_Modules_Import.imscc
├── specs/
│   └── 001-module-specification-and-scaffold/
│       ├── spec.md
│       ├── plan.md
│       └── tasks.md
├── scripts/
│   └── export_slide_pdfs.ps1
└── units/
    ├── module_01_agentic_ai/
    ├── week_03_prompt_engineering_i/
    ├── week_04_prompt_engineering_ii/
    ├── week_10_transformers_llm_evolution/
    ├── week_11_diffusion_models_text_to_image/
    ├── week_12_pretraining_generative_ai/
    ├── week_13_finetuning_generative_ai/
    ├── week_15_prototyping_genai_apps/
    └── week_16_llm_alignment_responsible_ai/
```
