# Repository semantic capsule: zou-group/textgrad

- Commit: `75e912e210864b61999781778cdf756d4468120f`
- Default branch: `main`
- Description: zou-group/textgrad
- Selected evidence files: 1 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

![Logo](assets/logo_full.png)

<!--- BADGES: START --->
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zou-group/TextGrad/blob/main/examples/notebooks/Prompt-Optimization.ipynb)
[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg)][#license-gh-package]
[![Nature](https://img.shields.io/badge/Nature-Paper-green?logo=nature&logoColor=white)](https://www.nature.com/articles/s41586-025-08661-4)
[![Arxiv](https://img.shields.io/badge/arXiv-2406.07496-B31B1B.svg)][#arxiv-paper-package]
[![Documentation Status](https://readthedocs.org/projects/textgrad/badge/?version=latest)][#docs-package]
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textgrad)][#pypi-package]
[![PyPI](https://img.shields.io/pypi/v/textgrad)][#pypi-package]
[![Conda - Platform](https://img.shields.io/conda/pn/conda-forge/textgrad?logo=anaconda&style=flat)][#conda-forge-package]
[![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/textgrad?logo=anaconda&style=flat&color=orange)][#conda-forge-package]

[#license-gh-package]: https://lbesson.mit-license.org/
[#arxiv-paper-package]: https://arxiv.org/abs/2406.07496
[#docs-package]: https://textgrad.readthedocs.io/en/latest/?badge=latest
[#pypi-package]: https://pypi.org/project/textgrad/
[#conda-forge-package]: https://anaconda.org/conda-forge/textgrad
[#nature-link]: https://www.nature.com/articles/s41586-025-08661-4

<!--- BADGES: END --->

## TextGrad: Automatic ''Differentiation'' via Text

An autograd engine -- for textual gradients!

TextGrad is a powerful framework  building automatic ``differentiation'' via text.
TextGrad implements backpropagation through text feedback provided by LLMs, strongly building on the gradient metaphor

We provide a simple and intuitive API that allows you to define your own loss functions and optimize them using text feedback.
This API is similar to the Pytorch API, making it simple to adapt to your usecases.

![Analogy with Torch](assets/analogy.png)


### Updates:

**19th March 2025**

TextGrad published in [Nature](https://www.nature.com/articles/s41586-025-08661-4)!

**Past Updates**:

We are introducing a new engine based on [litellm](https://github.com/BerriAI/litellm). This should allow
you to use any model you like, as long as it is supported by litellm. This means that now
**Bedrock, Together, Gemini and even more** are all supported by TextGrad!

This should be seen as experimental but we plan to depreciate the old engines in the future.

In addition to this, with the new engines it should be easy to enable and disable caching.  

We are in the process of testing these new engines and deprecating the old engines. If you have any issues, please let us know!

The new litellm engines can be loaded with the following code: 

An example of loading a litellm engine:
```python
engine = get_engine("experimental:gpt-4o", cache=False)

# this also works with

set_backward_engine("experimental:gpt-4o", cache=False)
```

Be sure to set the relevant environment variables for the new engines!

An example of forward pass:
```python

import httpx
from textgrad.engine_experimental.litellm import LiteLLMEngine

LiteLLMEngine("gpt-4o", cache=True).generate(content="hello, what's 3+4", system_prompt="you are an assistant")

image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image_data = httpx.get(image_url).content

LiteLLMEngine("gpt-4o", cache=True).generate(content=[image_data, "what is this my boy"], system_prompt="you are an assistant")
```

In the examples folder you will find two new notebooks that show how to use the new engines.


## QuickStart
If you know PyTorch, you know 80% of TextGrad.
Let's walk through the key components with a simple example. Say we want to use GPT-4o to solve a simple
reasoning problem.

The question is *If it takes 1 hour to dry 25 shirts under the sun, how long will it take to dry 30 shirts under the sun? Reason step by step.* (Thanks, [Reddit User](https://www.reddit.com/r/OpenAI/comments/18q479x/comment/kf444es/))

```python
import textgrad as tg

tg.set_backward_engine("gpt-4o", override=True)

# Step 1: Get an initial response from an LLM.
model = tg.BlackboxLLM("gpt-4o")
question_string = ("If it takes 1 hour to dry 25 shirts under the sun, "
                   "how long will it take to dry 30 shirts under the sun? "
                   "Reason step by step")

question = tg.Variable(question_string,
                       role_description="question to the LLM",
                       requires_grad=False)

answer = model(question)
```

> :warning: **answer: To determine how long it will take to dry 30 shirts under the sun,**
> **we can use a proportional relationship based on the given information.**
> **Here’s the step-by-step reasoning: [.....]**
> **So, it will take 1.2 hours (or 1 hour and 12 minutes) to dry 30 shirts under the sun.**


As you can see, **the model's answer is incorrect.** We can optimize the answer using TextGrad to get the correct answer.

```python

answer.set_role_description("concise and accurate answer to the question")

# Step 2: Define the loss function and the optimizer, just like in PyTorch!
# Here, we don't have SGD, but we have TGD (Textual Gradient Descent)
# that works with "textual gradients".
optimizer = tg.TGD(parameters=[answer])
evaluation_instruction = (f"Here's a question: {question_string}. "
                           "Evaluate any given answer to this question, "
                           "be smart, logical, and very critical. "
                           "Just provide concise feedback.")


# TextLoss is a natural-language specified loss function that describes
# how we want to evaluate the reasoning.
loss_fn = tg.TextLoss(evaluation_instruction)
```
> :brain: **loss: [...] Your step-by-step reasoning is clear and logical,**
> **but it contains a critical flaw in the assumption that drying time is**
> **directly proportional to the number of shirts. [...]**

```python
# Step 3: Do the loss computation, backward pass, and update the punchline.
# Exact same syntax as PyTorch!
loss = loss_fn(answer)
loss.backward()
optimizer.step()
answer
```

> :white_check_mark: **answer: It will still take 1 hour to dry 30 shirts under the sun,**
> **assuming they are all laid out properly to receive equal sunlight.**

We have many more examples around how TextGrad can optimize all kinds of variables -- code, solutions to problems, molecules, prompts, and all that!

### Tutorials

We have prepared a couple of tutorials to get you started with TextGrad. The order of this
tutorial is what we would recommend to follow for a beginner. You can run them directly in Google Colab by clicking on the links below (but
you need an OpenAI/Anthropic key to run the LLMs).

<div align="center">

| Tutorial                                           | Difficulty                                                      | Colab Link                                                                                                                                                                                                    |
|----------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Introduction to TextGrad Primitives             | ![](https://img.shields.io/badge/Level-Beginner-green.svg)      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zou-group/TextGrad/blob/main/examples/notebooks/Tutorial-Primitives.ipynb)              |
| 2. Solution Optimization                           | ![](https://img.shields.io/badge/Level-Beginner-green.svg)      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zou-group/TextGrad/blob/main/examples/notebooks/Tutorial-Solution-Optimization.ipynb)   |
| 3. Optimizing a Code Snippet and Define a New Loss | ![](https://img.shields.io/badge/Level-Beginner-green.svg)      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zou-group/textgrad/blob/main/examples/notebooks/Tutorial-Test-Time-Loss-for-Code.ipynb) |
| 4. Prompt Optimization                             | ![](https://img.shields.io/badge/Level-Intermediate-yellow.svg) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zou-group/TextGrad/blob/main/examples/notebooks/Tutorial-Prompt-Optimization.ipynb)     |
| 5. MultiModal Optimization                         | ![](https://img.shields.io/badge/Level-Beginner-green.svg)      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zou-group/TextGrad/blob/main/examples/notebooks/Tutorial-MultiModal.ipynb)              |

</div>



### Installation

You can install TextGrad using any of the following methods.

**With `pip`**:

```bash
pip install textgrad
```

**With `conda`**:

```sh
conda install -c conda-forge textgrad
```

> :bulb: The conda-forge package for `textgrad` is maintained [here](https://github.com/conda-forge/textgrad-feedstock).

**Bleeding edge installation with `pip`**:

```sh
pip install git+https://github.com/zou-group/textgrad.git
```

**Installing textgrad with vllm**:

```sh
pip install textgrad[vllm]
```

See [here](https://pip.pypa.io/en/stable/cli/pip_install/) for more details on various methods of pip installation.

## More detailed examples

### Minimal Instance Optimization Example

TextGrad can optimize unstructured variables, such as text. Let us have an initial solution to a math problem that we want to improve. Here's how to do it with TextGrad, using GPT-4o:

```python
tg.set_backward_engine("gpt-4o")

initial_solution = """To solve the equation 3x^2 - 7x + 2 = 0, we use the quadratic formula:
x = (-b ± √(b^2 - 4ac)) / 2a
a = 3, b = -7, c = 2
x = (7 ± √((-7)^2 - 4 * 3(2))) / 6
x = (7 ± √(7^3) / 6
The solutions are:
x1 = (7 + √73)
