LLaMA - Wikipedia


























Jump to content







Main menu





Main menu
move to sidebar
hide



		Navigation
	


Main pageContentsCurrent eventsRandom articleAbout WikipediaContact usDonate





		Contribute
	


HelpLearn to editCommunity portalRecent changesUpload file



















Search











Search





























Create account

Log in








Personal tools





 Create account Log in





		Pages for logged out editors learn more



ContributionsTalk




























Contents
move to sidebar
hide




(Top)





1Models



Toggle Models subsection





1.1Llama 2







1.2Llama 3









2Architecture and training



Toggle Architecture and training subsection





2.1Architecture







2.2Training datasets







2.3Fine-tuning









3Release and leak







4Dataset reproduction







5Applications







6References







7Further reading







8External links

















Toggle the table of contents







LLaMA



15 languages




CatalàDeutschEspañolفارسیFrançais한국어עברית日本語PortuguêsRuna SimiРусскийСаха тылаSuomiУкраїнська中文

Edit links











ArticleTalk





English

















ReadEditView history







Tools





Tools
move to sidebar
hide



		Actions
	


ReadEditView history





		General
	


What links hereRelated changesUpload fileSpecial pagesPermanent linkPage informationCite this pageGet shortened URLDownload QR codeWikidata item





		Print/export
	


Download as PDFPrintable version

























From Wikipedia, the free encyclopedia


Large language model by Meta AI
For the animal, see Llama. For other uses, see Llama (disambiguation).
Not to be confused with LaMDA.
Llama (Large Language Model Meta AI) is a family of autoregressive large language models released by Meta AI starting in February 2023.[1][2] The latest version is Llama 3 released in April 2024.
The model weights for the first version of Llama were released to the research community under a non-commercial license.[2] Subsequent versions of Llama were made accessible outside academia and released under licenses that permitted some commercial use.[citation needed]
Trained at various different parameter sizes, LLaMA's developers reported that the 13B parameter model's performance on most NLP benchmarks exceeded that of the much larger GPT-3 (with 175B parameters) and that the largest model was competitive with state of the art models such as PaLM and Chinchilla.[1].
Four model sizes were trained for the first version of LLaMA: 7, 13, 33, and 65 billion parameters. Within a week of LLaMA's release, its weights were leaked to the public on 4chan via BitTorrent.[3]


Models[edit]
Llama 2[edit]
On July 18, 2023, in partnership with Microsoft, Meta announced Llama-2, the next generation of LLaMA. Meta trained and released Llama-2 in three model sizes: 7, 13, and 70 billion parameters.[4] The model architecture remains largely unchanged from that of LLaMA-1 models, but 40% more data was used to train the foundational models.[5] The accompanying preprint[5] also mentions a model with 34B parameters that might be released in the future upon satisfying safety targets.
Llama-2 includes foundational models and models fine-tuned for dialog, called Llama-2 Chat. In a further departure from LLaMA-1, all models are released with weights and are free for many commercial use cases. However, due to some remaining restrictions, Meta's description of LLaMA as open source has been disputed by the Open Source Initiative (known for maintaining the Open Source Definition).[6]

Llama 3[edit]
On April 18, 2024, Meta released Llama-3 with two sizes: 8B and 70B parameters. The models have been pre-trained on approximately 15 trillion tokens of text gathered from “publicly available sources” with the instruct models fine-tuned on “publicly available instruction datasets, as well as over 10M human-annotated examples". Meta plans on releasing multimodal models, models capable of conversing in multiple languages, and models with larger context windows. A version with 400B+ parameters is currently being trained.[7]



Name
Release date
Parameters
Context length
Corpus size
Commercial viability?


LLaMA

Feburary 24, 2023


6.7B
13.0B
32.5B
65.2B

2048

1.0-1.4T

No


Llama 2

July 18, 2023


6.7B
13.0B
~34B (unreleased)
69B

4096

2T

Yes


Llama 3

April 18, 2024


8B
70.6B
400B+ (unreleased)

8912

15T

Yes

Architecture and training[edit]

"A conversation between the sun and pluto"

Sun: Hey Pluto, what’s up?
Pluto: Not much. Just hanging out here at the edge of the solar system.
Sun: Yeah, I’ve been meaning to talk to you about that. You’re not a planet anymore.
Pluto: What? Come on, man. That’s not fair.
Sun: I’m sorry, but it’s true. You just don’t meet the criteria anymore.
Pluto: This is bulls**t! I’ve been a planet for over 70 years!
Sun: Things change, Pluto. You’ve just got to accept it.
Pluto: F**k you, Sun! F**k you and your stupid solar system!


