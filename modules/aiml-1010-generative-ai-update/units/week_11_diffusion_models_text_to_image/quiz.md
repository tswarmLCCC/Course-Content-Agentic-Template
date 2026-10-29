# Week 11 Knowledge Check: Diffusion Models and Text-to-Image Generation

**Course**: AIML 1010: Introduction to Artificial Intelligence  
**Assessment Type**: Multiple Choice Knowledge Check  
**Allowed Attempts**: 3 | **Scoring Policy**: Keep Highest Score | **Points Possible**: 30.0

---

## Assessment Questions

### Question 1
What is the primary advantage of Diffusion Models compared to traditional Generative Adversarial Networks (GANs)?

* A) They require significantly smaller training datasets
* B) They have more stable training dynamics and do not suffer from adversarial mode collapse
* C) They generate images instantaneously in a single forward pass
* D) They do not require any GPU acceleration

### Question 2
How does the forward diffusion process operate in a Denoising Diffusion Probabilistic Model (DDPM)?

* A) It progressively adds small amounts of Gaussian noise to an image over T timesteps until it becomes pure noise
* B) It sharpens an image by removing blur filters
* C) It compresses an image using JPEG encoding
* D) It generates an image from a random seed in one step

### Question 3
What is the neural network (typically a U-Net or DiT) trained to predict during the reverse diffusion process?

* A) The RGB color histogram of the original image
* B) The specific noise component added at timestep t, allowing the system to subtract it and denoise
* C) The camera focal length used to take the picture
* D) The text sentiment of the user prompt

### Question 4
What is the major innovation of Latent Diffusion Models (LDMs, such as Stable Diffusion) over pixel-space diffusion?

* A) Running the diffusion process in a compressed latent space learned by a VAE rather than high-dimensional pixel space
* B) Eliminating the need for neural network weights
* C) Generating 3D models instead of 2D images
* D) Using decision trees instead of convolutional networks

### Question 5
How does text conditioning work in text-to-image models like Stable Diffusion?

* A) Text is encoded via a model like CLIP or T5 and injected into the diffusion U-Net via cross-attention layers
* B) Text is directly converted into pixel RGB values at the top left corner
* C) Text prompt length dictates the output canvas pixel width
* D) The system searches a database of images and crops them

### Question 6
What does Classifier-Free Guidance (CFG) control during diffusion generation?

* A) The physical resolution of the image sensor
* B) The trade-off between prompt fidelity (how strictly the image follows the prompt) and sample diversity/realism
* C) The monetary cost per generation on cloud GPUs
* D) The aspect ratio of the generated image canvas

### Question 7
In image generation, what is 'Inpainting'?

* A) Generating a completely new image from scratch without a prompt
* B) Restoring, replacing, or modifying a specific masked region of an existing image while preserving surrounding context
* C) Converting a 2D image into a vectorized SVG outline
* D) Upscaling an image resolution using nearest-neighbor interpolation

### Question 8
How do Vision Transformers (ViTs) process input images?

* A) They scan images one individual pixel at a time from top-left to bottom-right
* B) They divide the image into non-overlapping patches (e.g. 16x16 pixels), flatten them, and treat each patch as a token sequence with self-attention
* C) They use exclusively 3x3 convolutional kernels with zero attention
* D) They convert all images into grayscale audio waveforms

### Question 9
True or False: Diffusion models can only generate 2D still images and cannot be adapted for video, audio, or 3D synthesis.

* A) True
* B) False

### Question 10
What role does the VAE (Variational Autoencoder) play in latent diffusion architectures?

* A) It encodes high-resolution pixel images into compact latent representations for efficient diffusion, then decodes latents back into pixels
* B) It acts as the primary web search engine for training images
* C) It replaces the cross-attention mechanism between text and image
* D) It regulates cooling fans on GPU hardware

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **B** | GANs suffer from unstable min-max adversarial training and mode collapse. Diffusion models optimize standard variational bounds with stable mean squared error loss. |
| **2** | **A** | The forward process is a fixed Markov chain that systematically adds Gaussian noise to data according to a variance schedule until data structure is destroyed. |
| **3** | **B** | The reverse process neural network learns to predict the noise vector present at step t, enabling iterative denoising to recover clear images. |
| **4** | **A** | Pixel-space diffusion is computationally expensive. LDMs compress images into a low-dimensional latent space using an autoencoder, vastly reducing compute requirements. |
| **5** | **A** | Text encoders (like CLIP or T5) produce vector embeddings for prompt tokens, which guide intermediate image latent representations via cross-attention mechanisms. |
| **6** | **B** | Higher CFG scales force the reverse process to adhere more aggressively to the text prompt conditioning, while lower values yield more creative diversity. |
| **7** | **B** | Inpainting masks an area of an image and uses diffusion conditioning to regenerate plausible, seamless content consistent with the unmasked boundaries. |
| **8** | **B** | ViTs break images into a grid of patches, linearly project them into embeddings, prepend positional embeddings, and process them like text tokens via standard self-attention. |
| **9** | **B** | Diffusion principles have been successfully generalized to generate temporal video frames, audio spectrograms, and 3D NeRFs/Gaussian splats. |
| **10** | **A** | The VAE encoder compresses high-dimensional pixel space into latent space, and the VAE decoder reconstructs the finalized denoised latent array into human-visible pixels. |