– Output of 65 billion parameter LLaMA model after instruction tuning given the prompt "Write a conversation between the sun and pluto"[1]

Architecture[edit]
LLaMA uses the transformer architecture, the standard architecture for language modeling since 2018. 
There are minor architectural differences. Compared to GPT-3, LLaMA 

uses SwiGLU[8] activation function instead of GeLU;
uses rotary positional embeddings[9] instead of absolute positional embedding;
uses root-mean-squared layer-normalization[10] instead of standard layer-normalization.[11]
Increases context length from 2K (Llama 1) tokens to 4K (Llama 2) tokens between.
Training datasets[edit]
LLaMA's developers focused their effort on scaling the model's performance by increasing the volume of training data, rather than the number of parameters, reasoning that the dominating cost for LLMs is from doing inference on the trained model rather than the computational cost of the training process. 
LLaMA 1 foundational models were trained on a data set with 1.4 trillion tokens, drawn from publicly available data sources, including:[1]

Webpages scraped by CommonCrawl
Open source repositories of source code from GitHub
Wikipedia in 20 different languages
Public domain books from Project Gutenberg
The LaTeX source code for scientific papers uploaded to ArXiv
Questions and answers from Stack Exchange websites
Llama 2 foundational models were trained on a data set with 2 trillion tokens. This data set was curated to remove Web sites that often disclose personal data of people. It also upsamples sources considered trustworthy.[5] Llama 2 - Chat was additionally fine-tuned on 27,540 prompt-response pairs created for this project, which performed better than larger but lower-quality third-party datasets. For AI alignment, reinforcement learning with human feedback (RLHF) was used with a combination of 1,418,091 Meta examples and seven smaller datasets. The average dialog depth was 3.9 in the Meta examples, 3.0 for Anthropic Helpful and Anthropic Harmless sets, and 1.0 for five other sets, including OpenAI Summarize, StackExchange, etc.

Fine-tuning[edit]
Llama 1 models are only available as foundational models with self-supervised learning and without fine-tuning. Llama 2 – Chat models were derived from foundational Llama 2 models. Unlike GPT-4 which increased context length during fine-tuning, Llama 2 and Llama 2 - Chat have the same context length of 4K tokens. Supervised fine-tuning used an autoregressive loss function with token loss on user prompts zeroed out. The batch size was 64.
For AI alignment, human annotators wrote prompts and then compared two model outputs (a binary protocol), giving confidence levels and separate safety labels with veto power. Two separate reward models were trained from these preferences for safety and helpfulness using Reinforcement learning from human feedback (RLHF). A major technical contribution is the departure from the exclusive use of Proximal Policy Optimization (PPO) for RLHF – a new technique based on Rejection sampling was used, followed by PPO.
Multi-turn consistency in dialogs was targeted for improvement, to make sure that "system messages" (initial instructions, such as "speak in French" and "act like Napoleon") are respected during the dialog. This was accomplished using the new "Ghost attention" technique during training, which concatenates relevant instructions to each new user message but zeros out the loss function for tokens in the prompt (earlier parts of the dialog).

Release and leak[edit]
LLaMA was announced on February 24, 2023, via a blog post and a paper describing the model's training, architecture, and performance.[1][2] The inference code used to run the model was publicly released under the open-source GPL 3 license.[12] Access to the model's weights was managed by an application process, with access to be granted "on a case-by-case basis to academic researchers; those affiliated with organizations in government, civil society, and academia; and industry research laboratories around the world".[2]
On March 3, 2023, a torrent containing LLaMA's weights was uploaded, with a link to the torrent shared on the 4chan imageboard and subsequently spread through online AI communities.[3] That same day, a pull request on the main LLaMA repository was opened, requesting to add the magnet link to the official documentation.[13][14] On March 4, a pull request was opened to add links to HuggingFace repositories containing the model.[15][13] On March 6, Meta filed takedown requests to remove the HuggingFace repositories linked in the pull request, characterizing it as "unauthorized distribution" of the model. HuggingFace complied with the requests.[16] On March 20, Meta filed a DMCA takedown request for copyright infringement against a repository containing a script that downloaded LLaMA from a mirror, and GitHub complied the next day.[17] As of March 25, Facebook has not responded to the pull request containing the magnet link.[14]
Reactions to the leak varied. Some speculated that the model would be used for malicious purposes, such as more sophisticated spam. Some have celebrated the model's accessibility, as well as the fact that smaller versions of the model can be run relatively cheaply, suggesting that this will promote the flourishing of additional research developments.[3] Multiple commentators, such as Simon Willison, compared LLaMA to Stable Diffusion, a text-to-image model which, unlike comparably sophisticated models which preceded it, was openly distributed, leading to a rapid proliferation of associated tools, techniques, and software.[3][18]

Dataset reproduction[edit]
On April 17, 2023, TogetherAI launched a project named RedPajama to reproduce and distribute an open source version of the LLaMA dataset.[19] The dataset has approximately 1.2 trillion tokens and is publicly available for download.[20]

Applications[edit]
Software developer Georgi Gerganov released llama.cpp as open-source on March 10, 2023. It's a re-implementation of LLaMA in C++, allowing systems without a powerful GPU to run the model locally.[21] The llama.cpp project introduced the GGUF file format, a binary format that stores both tensors and metadata.[22] The format focuses on supporting different quantization types, which can reduce memory usage, and increase speed at the expense of lower model precision.[23]
llamafile created by Justine Tunney is an open-source tool that bundles llama.cpp with the model into a single executable file. Tunney et. al. introduced new optimized matrix multiplication kernels for x86 and ARM CPUs, improving prompt evaluation performance for FP16 and 8-bit quantized data types.[24]
AI startup Groq has made LLaMA models available via it's API.[25][26]
The Stanford University Institute for Human-Centered Artificial Intelligence (HAI) Center for Research on Foundation Models (CRFM) released Alpaca, a training recipe based on the LLaMA 7B model that uses the "Self-Instruct" method of instruction tuning to acquire capabilities comparable to the OpenAI GPT-3 series text-davinci-003 model at a modest cost.[27][28][29] The model files were officially removed on March 21st 2023 over hosting costs and safety concerns, though the code and paper remain online for reference.[30][31]
Meditron is a family of Llama-based finetuned on a corpus of clinical guidelines, PubMed papers, and articles. It was created by researchers at École Polytechnique Fédérale de Lausanne School of Computer and Communication Sciences, and the Yale School of Medicine. It shows increased performance on medical-related benchmarks such as MedQA and MedMCQA.[32][33][34]

References[edit]


^ a b c d e Touvron, Hugo; Lavril, Thibaut; Izacard, Gautier; Martinet, Xavier; Lachaux, Marie-Anne; Lacroix, Timothée; Rozière, Baptiste; Goyal, Naman; Hambro, Eric; Azhar, Faisal; Rodriguez, Aurelien; Joulin, Armand; Grave, Edouard; Lample, Guillaume (2023). "LLaMA: Open and Efficient Foundation Language Models". arXiv:2302.13971 [cs.CL].

^ a b c d "Introducing LLaMA: A foundational, 65-billion-parameter large language model". Meta AI. 24 February 2023.

^ a b c d Vincent, James (8 March 2023). "Meta's powerful AI language model has leaked online — what happens now?". The Verge.

^ "Meta and Microsoft Introduce the Next Generation of LLaMA". Meta. 18 July 2023. Retrieved 21 July 2023.

^ a b c Touvron, Hugo; Martin, Louis; et al. (18 Jul 2023). "LLaMA-2: Open Foundation and Fine-Tuned Chat Models". arXiv:2307.09288 [cs.CL].

^ Edwards, Benj (2023-07-18). "Meta launches LLaMA-2, a source-available AI model that allows commercial applications [Updated]". Ars Technica. Retrieved 2023-08-08.

^ "Introducing Meta Llama 3: The most capable openly available LLM to date". ai.meta.com. April 18, 2024. Retrieved 2024-04-21.

^ Shazeer, Noam (2020-02-01). "GLU Variants Improve Transformer". arXiv:2104.09864 [cs.CL].

^ Su, Jianlin; Lu, Yu; Pan, Shengfeng; Murtadha, Ahmed; Wen, Bo; Liu, Yunfeng (2021-04-01). "RoFormer: Enhanced Transformer with Rotary Position Embedding". arXiv:2104.09864 [cs.CL].

^ Zhang, Biao; Sennrich, Rico (2019-10-01). "Root Mean Square Layer Normalization". arXiv:1910.07467 [cs.LG].

^ Lei Ba, Jimmy; Kiros, Jamie Ryan; Hinton, Geoffrey E. (2016-07-01). "Layer Normalization". arXiv:1607.06450 [stat.ML].

^ "llama". GitHub. Retrieved 16 March 2023.

^ a b VK, Anirudh (6 March 2023). "Meta's LLaMA Leaked to the Public, Thanks To 4chan". Analytics India Magazine. Retrieved 17 March 2023.

^ a b "Save bandwidth by using a torrent to distribute more efficiently by ChristopherKing42 · Pull Request #73 · facebookresearch/llama". GitHub. Retrieved 25 March 2023.

^ "Download weights from hugging face to help us save bandwidth by Jainam213 · Pull Request #109 · facebookresearch/llama". GitHub. Retrieved 17 March 2023.

^ Cox, Joseph (7 March 2023). "Facebook's Powerful Large Language Model Leaks Online". Vice. Retrieved 17 March 2023.

^ OpSec Online LLC (21 March 2023). "github/dmca - Notice of Claimed Infringement via Email". GitHub. Retrieved 25 March 2023.

^ Willison, Simon (11 March 2023). "Large language models are having their Stable Diffusion moment". Simon Willison's Weblog.

^ "RedPajama-Data: An Open Source Recipe to Reproduce LLaMA training dataset". GitHub. Together. Retrieved 4 May 2023.

^ "RedPajama-Data-1T". Hugging Face. Together. Retrieved 4 May 2023.

^ Edwards, Benj (2023-03-13). "You can now run a GPT-3-level AI model on your laptop, phone, and Raspberry Pi". Ars Technica. Retrieved 2024-01-04.

^ "GGUF". huggingface.co. Retrieved 9 May 2024.

^ Labonne, Maxime (29 November 2023). "Quantize Llama models with GGUF and llama.cpp". Medium. Towards Data Science. Retrieved 9 May 2024.

^ Connatser, Matthew. "Llamafile LLM driver project boosts performance on CPU cores". www.theregister.com. Retrieved 10 May 2024.

^ Lee, Jane; Nellis, Stephen. "Groq adapts Meta's chatbot for its own chips in race against Nvidia". Reuters. Retrieved 12 May 2024.

^ "12 Hours Later, Groq Deploys Llama 3 Instruct (8 & 70B) by Meta AI on Its LPU™ Inference Engine - Groq". 19 April 2024.

^ Taori, Rohan; Gulrajani, Ishaan; Zhang, Tianyi; Dubois, Yann; Li, Xuechen; Guestrin, Carlos; Liang, Percy; Hashimoto, Tatsunori B. (13 March 2023). "Alpaca: A Strong, Replicable Instruction-Following Model". Stanford Center for Research on Foundation Models.

^ Wang, Yizhong; Kordi, Yeganeh; Mishra, Swaroop; Liu, Alisa; Smith, Noah A.; Khashabi, Daniel; Hajishirzi, Hannaneh (2022). "Self-Instruct: Aligning Language Models with Self-Generated Instructions". arXiv:2212.10560 [cs.CL].

^ "Stanford CRFM". crfm.stanford.edu.

^ Quach, Katyanna. "Stanford takes costly, risky Alpaca AI model offline". www.theregister.com.

^ "Stanford Researchers Take Down Alpaca AI Over Cost and Hallucinations". Gizmodo. 21 March 2023.

^ "Meditron: An LLM suite for low-resource medical settings leveraging Meta Llama". ai.meta.com.

^ Petersen, Tanya (28 November 2023). "EPFL's new Large Language Model for Medical Knowledge".

^ "epfLLM/meditron". epfLLM. 11 May 2024.


Cite error: A list-defined reference named "repo-alpaca" is not used in the content (see the help page).
Further reading[edit]

Huang, Kalley; O'Regan, Sylvia Varnham (September 5, 2023). "Inside Meta's AI Drama: Internal Feuds Over Compute Power". The Information. Archived from the original on September 5, 2023. Retrieved September 6, 2023.

External links[edit]
Official website
Source code on GitHub




Retrieved from "https://en.wikipedia.org/w/index.php?title=LLaMA&oldid=1223480695"
Categories: 2023 softwareInternet leaksLarge language modelsMeta PlatformsHidden categories: Pages with reference errorsPages with incorrect ref formattingArticles with short descriptionShort description matches WikidataAll articles with unsourced statementsArticles with unsourced statements






 This page was last edited on 12 May 2024, at 12:19 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike License 4.0;
additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.


Privacy policy
About Wikipedia
Disclaimers
Contact Wikipedia
Code of Conduct
Developers
Statistics
Cookie statement
Mobile view













Toggle limited content width